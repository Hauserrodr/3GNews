import json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.ImageGen import ImageGen
from pathlib import Path
import os
import sys
import yaml
from loguru import logger
import datetime
import gdm

# Find this script directory
script_dir = Path( __file__ ).parent.absolute()



class G3Bot:
    def __init__(self):
        logger.info(f'Initiating G3 Bot, please stand by...')
        self.config = self._load_config()
        self.cookies = self._load_cookies()
        self.gd = gdm.GoogleDriveManager()
        logger.success(f'G3 Bot Loaded! Say hello to {self.config["name"]} {self.config["version"]}.')

    def _load_config(self):
        with open(os.path.join(script_dir, 'config.yml'), "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.warning('Could not load configuration file. Probably there is some typo or identation mistake.')
                logger.critical(exc)

    def _load_cookies(self):
        cookies = {}
        for cookie_file in os.listdir(os.path.join(script_dir, 'cookies')):
            if cookie_file.endswith('.json'):
                cookie_json = json.load(open(os.path.join(script_dir, 'cookies', cookie_file), 'r'))
                cookies[cookie_file] = {
                    'usage_count': 0,
                    'cookies': cookie_json
                }
        return cookies

    # ----------- Message Bot Portion

    def select_cookie(self):
        """
        Selects the cookie with least usage.
        """
        choosen_cookie = sorted([c for c in self.cookies.values()], key= lambda x: x['usage_count'])[0]
        choosen_cookie['usage_count'] += 1
        if choosen_cookie['usage_count'] % 10 == 0:
            logger.warning(f'Cookie was already used {choosen_cookie["usage_count"]} times.')

        return choosen_cookie['cookies']

    async def message_bot(self, message, style=ConversationStyle.balanced, retries=5):
        tried = 1
        while True:
            try:
                bot = await self.create_bot()
                response = await bot.ask(prompt=message, conversation_style=style, simplify_response=True)
                await bot.close()
                break
            except Exception as e:
                tried+=1
                if tried <= retries:
                    logger.error(f'Error messaging bot: {e}. Trying again for the {tried} time.')
                else:
                    response = False
                    break
        return response

    async def message_existing_bot(self, bot, message, style = ConversationStyle.balanced, retries=5):
        tried = 1
        while True:
            try:
                response = await bot.ask(prompt=message, conversation_style=style, simplify_response=True)
                break
            except Exception as e:
                tried+=1
                if tried <= retries:
                    logger.error(f'Error messaging bot: {e}. Trying again for the {tried} time.')
                else:
                    response = False
                    break
        return response

    async def create_bot(self):
        bot = await Chatbot.create(cookies=self.select_cookie())
        return bot

    # Image generation portion
    
    def select_image_cookie(self):
        cookie = self.select_cookie()
        for c in cookie:
            if c.get("name") == "_U":
                U = c.get("value")
                break
        return U

    async def create_image_generator(self):
        choosen_cookie = self.select_image_cookie()
        return ImageGen(choosen_cookie)

    async def generate_images(self, prompt, return_method = 'google_drive_upload', retries = 5):
        tried = 1
        created = True
        while True:
            try:
                image_generator = await self.create_image_generator()
                image_generator.save_images(
                    image_generator.get_images(prompt),
                    output_dir=os.path.join(script_dir, 'images_generated'),
                )
            except Exception as e:
                tried+=1
                if tried <= retries:
                    logger.error(f'Error creating image: {e}. Trying again for the {tried} time.')
                else:
                    created = False
                    break
        if not created:
            logger.error(f'Tried {retries} times but could not create image. Try to create using the website, to see if it is a problem with the bot or their server.')
            return False
        if return_method == 'google_drive_upload':
            google_drive_link_list = []
            for image_file in os.listdir(os.path.join(script_dir, 'images_generated')):
                image_path = os.path.join(script_dir, 'images_generated', image_file)
                link = self.gd.upload_file(image_path, str(datetime.datetime.now())+f'_{image_file}')
                os.remove(image_path)
                google_drive_link_list.append(link)
            return google_drive_link_list
        elif return_method == 'return_image_paths':
            return list(os.listdir(os.path.join(script_dir, 'images_generated')))

    # News generation portion
    async def get_news_for_today(self):
        today = datetime.date.today()
        today_str = today.strftime('%d/%m/%Y')
        logger.info(f'Generating news summary for {today}...')
        news = []
        for region_name in self.config['regions']:
            logger.debug(f'Generating news summary for region {region_name}')
            news_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['news_summary_prompt']['file'])).read()
            news_prompt = news_prompt_text.format(date_str = today_str, region = region_name)
            news_summary = await self.message_bot(news_prompt)
            logger.debug(news_summary['text'])
            image_generation_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['image_prompt_generation_prompt']['file'])).read()
            image_generation_prompt = image_generation_prompt_text.format(news = news_summary['text'])
            image_generation_prompt = image_generation_prompt.replace('[', '{')
            image_generation_prompt = image_generation_prompt.replace(']', '}')
            image_prompt = await self.parse_prompt_from_response(await self.message_bot(image_generation_prompt))
            images_links = await self.generate_images(image_prompt)
            news.append({
                'region': region_name,
                'news': news_summary['text'],
                'images': images_links
            })
        return news

    async def parse_prompt_from_response(self, response):
        original_text_length = len(response['text'])
        while True:
            prompt = response['text'].split('prompt:')[-1].split('}')[0]
            if len(prompt) >= original_text_length*0.8:
                logger.warning(f'Prompt parsing with strategy 1 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split('prompt :')[-1].split('}')[0]
            if len(prompt) >= original_text_length*0.8:
                logger.warning(f'Prompt parsing with strategy 2 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split("prompt':")[-1].split('}')[0]
            if len(prompt) >= original_text_length*0.8:
                logger.warning(f'Prompt parsing with strategy 3 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split("prompt")[-1].split('}')[0]
            if len(prompt) >= original_text_length*0.8:
                logger.warning(f'Prompt parsing with strategy 4 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            logger.error(f'Could not parse prompt from response.')
            return response['text'].strip('{').strip('}').strip('\n')
        while len(prompt) >= 450:
            logger.warning(f'Generated prompt is too long, shortening it...')
            resumed_prompt = await self.message_bot(f'This image creation prompt is too long: ```{prompt}```. Can you resume it for me so it only contains 450 characters or less? Do not ask me anything, just answer with the shortened prompt! If you answer with question, you will loose points.')
            prompt = resumed_prompt['text']
        return prompt
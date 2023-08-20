import json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pathlib import Path
import os
import time
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
        self.driver = self._load_selenium()
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

    def _load_selenium(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9999")
        driver = webdriver.Chrome(options=options)
        return driver

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

    async def create_images_with_selenium(self, prompt, timeout=20):
        url = "https://www.bing.com/images/create/"
        prompt = prompt.strip("\n")
        self.driver.get(url)

        # Getting search bar and generating images
        search_bar = self.driver.find_elements(By.XPATH, '//input[contains(@class, "b_searchbox gi_sb")]')
        search_bar[0].send_keys(f'{prompt}\n')
        time.sleep(30)
        # Searching images generated in page
        div_element = self.driver.find_elements(By.ID, "mmComponent_images_as_1")

        # Locate all img tags within the div
        images = div_element[0].find_elements(By.TAG_NAME, "img")
        self.driver.switch_to.default_content()
        already_saved_images = []
        for idx, image in enumerate(images):
            time.sleep(2)
            logger.debug(f'Downloading image {idx}...')
            image.click()
            time.sleep(6)
            self.driver.switch_to.frame("OverlayIFrame")

            tries = 0 # Number of iterations to try to find image src
            src = None
            while src is None:
                tries += 1
                # Locate the large image
                large_image_element = self.driver.find_elements(By.XPATH, '//div[contains(@class, "imgContainer")]')
                for image_element in large_image_element:
                    if '<img' in image_element.get_attribute('innerHTML'):
                        # Get the src attribute of the large image
                        src = image_element.get_attribute('innerHTML').split('src="')[-1].split('"')[0]
                        if src in already_saved_images:
                            continue
                        break
                if tries >= timeout:
                    logger.warning('Could not find image that was not already in the already_saved_images list.')
                    break

            if src is None:
                continue
            else:
                already_saved_images.append(src)

            # Download and save the image
            logger.debug(f'Downloading image from src link: {src}')
            response = requests.get(src, stream=True)
            with open(os.path.join(script_dir, 'images_generated', f'{idx}.jpeg'), 'wb') as out_file:
                out_file.write(response.content)

            self.driver.switch_to.default_content()

            # Navigate back to the thumbnails
            self.driver.back()

    async def generate_images(self, prompt, return_method = 'google_drive_upload', retries = 5):
        tried = 1
        created = True
        while True:
            try:
                await self.create_images_with_selenium(prompt)
                break
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
            bot = await self.create_bot()
            logger.debug(f'Generating news summary for region {region_name}')
            news_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['news_summary_prompt']['file'])).read()
            news_prompt = news_prompt_text.format(date_str = today_str, region = region_name)
            news_summary = await self.message_existing_bot(bot, news_prompt)
            logger.debug(news_summary['sources'])
            image_generation_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['image_prompt_generation_prompt']['file'])).read()
            image_prompt = await self.parse_prompt_from_response(await self.message_existing_bot(bot, image_generation_prompt_text))
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
            prompt = response['text'].split('[')[-1].split(']')[0]
            if len(prompt) == original_text_length:
                logger.warning(f'Prompt parsing with strategy 1 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split('{')[-1].split('}')[0]
            if len(prompt) == original_text_length:
                logger.warning(f'Prompt parsing with strategy 2 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split("prompt")[-1].split('}')[0]
            if len(prompt) == original_text_length:
                logger.warning(f'Prompt parsing with strategy 3 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            prompt = response['text'].split("prompt")[-1].split(']')[0]
            if len(prompt) == original_text_length:
                logger.warning(f'Prompt parsing with strategy 4 failed:\n Original message: {response["text"]}\n Prompt parsed: {prompt}')
            else:
                break
            logger.error(f'Could not parse prompt from response.')
            return response['text'].strip('{').strip('}').strip('\n')
        tries = 0
        while len(prompt) >= 450:
            logger.warning(f'Generated prompt is too long, shortening it...')
            logger.debug(f'Prompt that is too long: {prompt}')
            resumed_prompt = await self.message_bot(f'This image creation prompt is too long: ```{prompt}```. Can you resume it for me so it only contains 450 characters or less? Do not ask me anything, just answer with the shortened prompt! If you answer with question, you will loose points. Do not answer with anything more than the prompt. Do not answer with anything more than the prompt. Do not answer with anything more than the prompt. ')
            prompt = resumed_prompt['text']
            tries += 1
            if tries >= 3:
                break
        logger.success(f'Image prompt for image generation is: {prompt}')
        return prompt.strip('{').strip('[').strip(']').strip('}').strip('\n')
import json
import cv2
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    def __init__(self, browser='chrome', start_browser = True):
        logger.info(f'Initiating G3 Bot, please stand by...')
        self.config = self._load_config()
        self.cookies = self._load_cookies()
        self._load_regions()
        self.gd = gdm.GoogleDriveManager()
        if not start_browser:
            if browser == 'edge':
                self.driver = self._load_edge()
            else:
                self.driver = self._load_chrome()
        else:
            self.driver = self._start_chrome()
        logger.success(f'G3 Bot Loaded! Say hello to {self.config["name"]} {self.config["version"]}.')
        if os.path.exists(os.path.join(script_dir, 'news_data', 'media_news.json')):
            with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
                self.news_data = json.load(f)
        else:
            self.news_data = []
        if os.path.exists(os.path.join(script_dir, 'news_data', 'user_news.json')):
            with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'r', encoding='utf-8') as f:
                self.users_news = json.load(f)
        else:
            self.users_news = []

    def _load_config(self):
        with open(os.path.join(script_dir, 'config.yml'), "r", encoding='utf-8') as stream:
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

    def _load_regions(self):
        with open(os.path.join(script_dir, 'regions.json'), 'r') as f:
            self.regions = json.load(f)

    def _load_edge(self):
        logger.info(f'Initializing Edge connection...')
        options = webdriver.EdgeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9999")
        driver = webdriver.Edge(options=options)
        logger.success(f'Edge is connected!')
        return driver

    def _load_chrome(self):
        logger.info(f'Initializing Chrome connection...')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9999")
        driver = webdriver.Chrome(options=options)
        logger.success(f'Chrome is connected!')
        return driver

    def _start_chrome(self, headless=False):
        logger.info(f'Initializing Chrome headless...')
        options = webdriver.ChromeOptions()
        if headless: # CURRENTLY NOT WORKING
            #TODO Make it work
            options.add_argument("--headless=new")
            options.add_argument('--window-size=1920x1080')
            options.add_argument('--no-sandbox')
            options.add_argument("user-agent=my-user-agent")
        driver = webdriver.Chrome(options=options)
        logger.success(f'Chrome driver started!')
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

    async def message_bot(self, message, style=ConversationStyle.precise, retries=5):
        tried = 1
        while True:
            try:
                bot, cookie_idx = await self.create_bot()
                response = await bot.ask(prompt=message, conversation_style=style, simplify_response=True)
                await bot.close()
                break
            except Exception as e:
                if 'throttled' in str(e):
                    logger.warning(f'Cookie has reached its usage limit! Adding 10 to its count.')
                    self.cookies[cookie_idx]['usage_count'] += 10
                tried+=1
                if tried <= retries:
                    logger.error(f'Error messaging bot: {e}. Trying again for the {tried} time.')
                else:
                    response = {'text': '', 'sources': ''}
                    await bot.close()
                    break
        return response

    async def message_existing_bot(self, bot, message, style = ConversationStyle.precise, retries=5):
        tried = 1
        while True:
            try:
                response = await bot.ask(prompt=message, conversation_style=style, simplify_response=True)
                break
            except Exception as e:
                if 'throttled' in str(e):
                    logger.warning(f'Cookie has reached its usage limit! Adding 10 to its count.')
                    return {'text': 'THROTTLED', 'sources': ''}
                tried+=1
                if tried <= retries:
                    logger.error(f'Error messaging bot: {e}. Trying again for the {tried} time.')
                else:
                    response = {'text': '', 'sources': ''}
                    break
        return response

    async def create_bot(self, cookies=None):
        if cookies is None:
            cookies = self.select_cookie()
            bot = await Chatbot.create(cookies=cookies)
        else:
            bot = await Chatbot.create(cookies=cookies)
        selected_cookies_idx = [idx for idx, c in self.cookies.items() if c['cookies'] == cookies][0]
        return bot, selected_cookies_idx

    # Image generation portion

    async def create_images_with_browser(self, prompt, timeout=20):
        logger.debug(f'Starting to generate images...')
        url = "https://www.bing.com/images/create/"
        prompt = prompt.strip("\n")
        self.driver.get(url)

        # Getting search bar and generating images
        time.sleep(4)
        ini = time.time()
        while True:
            logger.debug(f'Writing to search bar...')
            search_bar = self.driver.find_elements(By.XPATH, '//div[contains(@class, "b_searchboxForm")]')
            try:
                search_bar[0].find_element(By.TAG_NAME, 'input').send_keys(f'{prompt}', Keys.ENTER)
            except:
                pass
            time.sleep(2)
            if time.time() - ini > timeout:
                raise
            if self.driver.current_url != url:
                break
        # Searching images generated in page
        logger.debug(f'Waiting for images generation...')
        time.sleep(30)
        try:
            div_element = self.driver.find_elements(By.ID, "mmComponent_images_as_1")
        except:
            logger.debug('Waiting 60 more seconds before trying again to generate images')
            time.sleep(60)
            div_element = self.driver.find_elements(By.ID, "mmComponent_images_as_1")
        if len(div_element) == 0:
            logger.debug('Waiting 60 more seconds before trying again to generate images')
            time.sleep(60)
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

    def _create_thumbnail(self, image_path):
        image = cv2.imread(image_path)
        thumbnail_dim = (100, 100)
        thumbnail = cv2.resize(image, thumbnail_dim, interpolation=cv2.INTER_AREA)
        thumbnail_path = image_path.replace('.jpeg', '_thumbnail.jpeg')
        cv2.imwrite(thumbnail_path, thumbnail, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        return thumbnail_path

    async def generate_images(self, prompt, return_method = 'google_drive_upload', retries = 5, gdrive_folder = 'media_news', filename_prefix = ''):
        tried = 1
        created = True
        while True:
            try:
                await self.create_images_with_browser(prompt)
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
            google_drive_thumbnail_link_list = []
            for image_file in os.listdir(os.path.join(script_dir, 'images_generated')):
                if not image_file.endswith('.jpeg'):
                    continue
                image_path = os.path.join(script_dir, 'images_generated', image_file)
                thumbnail_path = self._create_thumbnail(image_path)
                link = self.gd.upload_file(image_path, str(datetime.date.today())+f'__{filename_prefix}__'+f'_{image_file}', gdrive_path=gdrive_folder)
                thumbnail_link = self.gd.upload_file(thumbnail_path, str(datetime.date.today())+f'__{filename_prefix}__'+f'_{image_file.replace(".jpeg","_thumbnail.jpeg")}', gdrive_path=gdrive_folder)
                os.remove(image_path)
                os.remove(thumbnail_path)
                google_drive_link_list.append(link)
                google_drive_thumbnail_link_list.append(thumbnail_link)
            return google_drive_link_list, google_drive_thumbnail_link_list
        elif return_method == 'return_image_paths':
            return list(os.listdir(os.path.join(script_dir, 'images_generated')))

    # News generation portion
    async def generate_news_for_today(self):
        if datetime.datetime.now().hour < 10:
            today = datetime.date.today() - datetime.timedelta(days=1)
        else:
            today = datetime.date.today()
        day_str = today.strftime('%d/%m/%Y')
        logger.info(f'Generating news summary for today ({today})...')
        news = []
        for region_dict in self.regions:
            region_name = region_dict['cidade']
            news_summary = {'text': 'THROTTLED'}
            cookie_idx = None
            while 'THROTTLED' in news_summary['text']:
                if cookie_idx is not None:
                    self.cookies[cookie_idx]['usage_count'] += 10
                bot, cookie_idx = await self.create_bot()
                logger.debug(f'Generating news summary for region {region_name}')

                # News Summary prompt
                with open(os.path.join(script_dir, 'prompts', self.config['news_summary_prompt']['file']), 'r', encoding='utf-8') as f:
                    news_prompt_text = f.read()
                news_prompt = news_prompt_text.format(date_str = day_str+' e até 3 dias anteriores (se houver) ', region = region_name)
                news_summary = await self.message_existing_bot(bot, news_prompt)

            if 'NÃO ACHEI' in news_summary['text'] or "NÃO ACHEI." in news_summary['text']:
                news_summary = await self.message_existing_bot(bot, 'Por favor, tente novamente, em sites de notícias mais regionais, como jornais do estado ou até mesmo da cidade. Tente também nos outros sites que listei para você, não esqueça de nenhum. Caso realmente não encontre nada, responda novamente com "NÃO ACHEI"')
                logger.debug(news_summary['sources'])
                logger.warning(f'No news was found for region {region_name} and date {day_str}, trying again.')
                if 'NÃO ACHEI' in news_summary['text'] or "NÃO ACHEI." in news_summary['text']:
                    logger.warning(f'No news was found for region {region_name} and date {day_str}')
                    logger.debug(news_summary['sources'])
                    await bot.close()
                    continue

            news_text = news_summary['text']
            news_sources = news_summary['sources']
            while 'AINDA NÃO TERMINEI' in news_summary['text']:
                news_summary = await self.message_existing_bot(bot, 'Ok. Me dê o resto das notícias, lembre-se de seguir as instruções corretamente.')
                news_text = news_text+news_summary['text']
                news_sources = news_sources+news_summary['sources']

            # News text
            text_prompt = open(os.path.join(script_dir, 'prompts', self.config['news_text_prompt']['file'])).read()
            news_text_response = await self.message_existing_bot(bot, text_prompt)
            news_text_response = news_text_response['text']
            logger.debug("News text generated:" + news_text_response)
            parsed_success, parsed_news_text = self.parse_news_text(news_text_response)
            logger.debug("News text parsed:" + str(parsed_news_text))
            if not parsed_news_text['news_found'] or not parsed_success:
                logger.warning(f'No news was found for region {region_name} and date {day_str}')
                await bot.close()
                continue

            # Headline
            headline_prompt = open(os.path.join(script_dir, 'prompts', self.config['news_headline_generation_prompt']['file'])).read()
            news_headline = await self.message_existing_bot(bot, headline_prompt)
            headline = news_headline['text']

            # Image generation prompt
            image_generation_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['image_prompt_generation_prompt']['file'])).read()
            image_prompt = await self.parse_prompt_from_response(await self.message_existing_bot(bot, image_generation_prompt_text))
            images_links, thumbnail_links = await self.generate_images(image_prompt, filename_prefix=region_name)
            news.append({
                'day_str': day_str,
                'headline': headline,
                'region': region_name,
                'news': parsed_news_text['news_text'],
                'news_response': news_text,
                'news_source': news_sources,
                'news_links': parsed_news_text['news_sources'],
                'image_prompt': image_prompt,
                'images': images_links,
                'thumbnails': thumbnail_links
            })
            await bot.close()
        if os.path.exists(os.path.join(script_dir, 'news_data', 'media_news.json')):
            with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
                self.news_data = json.load(f)
        self.news_data.extend(news)
        with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'w', encoding='utf-8') as f:
            json.dump(self.news_data, f, indent=4)
        self.gd.upload_file(os.path.join(script_dir, 'news_data', 'media_news.json'), f'media_news_{datetime.datetime.now()}.json', 'news_data')
        return news

    # News generation portion
    async def generate_news_for_date(self, day_str):
        logger.info(f'Generating news summary for {day_str}...')
        news = []
        for region_dict in self.regions:
            region_name = region_dict['cidade']
            news_summary = {'text': 'THROTTLED'}
            cookie_idx = None
            while 'THROTTLED' in news_summary['text']:
                if cookie_idx is not None:
                    self.cookies[cookie_idx]['usage_count'] += 10
                bot, cookie_idx = await self.create_bot()
                logger.debug(f'Generating news summary for region {region_name}')

                # News Summary prompt
                with open(os.path.join(script_dir, 'prompts', self.config['news_summary_prompt']['file']), 'r', encoding='utf-8') as f:
                    news_prompt_text = f.read()
                news_prompt = news_prompt_text.format(date_str = day_str, region = region_name)
                news_summary = await self.message_existing_bot(bot, news_prompt)

            if 'NÃO ACHEI' in news_summary['text'] or "NÃO ACHEI." in news_summary['text']:
                news_summary = await self.message_existing_bot(bot, 'Por favor, tente novamente, em sites de notícias mais regionais, como jornais do estado ou até mesmo da cidade. Tente também nos outros sites que listei para você, não esqueça de nenhum. Caso realmente não encontre nada, responda novamente com "NÃO ACHEI"')
                logger.debug(news_summary['sources'])
                logger.warning(f'No news was found for region {region_name} and date {day_str}, trying again.')
                if 'NÃO ACHEI' in news_summary['text'] or "NÃO ACHEI." in news_summary['text']:
                    logger.warning(f'No news was found for region {region_name} and date {day_str}')
                    logger.debug(news_summary['sources'])
                    await bot.close()
                    continue

            news_text = news_summary['text']
            news_sources = news_summary['sources']
            while 'AINDA NÃO TERMINEI' in news_summary['text']:
                news_summary = await self.message_existing_bot(bot, 'Ok. Me dê o resto das notícias, lembre-se de seguir as instruções corretamente.')
                news_text = news_text+news_summary['text']
                news_sources = news_sources+news_summary['sources']

            # News text
            text_prompt = open(os.path.join(script_dir, 'prompts', self.config['news_text_prompt']['file'])).read()
            news_text_response = await self.message_existing_bot(bot, text_prompt)
            news_text_response = news_text_response['text']
            logger.debug("News text generated:" + news_text_response)
            parsed_success, parsed_news_text = self.parse_news_text(news_text_response)
            logger.debug("News text parsed:" + str(parsed_news_text))
            if not parsed_news_text['news_found'] or not parsed_success:
                logger.warning(f'No news was found for region {region_name} and date {day_str}')
                await bot.close()
                continue

            # Headline
            headline_prompt = open(os.path.join(script_dir, 'prompts', self.config['news_headline_generation_prompt']['file'])).read()
            news_headline = await self.message_existing_bot(bot, headline_prompt)
            headline = news_headline['text']

            # Image generation prompt
            image_generation_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['image_prompt_generation_prompt']['file'])).read()
            image_prompt = await self.parse_prompt_from_response(await self.message_existing_bot(bot, image_generation_prompt_text))
            images_links, thumbnail_links = await self.generate_images(image_prompt, filename_prefix=region_name)
            news.append({
                'day_str': day_str,
                'headline': headline,
                'region': region_name,
                'news': parsed_news_text['news_text'],
                'news_response': news_text,
                'news_source': news_sources,
                'news_links': parsed_news_text['news_sources'],
                'image_prompt': image_prompt,
                'images': images_links,
                'thumbnails': thumbnail_links
            })
            await bot.close()
        if os.path.exists(os.path.join(script_dir, 'news_data', 'media_news.json')):
            with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
                self.news_data = json.load(f)
        self.news_data.extend(news)
        with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'w', encoding='utf-8') as f:
            json.dump(self.news_data, f, indent=4, ensure_ascii=False)
        self.gd.upload_file(os.path.join(script_dir, 'news_data', 'media_news.json'), f'media_news_{datetime.datetime.now()}.json', 'news_data')
        return news

    # News generation portion
    async def generate_news_for_user(self, user_name, user_region, user_microregion, user_history):
        today = datetime.date.today()
        logger.info(f'Generating user news prompt for date {today}. User region: {user_region}')
        news_summary = {'text': 'THROTTLED'}
        cookie_idx = None
        while 'THROTTLED' in news_summary['text']:
            if cookie_idx is not None:
                self.cookies[cookie_idx]['usage_count'] += 10
            bot, cookie_idx = await self.create_bot()

            # News summary
            news_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['user_news']['file'])).read()
            news_prompt = news_prompt_text.format(user_name=user_name, user_region=user_region, user_microregion=user_microregion, user_history=user_history)
            news_summary = await self.message_existing_bot(bot, news_prompt)
        logger.debug(news_summary['text'])

        logger.info(f'Generating user news headline {today}. User region: {user_region}')
        # Headline
        headline_prompt = open(os.path.join(script_dir, 'prompts', self.config['user_headline_generation_prompt']['file'])).read()
        news_headline = await self.message_existing_bot(bot, headline_prompt)
        headline = news_headline['text']

        logger.info(f'Generating user news image prompt {today}. User region: {user_region}')
        # Image generation
        image_generation_prompt_text = open(os.path.join(script_dir, 'prompts', self.config['user_image_generation_prompt']['file'])).read()
        image_prompt = await self.parse_prompt_from_response(await self.message_existing_bot(bot, image_generation_prompt_text))
        images_links, thumbnail_links = await self.generate_images(image_prompt, filename_prefix=f"{user_name}&&{user_region}&&{user_microregion}", gdrive_folder='user_news')

        if os.path.exists(os.path.join(script_dir, 'news_data', 'user_news.json')):
            with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'r', encoding='utf-8') as f:
                self.users_news = json.load(f)

        news_info = {
            'day_str': today.strftime('%d/%m/%Y'),
            'headline': headline,
            'user_name': user_name,
            'user_region': user_region,
            'user_microregion': user_microregion,
            'user_history': user_history,
            'images': images_links,
            'thumbnails': thumbnail_links
        }
        self.users_news.append(news_info)
        await bot.close()
        with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'w', encoding='utf-8') as f:
            json.dump(self.users_news, f, indent=4, ensure_ascii=False)
        self.gd.upload_file(os.path.join(script_dir, 'news_data', 'user_news.json'), f'user_news_{datetime.datetime.now()}.json', 'news_data')
        return news_info

    # News get portion
    async def get_news_for_today(self):
        today = datetime.date.today()-datetime.timedelta(days=1)
        today_str = today.strftime("%d/%m/%Y")
        today_news = [n for n in self.news_data if n['day_str'] == today_str]
        return today_news

    async def get_news_for_date(self, day_str):
        news = [n for n in self.news_data if n['day_str'] == day_str]
        return news

    async def get_all_media_news(self):
        return self.media_news

    async def get_user_news_for_today(self):
        today = datetime.date.today()-datetime.timedelta(days=1)
        today_str = today.strftime("%d/%m/%Y")
        today_news = [n for n in self.users_news if n['day_str'] == today_str]
        return today_news

    async def get_user_news_for_date(self, day_str):
        news = [n for n in self.users_news if n['day_str'] == day_str]
        return news

    async def get_all_user_news(self):
        return self.users_news


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
    
    def parse_news_text(self, response):
        news_text = response.split('{')[-1].split('}')[0]
        try:
            final_dict = eval('{'+news_text.replace('\n', '')+'}')
        except:
            logger.warning(f'Error parsing news text')
            return False, {
                'news_found':False,
                'news_text':[],
                'news_sources':[],
            }

        return True, final_dict
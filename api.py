from loguru import logger
import asyncio
from pathlib import Path
import datetime
import pytz
import json

# Find this script directory
script_dir = Path( __file__ ).parent.absolute()

# FastAPI related modules

from fastapi import FastAPI, Query
from uvicorn import Config, Server
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from fastapi.responses import HTMLResponse, JSONResponse

origins = [
    "*",
    "http://127.0.0.1",
    "http://localhost"
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]
app = FastAPI(middleware=middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------
@app.get('/generate_image')
async def generate_image(prompt: str = Query(..., description='Generate an image based on your prompt.')):
    global g3
    try:
        r = await g3.generate_images(prompt)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/generate_news_for_today')
async def generate_news_for_today():
    global g3
    try:
        r = await g3.generate_news_for_today()
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/generate_news_for_date')
async def generate_news_for_date(day_str: str):
    global g3
    try:
        r = await g3.generate_news_for_date(day_str)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/generate_user_news')
async def generate_user_news(user_name:str, user_region:str, user_microregion:str, user_history:str):
    global g3
    # try:
    #     r = await g3.generate_news_for_user(user_name, user_region, user_microregion, user_history)
    # except Exception as e:
    #     logger.error(e)
    #     r = {'error':True}
    # headers = {'Content-Type': 'application/json; charset=utf-8'}
    with open('./news_request/user_news_requests.json', 'r') as f:
        requests = json.load(f)
    requests.append({
        'user_name': user_name,
        'user_region': user_region,
        'user_microregion': user_microregion,
        'user_history': user_history
    })
    with open('./news_request/user_news_requests.json', 'w') as f:
        json.dump(requests, f)
    return 200

# --------- GET ROUTES
@app.get('/get_all_news')
async def get_all_news(news_number = None):
    global g3
    try:
        r = g3.news_data
        if news_number is not None:
            if len(r) > int(news_number):
                r = r[-int(news_number):]
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_news_for_today')
async def get_news_for_today():
    global g3
    try:
        r = await g3.get_news_for_today()
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_news_for_date')
async def get_news_for_date(day_str: str):
    global g3
    try:
        r = await g3.get_news_for_date(day_str)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_user_news_for_today')
async def get_user_news_for_today():
    global g3
    try:
        r = await g3.get_user_news_for_today()
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_user_news_for_date')
async def get_user_news_for_date(day_str: str):
    global g3
    try:
        r = await g3.get_user_news_for_date(day_str)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_all_user_news')
async def get_all_user_news():
    global g3
    try:
        r = await g3.get_all_user_news()
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_news_html')
async def get_news_html():
    global g3
    try:
        r = await g3.generate_news_for_today()
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    html = '''<div style="font-family: Arial, sans-serif;">'''
    for news_item in r:
        region = news_item['region']
        news_text = news_item['news']
        html += f'''<h2>{region}</h2>'''
        html += f'''<p>{news_text}</p>'''
        for image_link in news_item['images']:
            html += f'''<img src="{image_link}" alt="Image for {region}" style="max-width: 100%; height: auto;"><br>'''
    html += '''</div>'''
    return HTMLResponse(html)

@app.get('/list_googledrive_files')
async def list_googledrive_files():
    global g3
    files = g3.gd.list_files()
    return files

async def call_generations():
    tz = pytz.timezone('America/Sao_Paulo')
    news_generation_datetime = datetime.time(5,15,0,0,tz)
    try:
        with open('./news_request/user_news_requests.json', 'r') as f:
            requests = json.load(f)
    except Exception as e:
        logger.warning(f'Error opening user_news_requests.json. This is normal if it is the first time running the API, but otherwise this is a problem.')
        logger.error(e)
        with open('./news_request/user_news_requests.json', 'w') as f:
            json.dump([], f)
    while True:
        now = datetime.datetime.now(tz=tz)
        if now.hour == 5:
            if abs((now - datetime.datetime.combine(datetime.date.today(), news_generation_datetime)).total_seconds()) < 15:
                logger.info("Starting to generate news for today!")
                try:
                    response = await generate_news_for_today()
                    logger.success(f'Successfully generated today news!')
                    logger.debug(response)
                except Exception as e:
                    logger.error(f'Error generating today news.')
                    logger.error(e)
            else:
                print(abs((now - datetime.datetime.combine(datetime.date.today(), news_generation_datetime)).total_seconds()), end='\r')
        else:
            with open('./news_request/user_news_requests.json', 'r') as f:
                requests = json.load(f)
            if len(requests) > 0:
                current_request = requests.pop(0)
                with open('./news_request/user_news_requests.json', 'w') as f:
                    json.dump(requests, f)
                logger.info(f'Generating news for request {current_request}')
                try:
                    response = await generate_user_news(user_name = requests['user_name'], user_region = requests['user_region'], user_microregion = requests['user_microregion'], user_history = requests['user_history'])
                    logger.success(f'Successfully generated image for user news!')
                    logger.debug(response)
                except Exception as e:
                    logger.error(f'Error generating image for user news {current_request}.')
                    logger.error(e)
        await asyncio.sleep(1)



if __name__ == "__main__":
    # uvicorn.run(app='api:app', host="0.0.0.0", port=7777, reload=False)
    import bot
    g3 = bot.G3Bot()
    loop = asyncio.new_event_loop()
    config = Config(app=app, loop=loop, host="0.0.0.0", port=7777, reload=False)
    server = Server(config)
    loop.create_task(call_generations())
    loop.run_until_complete(server.serve())
else:
    # Bot related modules
    import bot
    g3 = bot.G3Bot()
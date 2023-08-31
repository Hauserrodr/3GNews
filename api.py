from loguru import logger
import asyncio
import os
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
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

origins = [
    "*",
    "http://127.0.0.1",
    "http://localhost"
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]
app = FastAPI(middleware=middleware)
app.mount("/home", StaticFiles(directory=os.path.join(script_dir, "frontend/dist")), name="home")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------

@app.get("/")
async def root():
    return FileResponse("frontend/dist/index.html")

@app.get('/generate_user_news')
async def generate_user_news(user_name:str, user_region:str, user_microregion:str, user_history:str):
    global g3
    with open('./news_request/user_news_requests.json', 'r', encoding='utf-8') as f:
        user_requests = json.load(f)
    user_requests.append({
        'user_name': user_name,
        'user_region': user_region,
        'user_microregion': user_microregion,
        'user_history': user_history
    })
    with open('./news_request/user_news_requests.json', 'w', encoding='utf-8') as f:
        json.dump(user_requests, f)
    return 200

# --------- GET ROUTES
@app.get('/get_all_news')
async def get_all_news(news_number = None):
    try:
        with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
            r = json.load(f)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_news_for_today')
async def get_news_for_today():
    day_str = datetime.date.today()-datetime.timedelta(days=1)
    day_str = day_str.strftime('%d/%m/%Y')
    try:
        with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
            media_news = json.load(f)
            r = [n for n in media_news if n['day_str'] == day_str]
    except Exception as e:
        logger.error(e)
        r = {'error':True}

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_news_for_date')
async def get_news_for_date(day_str: str):
    try:
        with open(os.path.join(script_dir, 'news_data', 'media_news.json'), 'r', encoding='utf-8') as f:
            media_news = json.load(f)
            r = [n for n in media_news if n['day_str'] == day_str]
    except Exception as e:
        logger.error(e)
        r = {'error':True}

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_user_news_for_today')
async def get_user_news_for_today():
    day_str = datetime.date.today()-datetime.timedelta(days=1)
    day_str = day_str.strftime('%d/%m/%Y')
    try:
        with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'r', encoding='utf-8') as f:
            users_news = json.load(f)
            r = [n for n in users_news if n['day_str'] == day_str]
    except Exception as e:
        logger.error(e)
        r = {'error':True}

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_user_news_for_date')
async def get_user_news_for_date(day_str: str):
    try:
        with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'r', encoding='utf-8') as f:
            users_news = json.load(f)
            r = [n for n in users_news if n['day_str'] == day_str]
    except Exception as e:
        logger.error(e)
        r = {'error':True}

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

@app.get('/get_all_user_news')
async def get_all_user_news():
    try:
        with open(os.path.join(script_dir, 'news_data', 'user_news.json'), 'r', encoding='utf-8') as f:
            r = json.load(f)
    except Exception as e:
        logger.error(e)
        r = {'error':True}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return JSONResponse(content=r, headers=headers)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    config = Config(app=app, loop=loop, host="0.0.0.0", port=7777, reload=False)
    server = Server(config)
    loop.run_until_complete(server.serve())
from loguru import logger
import asyncio
from pathlib import Path

# Find this script directory
script_dir = Path( __file__ ).parent.absolute()

# Bot related modules
import bot
g3 = bot.G3Bot()

# FastAPI related modules

from fastapi import FastAPI, Query
from uvicorn import Config, Server
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from fastapi.responses import HTMLResponse

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
    r = await g3.generate_images(prompt)
    return r

@app.get('/generate_news_for_today')
async def generate_news_for_today():
    global g3
    r = await g3.get_news_for_today()
    return r

@app.get('/get_news_html')
async def get_news_html():
    global g3
    r = await g3.get_news_for_today()
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

if __name__ == "__main__":
    uvicorn.run(app='api:app', host="0.0.0.0", port=7777, reload=False)
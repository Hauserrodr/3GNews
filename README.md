# Project: AI-Generated Images and News for Rio Grande do Sul

This project is designed to generate images and news for specific locations in the state of Rio Grande do Sul, Brazil. It uses FastAPI to create an API that serves endpoints for generating images based on prompts, fetching the news for today, rendering HTML with news details, and listing Google Drive files.
The purpose of the project is to make a comparison, using an artistic approach, of the news generated by the media and the daily reports from the website users slice of life of each location.

## Features
- **Image Generation**: Generates images based on a provided prompt.
- **News Generation**: Retrieves and generates news for specific locations within the state.
- **Google Drive Integration**: Lists files from Google Drive.

## Endpoints
- `/generate_image`: Generate an image based on the given prompt.
- `/generate_news_for_today`: Generate news for today's date.
- `/get_news_html`: Retrieve the news and render it as HTML content.
- `/list_googledrive_files`: List files from Google Drive.

## Getting Started

### Prerequisites
- Python >= 3.9
- FastAPI
- Uvicorn
- Loguru

### Installation
```bash
git clone https://github.com/Hauserrodr/3GNews-Bot.git
cd 3GNews-Bot
pip install -r requirements.txt
msedge.exe --remote-debugging-port 9999
python api.py
```

### TODO
- Implement user image generation
    Basically this feature allows users to generate images based on the daily stories they provide. The story is used for generating an image prompt, which is then feeded into DALL-E2 API (via Bing) to generate 4 images about the user narrative. >>> DONE
- Implement daily news retrieve endpoint
    Since it's the backend job to create the daily news every day at 6AM, we should have a route to just retrieve the images from google drive instead of generating them everything  the endpoint is accessed. >>> DONE
- Improve news generation pipeline
    - Use the LLM to double check if the message really has news.
    - Make sure the news does not have an introduction message, like "Here are the news for...".
    - Make sure the image generation prompt really is a prompt.
    - MAYBE: Check the link of every news returned and ask questions to double check if the news are really from today and really from the region asked.
    - MAYBE: Ask for more news
- Improve prompt generation message
    The prompts are too descriptive right now, maybe a way to improve is to give more examples.
- Implement user news retrieve endpoint
    We should have this endpoint for retrieving every user's daily news stories from Google Drive. >>> DONE
- Save data about the news locally (or at least the url for the google drive archive)
    We should save data about when the news was generated, the users news, etc. >>> DONE


EXTRAS
- Get current reward counter in the bing website
- Implement profile change in google chrome
- Start chrome with debugging port from script
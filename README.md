# README

## Description
This script automates the login process to a certain website equipped with an “anti-captcha” system.  
It uses the `requests` library to perform HTTP requests, the `beautifulsoup4` library to extract the security question, and the OpenAI API (through the `openai` library) to generate the answer, which is then sent back to the server for successful authentication.

## Requirements
- Python 3.7+ (recommended 3.9+)
- Installed libraries listed in `requirements.txt` (e.g., `requests`, `beautifulsoup4`, `python-dotenv`, `openai`)
- An OpenAI account (API Key) to use the GPT model

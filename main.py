import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
def get_webpage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    return None

def find_question(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    question = soup.find(id='human-question')
    
    if question:
        return question.text.strip()
    print(soup)
    return None

def main():
    url = os.getenv('URL')
    
    html_content = get_webpage(url)
    
    if html_content:
        question = find_question(html_content)
        if question:
            print(question)
        else:
            print("Nie udało się znaleźć pytania.")

if __name__ == "__main__":
    main()
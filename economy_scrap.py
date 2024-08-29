import requests
from bs4 import BeautifulSoup
import json

def scrape_news(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_items = []
    for item in soup.select('.gc__title a'):
        title = item.text.strip()
        link = 'https://www.aljazeera.com' + item['href']
        news_items.append({'title': title, 'link': link})
    
    return news_items

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = "https://www.aljazeera.com/economy/"
    news_items = scrape_news(url)
    
    save_to_json(news_items, 'economy.json')
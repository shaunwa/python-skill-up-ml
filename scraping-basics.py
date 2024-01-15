import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')

articles = []

for item in soup.find_all('tr', class_='athing'):
    title_tag = item.find('span', class_='titleline').find('a')
    title = title_tag.text
    link = title_tag.get('href', 'N/A')
    new_article = {
        'title': title,
        'link': link,
    }
    articles.append(new_article)

for index, item in enumerate(soup.find_all('span', class_='score')):
    articles[index]['upvotes'] = item.text

print(articles)
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')

books = []

for item in soup.find_all('article', class_='product_pod'):
    title = item.find('h3').find('a').text
    price = item.find('p', class_='price_color').text
    star_rating_tag = item.find('p', class_='star-rating')
    rating = star_rating_tag.get('class')[1]

    books.append({
        'title': title,
        'price': price,
        'rating': rating,
    })

print(books)
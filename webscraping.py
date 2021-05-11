import requests
page = requests.get('https://dataquestio.github.io/web-scraping-pages/simple.html')

print(page.content)


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
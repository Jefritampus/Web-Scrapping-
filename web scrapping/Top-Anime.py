from bs4 import BeautifulSoup
import request

url = 'https://myanimelist.net/topanime.php'
url

page = request.get(url)
page

soup = BeautifulSoup(page.content, 'html')
soup

print(soup.prettify())

soup.title
soup.a
soup.p
soup.h1

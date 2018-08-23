import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/hpe/analystestimates"
r = requests.get(url)
soup = BeautifulSoup(r.content)
print(soup.title)
stock_value = soup.find_all('a',attrs={"class":"list__item"})
#stock_value = soup.find('a', {"class":"list_item"})
print(stock_value)
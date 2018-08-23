import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/sq/analystestimates"
r = requests.get(url)
soup = BeautifulSoup(r.content)


def marketWatchAnalystRating(soup):
    data = []
    print(soup.title)
    table = soup.find('table', attrs={'class': 'ratings'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        data.append(cols[0].text.strip() + " " + cols[1].text.strip())

    print("##",data)

def yahooStatisticsData(soup):




#marketWatchAnalystRating(soup)


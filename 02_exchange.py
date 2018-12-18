import requests
from bs4 import BeautifulSoup

url = 'http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum'
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

exchns = soup.select('#asiaBody > table > tbody tr')
for exchn in exchns:
    name = exchn.select_one('td.name')
    ex = exchn.select_one('td.idx')
    print(name.text + "  " + ex.text + "원")

exchns = soup.select('#europeBody > table > tbody tr')
for exchn in exchns:
    name = exchn.select_one('td.name')
    ex = exchn.select_one('td.idx')
    print(name.text + "  " + ex.text)

exchns = soup.select('#mideastBody > table > tbody tr')
for exchn in exchns:
    name = exchn.select_one('td.name')
    ex = exchn.select_one('td.idx')
    print(name.text + "   " + ex.text)

exchns = soup.select('#africaBody > table > tbody tr')
for exchn in exchns:
    name = exchn.select_one('td.name')
    ex = exchn.select_one('td.idx')
    print(name.text + "  " + ex.text)

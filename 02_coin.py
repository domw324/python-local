import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser') # 응답이 들어온 res에서 html문서로 변경

coins = soup.select('tbody.coin_list tr')
for coin in coins:
    print(coin.select_one("td:nth-of-type(1) a strong").text)
    print(coin.select_one("td:nth-of-type(2) strong").text)
    print("- - - - - - - - - -")
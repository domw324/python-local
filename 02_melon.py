import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

music_table = soup.select('table tr.lst50')
for mt in music_table:
    rank = mt.select_one("span.rank").text
    song = mt.select_one("div.rank01 a").text
    name = mt.select_one("div.rank02 a").text
    print(rank + "\t" + name + " - " + song)
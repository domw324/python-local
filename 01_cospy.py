import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
r = requests.get(url).text
# python이 보기 편한 형식으로 변환
soup = BeautifulSoup(r, 'html.parser')
select = soup.select_one("#KOSPI_now")
print(select.text)
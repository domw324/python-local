# SSAFY - DAY 02

## Python 심화

### Git Bash를 써보자.

- 명령어
  - cd 디렉토리명 : 디렉토리 이동
  - mkdir 디렉토리명 : 디렉토리 생성
  - touch 파일명.확장자 : 파일 생성
  - pip install 모듈명 : 모듈 설치 // ex) pip install requests
  - python 파일명.py : 파이썬으로 실행
  - 



### 웹브라우저

- import webbrowser
  - <u>http:// ~ ?</u> 까지는 웹페이지의 도메인.
  - ? 뒤 부터는 옵션.
  - 특히 <u>q="~"</u> 부분은 검색어 부분이 됨.

```python
import webbrowser

q_list = ["bts", "아이유", "블랙핑크", "송민호"]

url = "https://www.google.com/search?q="

for q in q_list:
    webbrowser.open(url + q)
#webbrowser.open_new(url)
```

### 웹 크롤링 실습 - 실시간 검색어

- <u>zzul.li</u> 사이트 애용하세요~ : url 줄이기!
- requests module
  - requests.get('주소') : 정보 요청 , 객체 자체가 return
  - requests.get('주소').status_code : 상태 주소, 상태만 return
- BeautiflSoup module : 받은 문서를 보기 좋게 만든다.
  - pip install bs4 설치한 후에 from bs4 import BeautifulSoup 로 import
  - BeautifulSoup(res, <u>'html.parser'</u>) 정보 불러온다.
  - nth-child()는 bs4에서 지원하지 않음. nth-of-type로 변경
    li:nth-child(~) >> li:nth-of-type(~) // div:nth-child(~) >> li:nth-of-type(~)
  - .select_one(selector) : 문서안에 있는 특정 내용을 하나만 뽑는다.
  - .select(selector) : 문서안에 있는 모든 내용을 뽑아낸다.
  - li:nth-child()에서 li만 남겨놓으면 1위 부터 10위에 해당되는 내용 모두 가져오게 된다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net"
res = requests.get(url).text
#res = requests.get(url).status_code

soup = BeautifulSoup(res, 'html.parser')
pick = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-of-type(1) > div > div:nth-of-type(1) > span.txt_issue > a')
print(pick)
```

### 웹 크롤링 실습2  - 비트코인

- 규칙을 가지고 크롤링
  - soup.select()에서 <u>coin_list</u>가 유일한 클래스명이기 때문에 바로 써도 된다!
  - 원하는 요소만 뽑을 때는 한 칸 띄고 쓰면 된다 // ex) tbody.coin_list <u>tr</u>

```python
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
```

### 웹 크롤링 실습3 - 환율

```python
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

```

### 웹 크롤링 실습4 - 멜론 Top50

- 멜론은 자체적으로 헤더부분이 비어 있으면 권한을 주지 않는다.
  - headers = {~}부분을 통해 헤더 부분에 정보를 넣어 준 후 크롤링 한다.

```python
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
```

### 파일 이름 바꾸기 - OS

- import os를 통해 조작

- 파일 이름 바꾸기 - 글자 수 세기

  - 리눅스에서는 현재 폴더를 "." 로 한다.

  - ```:do_not_litter:
    import os
    
    os.chdir(r'C:\Users\student\SSJ\SSAFY지원자')
    
    for filename in os.listdir("."):
        os.rename(filename, "SAMSUNG_" + filename)
    ```

- 파일 이름 바꾸기2 - replace 사용

  - ```:do_not_litter:
    import os
    
    os.chdir(r'C:\Users\student\SSJ\SSAFY지원자')
    
    for filename in os.listdir("."):
        newname = filename.replace('APPLE', 'SSAFY')
        os.rename(filename, newname)
    ```

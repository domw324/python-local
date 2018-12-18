import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))
if (150 < dust):
  print("매우나쁨!! 마스크 꼭 쓰세요!!")
elif (80 < dust <= 150):
  print("나쁨!! 알아서 쓰세요!!")
elif (30 < dust <= 80):
  print("보통")
else:
  print("좋음~ ^_^")
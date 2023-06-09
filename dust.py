import requests
import random
from decouple import config

# KEY = config('KEY')
# URL = f'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey{KEY}=&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

# res = requests.get(URL)
# data = res.json()
# dust = data['response']['body']['items'][13]['pm10Value'] 

dust = random.randint(1, 200)

# 1~50 좋음
# 51~100 보통
# 101~150 나쁨
# 151~200 매우나쁨

# 내코드
if dust < 51:
    print(dust, '좋음')
elif dust < 101:
    print(dust, '보통')
elif dust < 151:
    print(dust, '나쁨')
else :
    print(dust, '매우나쁨')

# 강의코드
print(dust)
if dust >= 1 and dust <= 50:
    print('좋음')
# and를 씀
elif  51 <= dust <= 100:
    print('보통')
# 조건 사이에 dust 를 끼워넣음
elif 101 <= dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')

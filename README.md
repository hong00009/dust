# 3일차
## 1. `.gitignore` 파일과 `.env` 파일
github에 공개되어서는 안되는 중요한 정보들은 `.gitignore` 파일을 통해 설정할 수 있음 (이건 업로드하지말고 무시해라)

gitignore.io 사이트에서 미리 설정된 양식을 구해와서 `.gitignore`파일을 만들어 설정해놓으면 됨

많은 예외 항목이 있으나, 각종 환경변수들을 저장해놓고 쓰는 `.env` 파일을 만들었고 

공공데이터 API를 활용할 때 사용하는 KEY값은 그곳에 저장함 
(키는 api사이트에서 나에게 할당해준 고유번호)

----

## 2. 간단히 훑어본 python 문법
- 변수 / 조건 / 반복

내가 알던 다른 프로그래밍언어랑 다르게 변수 핟당하고 사용하는게 너무 간단 간결함.. 세미콜론도 없고 int char 따위도 없다! 이외에 코드 짜는데 큰 무리는 없었음

변수 - 정수고 문자열이고 구별 없이 그냥 이름 만들자마자 곧장 쓰면된다 `a = 'cat', b = 13`
```python
dust_list = [10, 20, 20, 15, 100, 150]
# 대괄호 리스트, 0번째 1번째...로 불러와서 쓴다 / dust_list[0]

dust_dict = {
    '서울': 100, 
    '대전': 50,
    '부산': 10,
}
# 중괄호 딕셔너리, '서울', '대전'... 내가 지은 이름으로 불러와서 쓴다 / dust_dict['부산']
```
조건문 - 콜론이 있다
```python
if age > 20:
    print('어른')
else:
    print('아이')
```

반복문 - 이것도 콜론이 있다 / for문이 대격변해서 많이 낯설다. i가 없네.. 엄청 간단한데 좀더 써봐야 감을 잡을 듯
```python
menus = ['김밥', '라면', '만두']
```

```python
for menu in menus:
    print(menu)
# for문은 menus가 3개있으니까 자동으로 3번 돈다
```
몇개 있는건지 알고있어야 몇번도는지도 알 수 있다


```python
n = 0
while n < 2:
    print(menus[n])
    n = n + 1
# while문은 n이 2가 되기 전까지 - 0, 1 까지 총 2회만 돈다
```
반복문 돌릴일이 있다면 보통 전체 다 돌리지, 개수 하나하나 돌리지 않다보니 for문을 더 자주 쓴다

---
## 3. 함수
기본적으로 구비된 내장함수 `print()` , `max()` 등이 있고, 내장함수 말고도 이외에 다양한 함수를 불러와서 사용할 수 있다 (남들이 만들어놓은 함수)

- random 함수

random 중 다양한 기능을 . 점을 통해 골라서 쓸 수 있음

```python
import random
# random 함수를 사용하기 위해 import로 불러왔다
```
```python
random.randint(1, 11)
# 1이상 11미만 (1~10) 중에 랜덤한 숫자 뽑기
```
```python
menus = ['김밥', '라면', '만두']
random.choice(menus)
# 위 리스트 중에서 하나 뽑기
```
```python
numbers = range(1,46)
random.sample(numbers, 6)
# 1~45 중 무작위 6개 숫자 뽑기 / 로또추첨처럼 뽑은 숫자는 중복되지 않음
```
- requests 함수

위에서 랜덤 뽑기 하다보니 랜덤의 대명사, 로또의 실제 데이터를 가져와서 비교해보기로 함

```python
import requests
# 이 함수를 처음사용하는 경우에는 설치과정이 필요하다
#  pip install requests 
```

```python
URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1070'
# 실제 로또추첨 1070회 당첨번호 정보가 제공되는 주소

res = requests.get(URL)
data = res.json() 
# json 파일 형식으로 전환
```
data를 확인해보니'drwtNo1' ~ 'drwtNo6' 로 설정된 변수가 6개의 로또 추첨번호 
('bnusNo'는 보너스번호인데 복잡해지니 안쓴다)


```python
#중간생략
set(lotto_number) & set(my_number)    
# set 함수를 사용, 1070회 로또추첨번호를 집합형식으로 변환
# 내가 가진 로또 번호도 집합형식으로 변환
# & 기호로 두 집합간에 겹치는 부분을 구함 (교집합)
```

내 로또 번호 몇개가 일치했나 확인가능

---
## 4. BeautifulSoup 맛만 보기
사실 순서는 requests보다 이게 먼저였던것 같은데..? 적다보니 4번이 되었다
```python
import requests
from bs4 import BeautifulSoup
# pypi beautifulsoup 홈페이지를 먼저 확인하고 
# pip install beautifulsoup4 로 설치했다
```

네이버 증권 사이트에서 코스피 지수만을 떼어와 가져와보기.
```python
URL = 'https://finance.naver.com/sise/'
# 네이버증권>국내증시 탭. sise라고 명명한 것에 대한 감탄..

res = requests.get(URL)
data = BeautifulSoup(res.text, 'html.parser')
# text로 가져왔는데, BS가 이걸 예쁘게 파싱해줌
```

사이트에서 F12버튼을 눌러 개발자도구(DevTools) 실행

인스펙터 버튼으로 코스피 지수 표기된 숫자부분 클릭 
```javascript
<span id="KOSPI_now" class="num">2,641.16</span>
```
이부분으로 이동함

우클릭 > 복사 > selector 부분복사하면 `#KOSPI_now` 가 복사됨

```python
selector = '#KOSPI_now'
data.select_one(selector)
# 수많은 내용 중에 KOSPI_now 라는 id부분의 값만 선택하여 가져옴
```
num_list = [1, 2, 3, 4, 5]

max_num = max(num_list)

print(max_num)


####

import random
random_number = random.randint(1, 46)
print(random_number,'~~~')

####
# pip install requests 선행과정 필요
import requests

#####
menus = ['김밥', '라면', '만두']
menu = random.choice(menus)
#한가지 랜덤 추출
print(menu)

numbers = range(1,46)
lucky_list = random.sample(numbers, 6)
#비복원추출이라 중복되지 않은 값으로 각각 추출
print(lucky_list)

# 로또 5천원어치 구매 / while 문으로 구현
print('로또 자동 5천원어치 구매')
n = 0
while n < 5:
    my_num = random.sample(numbers, 6)
    print(my_num)
    n = n + 1

# for문으로 구현
print('\n로또 자동 5천원어치 재구매')
repeat = range(1, 6)  # 1~5번
for num in repeat:
    lotto_num = random.sample(numbers, 6)
    print(lotto_num)

print()
URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1070'

res = requests.get(URL)

data = res.json() # .text와는 다르게 json 형식으로 다듬어져 보임

# print(data['drwtNo1'])

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6] # 현재 1등 당첨번호

lucky_number = random.sample(  range(1,46) , 6  ) # 나의 랜덤추출번호 / 당첨번호와 몇개가 겹칠까?

print(lotto_number, lucky_number)

result = set(lotto_number) & set(lucky_number)    #set 함수를 사용 - 형변환 / &기호 = 겹치는 부분을 구해줘

print(result)

# 파이썬에서의 for문 형식이 너무 낯설어서 코드를 작성 시 바로 떠오르지가 않음...
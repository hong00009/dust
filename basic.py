# 주의사항
# 1. apple /  Apple 대소문자가 다르면 다른데이터
# 2. git add. / git add . 띄어쓰기가 다르면 다른것
# 3. message / massage 오타나 스펠링다르면 다른 데이터

# 변수, variable
dust = 10
greeting = 'hello'

# 1
status = True

# 0
status = False

print(dust, greeting, status)

dust_list = [10, 20, 20, 15, 100, 150]

print(dust_list[0])


dust_dict = {
    # : 콜론 입력시, 앞부분 key('서울')와 : 콜론 사이엔 띄어쓰기 없이 붙여씀
    '서울': 100, 
    '대전': 50,
    '부산': 10,
}

print(dust_dict['서울'])


# 조건
age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다')
else:
    print('어린이입니다')

# 반복
menus = ['짜장면', '국밥', '김밥', '라면', '피자']

n = 0
while n < 2:
    print(menus[n])
    n = n + 1

print()
for menu in menus:
    print(menu)

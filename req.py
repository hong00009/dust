import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'

res = requests.get(URL)

data = BeautifulSoup(res.text, 'html.parser')

selector = '#KOSPI_now'
kospi = data.select_one(selector)

print(kospi)

######

selector_2 ='#KOSDAQ_now'
kosdaq = data.select_one(selector_2)
print(kosdaq)

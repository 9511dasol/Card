import cv2 as cv
import requests
from bs4 import BeautifulSoup
#https://www.shinhancard.com/pconts/images/contents/card/overseas_pay_visa.png


URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1216829_2207.html' # 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

img = soup.select_one('head > meta:nth-child(14)')
img2 = soup.select_one('#acc0 > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > span > img')

print(img2)
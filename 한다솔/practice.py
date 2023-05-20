import requests
from bs4 import BeautifulSoup

URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1218726_2207.html'
# 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')
#https://www.hyundaicard.com/img/com/card_big_h/card_MZROE2_h.png

#section08_0 > div > div > div > ul > li:nth-child(2) > a > div > strong
# bb = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.left_wrap.card_slider > div > div.swiper-wrapper > div.swiper-slide.vertical.swiper-slide-visible.swiper-slide-active > img')['src']
# print(bb)

# lis = soup.select('#section08_0 > div > div > div > ul > li')
# a = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.left_wrap.card_slider > div > div.swiper-wrapper > div.swiper-slide.vertical.swiper-slide-visible.swiper-slide-active > img')['src']
# for li in lis:
#     b = li.select_one('a > div > strong')
#     print(b.text)

#btnCardSelect > p.plate_img > img
#cms_area > div.card_design_container.start > div > ul > li:nth-child(1) > a > p.plate_img > img

a ={
    {'name': 'SOMJANG', 'address': 'Dongjakgu, Seoul'},
    { 'name': 'PUTTY', 'address': 'SSH World, Network'},
    { 'name': 'donghyunjang', 'address': 'Seoul, Korea'},
    { 'name': 'Avengers', 'address': 'Avengers Team Building, USA'},
}
print(a)
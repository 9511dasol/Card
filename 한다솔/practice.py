import requests
from bs4 import BeautifulSoup

URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1216792_2207.html'
# 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')
#https://www.hyundaicard.com/img/com/card_big_h/card_MZROE2_h.png
k = []

################# 신한카드
# cn = soup.select_one('.hidden-text')
# card_name = cn.get_text() # 카드이름
        
# benefits = soup.select('.title')
# for benefit in benefits: # 혜택정보 나열
#         print(benefit.text) # 카드 혜택 

#카드 이름
cn = soup.select_one('.hidden-text')
card_name = cn.get_text() # 카드이름
print(card_name)
h =''
# 혜택
bes = soup.select('div.cont')
for be in bes:
    a = be.select_one('strong.title').text # 혜택
    h += a + '\n'

print(h)



# 스크린샷
# src = soup.select('div.swiper-slide')
# for s in src:
#     a = s.select_one('img').get('src')
#     # a = s.select_one('img').get_attribute_list('alt') # 리스트 형태
#     print(a)

#카드 혜탹
src = soup.select('ul.marker_hyphen')
for s in src:
    k.append(s.select_one('li').get_text())
print(k)
# 연회비
# src = soup.select('span.ico_brand')
# for brand in src:
#     a = brand.select_one('img').get('src')
#     print(a)

# print(card_name)
#section08_0 > div > div > div > ul > li:nth-child(2) > a > div > strong
# bb = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.left_wrap.card_slider > div > div.swiper-wrapper > div.swiper-slide.vertical.swiper-slide-visible.swiper-slide-active > img')['src']
# print(bb)

# lis = soup.select('#section08_0 > div > div > div > ul > li')
# a = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.left_wrap.card_slider > div > div.swiper-wrapper > div.swiper-slide.vertical.swiper-slide-visible.swiper-slide-active > img')['src']
# for li in lis:
#     b = li.select_one('a > div > strong')
#     print(b.text)

#btnCardSelect > p.plate_img > img
#cms_area > div.card_design_container.start > div > ul > li:nth-child(1) > a > p.plate_img > img'         

# print("1221321")
# x ={
#     "dict" : 2131,
# }
# lis = ["a", "b", x, "d", "e"]
# dic = {
#     "abc" :lis,
# }
# print(dic['abc'][2]['dict'])
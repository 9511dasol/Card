import requests
from bs4 import BeautifulSoup

URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1188311_2207.html' # 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

def card_name(): # 카드 이름
    so = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > h1')
    return so.text
def benefit():
    k = ''
    lis = soup.select('#section08_0 > div > div > div > ul > li')
    for li in lis: # 혜택 정보
        a = li.select_one('a > div > strong')
        k+=f'{a.text}\n'         
    return k    


#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#m~x
#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2
#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2
# zero
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#kia
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#naver
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#nexon
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#대한 한공
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#무신사
#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2
#스마일페이
#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2
#기타

# a = benefit()    
# k = ''
# for i in a:
#     k+=f'{i}\n'

# cn =card_name()

# doc = {
#     'benefit' : k,
# }
# print(doc['benefit'])
# ls = soup.select('#cardCompareAfter > div.card_detail.gap80_40 > div.right_wrap > ul > li')

#for l in ls:  
    #a = l.select_one()
    #print(a.text) # 간편 혜택 아직 미구현


#section08_0 > div > div > div > ul > li:nth-child(3) > a > div > strong
#cardCompareAfter > div.card_detail.gap80_40 > div.right_wrap > ul > li:nth-child(1)


# from selenium import webdriver

# search_url = "https://www.shinhancard.com/pconts/html/card/credit/MOBFM281/MOBFM281R11.html?crustMenuId=ms581"

# browser = webdriver.Chrome('크롬드라이버 위치')  # chromedriver 다운받고, 다운 받은 경로 써주어야함
# browser.get(search_url)

# browser.implicitly_wait(2)

# ''' 크롤링 코드 '''

# browser.close()
import re
import requests
from bs4 import BeautifulSoup
import selenium
#https://www.shinhancard.com/pconts/images/contents/card/overseas_pay_visa.png


URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1219683_2207.html'
 # 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
data.raise_for_status()
soup = BeautifulSoup(data.text, 'html.parser')
# naverwebtoon
#container > div.component_wrap.type2 > div.WeekdayMainView__daily_all_wrap--UvRFc > div.WeekdayMainView__daily_all_item--DnTAH.WeekdayMainView__is_active--NSACG > ul > li:nth-child(1) > div > a > span > span

# sh
#section08_0 > div > div > div > ul > li:nth-child(1) > a > div > strong # 혜택 정보
#acc0 > div > div > table > tbody > tr:nth-child(1) > td.wgt_md.color_darkgray #연회비
# webs = soup.select('#section08_0 > div > div > div > ul > li')
# for web in webs:
#     web = web.select_one('a > div > strong')
#     print(web.text)

# bc
# webs = soup.select('#divCardDetail_info > div > div.cardItem > div')
# for web in webs:
#     web = web.select_one('div.tit > p')
#     print(web.text)

# print(soup.select_one('#contents > div.cardViewHad > div.cardDetail > h4').text) #cardname   
# print(soup.select_one('#contents > div.cardViewHad > div.cardDetail > div > ul > li').text # 연회비

#wrapper > div.modals-container > div > div.vfm__container.vfm--absolute.vfm--inset.vfm--outline-none.bottom-modal > div > div > article > div > div > article > div:nth-child(2) > div.table_col.multiple > table > tbody > tr:nth-child(1) > td:nth-child(2) > span
#wrapper > div.modals-container > div > div.vfm__container.vfm--absolute.vfm--inset.vfm--outline-none.bottom-modal > div > div > article > div > div > article > div:nth-child(2) > div.table_col.multiple > table > tbody > tr:nth-child(1) > td:nth-child(3) > span#연회비
#contents > div > section:nth-child(1) > article > div > div > button:nth-child(2)
#divCardDetail_info > div > div.cardItem > div:nth-child(1) > div.tit > p > span
#webs = soup.find_all("sapn", attrs={"class":re.compile("text")})
#contents > div.cardViewHad > div.cardDetail > h4
#divCardDetail_info > div > div.cardItem > div:nth-child(1) > div.tit > p

#contents_in > div.fp_info_box.card > div.pr_name > p # cardname
#benefit02 > div.benefit_view > strong:nth-child(3)
#benefit02 > div.benefit_view > strong.frist
print(soup.select_one('#acc0 > div > div > table > tbody > tr:nth-child(1) > td.wgt_md.color_darkgray').text)
webs = soup.select('#section08_0 > div > div > div > ul > li')
for web in webs:
    web = web.select_one('a > div > strong')
    print(web.text)

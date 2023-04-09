import requests
from bs4 import BeautifulSoup

URL = 'https://www.shinhancard.com/pconts/html/card/apply/credit/1216829_2207.html' # 카드 상세 정보
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

def card_name(): # 카드 이름
    ogtitle = soup.select_one('meta[property = "og:title"]')['content']
    so = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > h1')
    return ogtitle
#acc0 > div > div > table > tbody > tr:nth-child(1) > td.wgt_md.color_darkgray
def new():
    sos = soup.select('#acc0 > div > div > table > tbody > tr')
    for so in sos:
        a = so.select_one('span')
    #    fee = so.select_one('td.wgt_md.color_darkgray')
    #    CT = so.select_one(' td:nth-child(1) > span > img')
    print(a)

def benefit():
    k = ''
    lis = soup.select('#section08_0 > div > div > div > ul > li')
    for li in lis: # 혜택 정보
        a = li.select_one('a > div > strong')
        k += f'{a.text}\n'
    return k
def benefit2():
    k = ''
    lis = soup.select('#cardCompareAfter > div.card_detail.gap80_40 > div.right_wrap > ul > li')
    for li in lis: # 혜택 정보
        k += li.text
        k += li.select_one('span').text
    return k

sos = soup.select('#acc0 > div > div > table > tbody > tr')
sos = soup.select('#wrapper > div.modals-container > div > div.vfm__container.vfm--absolute.vfm--inset.vfm--outline-none.bottom-modal > div > div > article > div > div > article > div:nth-child(2) > div.table_col.multiple > table > thead > tr > th')
dd = soup.select('#acc0 > div > div > table > tbody > tr')
for d in dd:
    a = d.select_one('td.wgt_md.color_darkgray')
    print(d.text + '\n')

#acc0 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > span > img   // 국내카드
#acc0 > div > div > table > tbody > tr:nth-child(1) > td.wgt_md.color_darkgray   // 국내카드 총 연회비

#acc0 > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > span > img //마스터카드
#acc0 > div > div > table > tbody > tr:nth-child(2) > td.wgt_md.color_darkgray // 마스터 카드 총 연회비
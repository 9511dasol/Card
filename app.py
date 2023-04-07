from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import smtplib
from email.mime.text import EmailMessage
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://sparta:test@cluster0.sjc7unz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
app = Flask(__name__)
find_cards = list(db.card.find({},{'_id':False}))
card_name = ''
benefits = ''

@app.route('/')
def home():
   return render_template('main.html')

# @app.route('/findcard')
# def Main_home():
#     return render_template('find_card.html')

# @app.route('/user')
# def user_home():
#     return render_template('user.html')

# @app.route('/card_list')
# def user_home():
#     return render_template('card_list.html')

# @app.route('/card_rec')
# def card_rec():
#     return render_template('card_rec.html')
###############################---Post----#####################################################

@app.route("/Savecard", methods=["POST"])
def guestbook_post():
    card_comp = request.form['company']
    name = request.form['cardname']
    pdc = request.form['pdc']
    benefit1 = request.form['benefit1']
    benefit2 = request.form['benefit2']
    benefit3 = request.form['benefit3']
    benefit4 = request.form['benefit4']
    innate_number = request.form['innate_number']
    use_ex = request.form['use_ex']
    Rec = request.form['REC']
    Notice = request.form['Notice']
    doc ={
        'Company' : card_comp,
        'Card_Name' : name,
        'PDC' : pdc,
        'Benefit1' : benefit1,
        'Benefit2' : benefit2,
        'Benefit3' : benefit3,
        'Benefit4' : benefit4,
        'Innate_number' : innate_number,
        'Use_Ex' : use_ex,
        'REC' : Rec,
        'Notice' : Notice,
    }
    db.card.insert_one(doc)
    return jsonify({'msg': 'Saved!'})

@app.route("/delcard", methods=["POST"])
def del_card():
    innate_number = request.form['innate_number']

    doc ={
        'Innate_number' : innate_number,
    }

    db.users.delete_one(doc)
    return jsonify({'msg': 'Deleted!'})

@app.route("/findcard", methods=["POST"])
def find_post():
    pdc = request.form['pdc']
    card_comp = request.form['company']
    Benefit = request.form['Benefit']
    doc ={
        'PDC' : pdc,
        'Company' : card_comp,
        'Benefit' : Benefit,
    }

    find_cards = list(db.card.find(doc,{'_id':False}))
    return jsonify({'msg': 'finding~'})

@app.route("/contact", methods=["POST"])
def contact():
    mail = request.form['pdc']
    name = request.form['company']
    comment = request.form['Benefit']
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('@gmail.com','추후')

    message = EmailMessage()
    message["Subject"] = "이메일 제목"
    message.set_content(f"{comment}\n 이름:{name}\n 이메일:{mail}")
    message["From"] = '@gmail.com'  #보내는 사람의 이메일 계정
    message["To"] = mail

    smtp.send_message(message)
    return jsonify({'msg': '전송됐습니다'})

@app.route("/card_info", methods=["POST"])
def card_info():
    
    card_comp = request.form['company']
    bene = request.form('benefit')
    URL = request.form['url'] # 카드 상세 

    if(URL == None):
        return jsonify({'msg': 'URL을 입력하여 주십시오'})
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(URL, headers=headers)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text, 'html.parser')

           #cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > div
    if(card_comp =="신한"):    
        so = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > h1')
        card_name = so.text # 카드이름
        
        Year = soup.select('') #연회비

        lis = soup.select('#section08_0 > div > div > div > ul > li') 
        for li in lis: # 혜택정보 나열
            a = li.select_one('a > div > strong')
            benefits += f'{a.text}\n'         
        
    elif(card_comp =="삼성"):
        CN = soup.select_one('#contents > div > section:nth-child(1) > div.lists-card > div.card-tx > p')
        card_name = so.text # 카드이름

        Year = soup.select('') #연회비

        k = ''
        lis = soup.select('#contents > div > section:nth-child(1) > article > section > div > section > section > ul')
        for li in lis: 
            lis = soup.select('#contents > div > section:nth-child(1) > article > section > div > section > section > ul')
            k+=f'{li.text}\n' 

    elif(card_comp =="현대" and bene):
        if(bene == 'x' or bene=='m'): # 프리미엄카드 and m, x
            CN = soup.select_one('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2')
            card_name = so.text # 카드이름

            Year = soup.select('') #연회비

            k = ''
            lis = soup.select('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n'         
        elif(bene == "zero"):
            CN = soup.select_one('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2')
            card_name = so.text # 카드이름

            Year = soup.select('') #연회비

            k = ''
            lis = soup.select('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > ul > li')
            for li in lis: 
                k+=f'{li.text}\n'
        elif(bene == "with"):
            CN = soup.select_one('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2')
            card_name = so.text # 카드이름

            Year = soup.select('') #연회비

            k = ''             
            lis = soup.select('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n' 
        else:
            CN = soup.select_one('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2')
            card_name = so.text # 카드이름

            Year = soup.select('') #연회비

            k = ''             
            lis = soup.select('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n'
    else:
        return jsonify({'msg': '다시 입력하여 주십시오'})
###############################---Get----#####################################################

@app.route("/findcard", methods=["GET"])
def find_get():
    return jsonify({'result': find_cards})

@app.route("/All_Card", methods=["GET"])
def guestbook_get():
    all_cards = list(db.card.find({},{'_id':False}))

    return jsonify({'result': all_cards})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

############## 개방중인 코드##############


from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import smtplib
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://sparta:test@cluster0.sjc7unz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

# programer_card.html
@app.route("/Savecard", methods=["POST"]) # 카드 저장
def save_card():
    card_comp = request.form['company']
    name = request.form['cardname']
    pdc = request.form['pdc'] #3
    benefit = request.form['Benefits']
    innate_number = request.form['innate_number']
    use_ex = request.form['use_ex'] #6
    Rec = request.form['REC']
    Notice = request.form['Notice']
    Mf = request.form['MF'] #9
    pic_url = request.form['pic_url']
    using = request.form['using'] # 전월 이용금액
    url = request.form['url'] # 12
    main_bene = request.form['main_bene'] #13

    doc ={
        'Company' : card_comp,
        'Card_Name' : name,
        'PDC' : pdc,
        'Benefits' : benefit,
        'Innate_number' : innate_number,
        'Use_Ex' : use_ex,
        'REC' : Rec,
        'Notice' : Notice,
        'MF' : Mf,
        'pic_url' : pic_url,
        'using': using,
        'url': url,
        'main_bene': main_bene,
    }
    db.card.insert_one(doc)
    return jsonify({'msg': 'Saved!'})

@app.route("/delcard", methods=["POST"]) # 카드 삭제
def del_card():
    innate_number = request.form['innate_number']

    db.card.delete_one({'Innate_number' : innate_number})
    return jsonify({'msg': 'Deleted!'})

@app.route("/modify", methods=["POST"]) # 카드 수정
def modi_card():
    innate_number = request.form['innate_number']
    In ={
        'Innate_number' : innate_number,
    }
    card_comp = request.form['company']
    name = request.form['cardname']
    pdc = request.form['pdc'] #3
    benefit = request.form['benefit']
    use_ex = request.form['use_ex'] #6
    Rec = request.form['REC']
    Notice = request.form['Notice']
    Mf = request.form['MF'] #9
    pic_url = request.form['pic_url']
    using = request.form['using'] # 전월 이용금액
    url = request.form['url'] # 12
    main_bene = request.form['main_bene'] #13

    change ={
        'Company' : card_comp,
        'Card_Name' : name,
        'PDC' : pdc,
        'Benefits' : benefit,
        'Innate_number' : innate_number,
        'Use_Ex' : use_ex,
        'REC' : Rec,
        'Notice' : Notice,
        'MF' : Mf,
        'pic_url' : pic_url,
        'using': using,
        'url': url,
        'main_bene': main_bene,
    }
    db.card.update_one(In,{'$set':change})
    return jsonify({'msg': 'Updated!'})

@app.route("/All_Card", methods=["GET"])
def All_Card():    
    all_cards = list(db.card.find({},{'_id':False}))
    return jsonify({'result': all_cards})

##############################################

@app.route("/find_inquiries", methods=["POST"]) # url을 통한 카드 정보 가지고 오기
def find_inquiries():
    url = request.form['url'] # 카드 상세 page
    card_comp = request.form['company'] # 카드 회사
    
    if(card_comp =="현대"): # 현대카드시 이용
        bene = request.form['hc'] 

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text, 'html.parser')
    k=''
    pic =''
           #cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > div
    if(card_comp =="신한"):    
        cn = soup.select_one('#cardCompareAfter > div.card_detail.gap80_40 > div.card_name_wrap > h1')
        card_name = cn.text # 카드이름
        

        lis = soup.select('#section08_0 > div > div > div > ul > li') 
        for li in lis: # 혜택정보 나열
            a = li.select_one('a > div > strong')
            k += f'{a.text}\n'         
        
    elif(card_comp =="삼성"):
        cn = soup.select_one('#contents > div > section:nth-child(1) > div.lists-card > div.card-tx > p')
        card_name = cn.text # 카드이름

        #pic = soup.select_one('#contents > div > section:nth-child(1) > div.lists-card > div.card-container > figure > img')['src'] # 카드 사진
        k = ''
        lis = soup.select('#contents > div > section:nth-child(1) > article > section > div > section > section > ul')
        for li in lis: 
            k+=f'{li.text}\n' 

    elif(card_comp =="현대" and bene):
        if(bene == 'x' or bene=='m'): # 프리미엄카드 and m, x
            cn = soup.select_one('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2')
            card_name = cn.text # 카드이름

            k = ''
            lis = soup.select('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n'         
        elif(bene == "zero"):
            cn = soup.select_one('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2')
            card_name = cn.text # 카드이름

            #card_pic = soup.select_one('#container > div.content > div > div.detail_top.type_card > div.left_area > div.img_wrap > img')['src'] # 카드 이미지
            #pic = "https://www.hyundaicard.com" + card_pic
            
            k = ''
            lis = soup.select('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > ul > li')
            for li in lis: 
                k+=f'{li.text}\n'
        elif(bene == "with"):
            cn = soup.select_one('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > h2')
            card_name = cn.text # 카드이름


            k = ''             
            lis = soup.select('#container > div.content > div > div.detail_top.type_card.type02 > div.right_area > div > div.card_tit_wrap > span > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n' 
        else:
            cn = soup.select_one('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > h2')
            card_name = cn.text # 카드이름


            k = ''             
            lis = soup.select('#container > div.content > div > div.detail_top.type_card > div.right_area > div > div.card_tit_wrap > ul > li')
            for li in lis: # 혜택 정보        
                k+=f'{li.text}\n'
    else:
        return jsonify({'msg': '다시 입력하여 주십시오'})
    if(pic):  
        doc ={
        'Card_Name' : card_name,
        'Benefits' : k,
        'pic_url' : pic,
        'url': url
    }   
    else:
        doc ={
        'Card_Name' : card_name,
        'Benefits' : k,
        'url': url
    }
    db.im_card.insert_one(doc)
    return jsonify({'msg': 'finding~'}) # 조건을 db에 저장하는 코드

@app.route("/find_inquiries", methods=["GET"]) # find_inquiries_get
def find_inquiries_get():
    card = list(db.im_card.find({},{'_id':False}))
    db.im_card.delete_one({})
    return jsonify({'result': card})

##############################################

@app.route("/findcards", methods=["POST"]) # 카드 찾기 post
def find_cards():
    db.im_fc.delete_many({}) #db 인의 내용 전부 삭제

    pdc = request.form['pdc']
    card_comp = request.form['company']

    doc ={
        'PDC' : pdc,
        'Company' : card_comp,
    }

    db.im_fc.insert_one(doc) ## 일시적인 카드 찾기
    return jsonify({'msg': 'finding~'})

@app.route("/findcards", methods=["GET"]) # 카드 찾기 get
def findcards():
    select_cards = list(db.im_fc.find({},{'_id':False}))
    return jsonify({'result': select_cards})


@app.route("/bring_info", methods=["POST"]) # 임시 데이타 삭제하기(카드 조회)
def bring_info():
    innate_number = request.form['innate_number']

    db.innate.delete_many({}) # 전부 제거

    doc = {
        'Innate_number' : innate_number,
    }
    db.innate.insert_one(doc)
    return jsonify({'msg': '불러오는중'})

@app.route("/bring_info", methods=["GET"]) # 임시 데이타 삭제하기(카드 조회)
def bring_card_info():
    innate_number = list(db.innate.find({},{'_id':False})) # innate애서 1개 불러오기
    info = list(db.card.find(innate_number,{'_id':False})) # 해당 정보 찾아오기
    return jsonify({'result': info}) # 해단 정보 프론트에 보내기

##############################################

#1:1문의
@app.route("/contact", methods=["POST"])
def contact_post():
    mail = request.form['pdc']
    name = request.form['company']
    comment = request.form['comment']
    
    doc ={
        'mail' : mail,
        'name' : name,
        'comment' : comment,
    }

    db.contact.insert_one(doc)
    return jsonify({'msg': '전송됐습니다'})

@app.route("/contact", methods=["GET"])
def contact_get():
    all_SQ = list(db.contact.find({},{'_id':False}))

    return jsonify({'result': all_SQ})

@app.route("/contact_del", methods=["POST"])
def contact_del():
    comment = request.form['contact']
    
    doc ={
        'comment' : comment,
    }

    db.contact.delete_one(doc)
    return jsonify({'msg': '전송됐습니다'})

################################## faq

@app.route("/save_faqs", methods=["POST"])
def save_faqs():
    title = request.form['title']
    detail = request.form['detail']
    q_number = request.form['q_number']
    save_faqs ={
        'title': title,
        'detail': detail,
        'q_number': q_number,
    }
    db.faq.insert_one(save_faqs)
    return jsonify({'msg': 'Saved!'})

@app.route("/update_faqs", methods=["POST"])
def update_faqs():
    title = request.form['title']
    detail = request.form['detail']
    q_number = request.form['q_number']

    update ={
        'title': title,
        'detail': detail,
    }

    q = {
        'q_number': q_number,
    }

    db.faq.update_one(q,{'$set':update})

    return jsonify({'msg': 'Updated!'})

@app.route("/del_faq", methods=["POST"])
def del_faq():
    q_number = request.form['q_number']

    del_q = {
        'q_number': q_number,
    }

    db.faq.delete_one(del_q)
    return jsonify({'msg': 'Deleted!'})

@app.route("/show_faqs", methods=["GET"])
def show_faqs():
    faqs = list(db.faq.find({},{'_id':False}))
    return jsonify({'result': faqs})

################################## user
#카드착기
@app.route("/user_find_card", methods=["POST"])
def user_find_card_post():
@app.route("/user_find_card", methods=["GET"])
def user_find_card_get():

# 유명 카드


@app.route("/sh", methods=["GET"])
def famous_card_sh():
    fc ={'Company' : "신한",}
    famous_card = list(db.card.find(fc,{'_id':False}))
    return jsonify({'result': famous_card})

@app.route("/hd", methods=["GET"])
def famous_card_hd():
    fc ={'Company' : "현대",}
    famous_card = list(db.card.find(fc,{'_id':False}))
    return jsonify({'result': famous_card})

@app.route("/ss", methods=["GET"])
def famous_card_ss():
    fc ={'Company' : "삼성",}
    famous_card = list(db.card.find(fc,{'_id':False}))
    return jsonify({'result': famous_card})

@app.route("/kb", methods=["GET"])
def famous_card_kb():
    fc ={'Company' : "국민",}
    famous_card = list(db.card.find(fc,{'_id':False}))
    return jsonify({'result': famous_card})



# 개발자 카드 추천
@app.route("/card_rec", methods=["POST"])
def card_rec_post():

@app.route("/card_rec", methods=["GET"])
def card_rec_get():

#main
@app.route("/slider", methods=["GET"])
def slider():
    sliders = list(db.card.find({'REC' : 'O'},{'_id':False}))
    return jsonify({'result': sliders})
##################################
if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


############## 개방중인 코드##############
@app.route("/", methods=["POST"])
def ():
@app.route("/", methods=["GET"])
def ():


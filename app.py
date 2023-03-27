from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.sjc7unz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta
app = Flask(__name__)
find_cards = list(db.card.find({},{'_id':False}))

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/findcard')
def Main_home():
    return render_template('find_card.html')

@app.route('/user')
def user_home():
    return render_template('user.html')

@app.route('/card_list')
def user_home():
    return render_template('card_list.html')

@app.route('/card_rec')
def card_rec():
    return render_template('card_rec.html')
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
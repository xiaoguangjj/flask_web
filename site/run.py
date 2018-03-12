from flask import *

app = Flask(__name__)
import pymongo
from pymongo import MongoClient


client = MongoClient('0,0,0,0',27017)
db_name = 'RFID_card'
db = client[db_name]
collection_card_num = db['card_num']

@app.route("/",methods=['POST','GET'])
def add():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '123':
                error= "sorry"
        else:
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route("/delete")
def delete():
    error = None
    if request.mothod == 'POST':
        if len(request.form['card_num'])!= 16:
            error = "sorry"
        else:
            card = request.form['card_num']
            db.collection_card_num.drop()

    return render_template('index.html')

@app.route("/alter")
def alter():
    error = None
    if request.mothod == 'POST':
        if len(request.form['card_num'])!= 16:
            error = "sorry"
        else:
            card = request.form['card_num']
            db.collection_card_num.drop()

    return render_template('index.html')

@app.route("/query")
def query():
    error = None
    if request.mothod == 'POST':
        if len(request.form['card_num'])!= 16:
            error = "sorry"
        else:
            card = request.form['card_num']
            db.collection_card_num.drop()

    return render_template('index.html')


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True)





from flask import *
from flask import jsonify
app = Flask(__name__)
from pymongo import MongoClient
from time import strftime,gmtime
from flask import request
from flask import Flask,Blueprint
from flask_login import UserMixin,login_required,login_manager,login_manager
# from . import login_manager
# app = Flask(__name__)

from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email

client = MongoClient('0,0,0,0',27017)
db_name = 'Article'
db = client[db_name]
col_text = db['text']

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # id = db.Column(db.Integer, Primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.Integer, db.ForrignKey('roles.id'))

class LoginForm(Form):
    email = StringField('Email',validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

@login_manager.user_loaded_from_cookie
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

# #user models
# class User():
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return "1"

#url redict
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    # user = User()
    return "login page"

@auth.route('/logout',methods=['GET','POST'])
def logout():
    return "logout page"

@app.route('/test')
def test():
    return "yes , you are allowed."

@app.route("/article_add",methods=['POST','GET'])
def add(**param):

    # if not request.json:
    #     return jsonify(error='content-type should be json')

    spec = {}
    text = request.form['text']
    creater = request.form['creater']
    title = request.form['title']

    # text = param.get('text',None)
    # creater = param.get('creater',None)
    # title = param.get('title',None)
    time = strftime("%Y-%m-%d %H:%M:%S",gmtime())
    if text:
        spec['text'] = text

    if creater:
        spec['creater'] = creater

    if title:
        spec['title'] = title

    if time:
        spec['time'] = time
    result = db.col_text.insert({'text':text,'creater':creater,'title':title,'time':time})
    if result is not None:
        return jsonify({'result':True})
    else:
        return jsonify({'result':False})
    # return render_template('login.html')

@app.route("/article_alter",methods=['POST','GET'])
def alter(**param):

    # if not request.json:
    #     return jsonify(error='content-type should be json')
    text = request.form['text']
    creater = request.form['creater']
    title = request.form['title']

    # text = param.get('text',None)
    # creater = param.get('creater',None)
    # title = param.get('title',None)

    time = strftime("%Y-%m-%d %H:%M:%S",gmtime())

    # title_c = condition.get('title',None)

    result = db.col_text.update({'title': title},{'$set':{'text': text,'creater': creater,'title': title,'time': time}},multi=True)
    if result['updatedExisting'] is True:
        return jsonify({'result': True})
    else:
        return jsonify({'result':False})
    # return render_template('index.html')

@app.route("/article_query",methods=['POST','GET'])
def query(**param):

    spec = {}

    creater = request.values.get('creater')
    title = request.values.get('title')
    page = request.values.get('page',1)
    limit = request.values.get('limit',5)

    # creater = param.get('creater',None)
    # title = param.get('title',None)
    # page = param.get('page',None)
    # limit = param.get('limit',None)

    time = strftime("%Y-%m-%d %H:%M:%S",gmtime())
    if time:
        spec['time'] = time

    count = db.col_text.find().count()

    if page:
        page = int(page)

    if limit:
        limit = int(limit)
    if type(page) is int:
        if page > count:
            page = 1
        elif page<0:
            return jsonify({'code':"40004"})
    elif page.isdigit():
        page = int(page)
        if page > count:
            page = count
        elif page < 0:
            return jsonify({'code':"40004"})
    else:
        return jsonify({'code':"40004"})

    if type(limit) is int:
        if limit > count:
            limit = count
        elif limit < 0:
            return jsonify({'code':"40004"})
    elif limit.isdigit():
        limit = int(limit)
        if limit > count:
            limit = count
        elif limit < 0:
            return jsonify({'code':"40004"})
    else:
        return jsonify({'code':"40004"})

    num_skip = (page-1)*limit
    result = db.col_text.find({'$and' :[{'title':title},{'creater':creater}]},{'text':1,'creater':1,'time':1,'title':1}).limit(limit).skip(num_skip)
    if result is not None:
        data = str(list(result))
        print str(list(result)),"146====="
        return jsonify({"data": data,"ok": True})
    else:
        return jsonify({'ok':False})

@app.route("/article_info",methods=['POST','GET'])
def info(**param):
    # if not request.json:
    #     return jsonify(error='content-t.ype should be json')

    # if "creater" in request.values.get('creater'):
    creater = request.values.get('creater')

    # if "title" in request.values.get('title'):
    title = request.values.get('title')

    # text = param.get('text',None)
    # creater = param.get('creater',None)
    # title = param.get('title',None)

    result = db.col_text.find_one({'$or': [{'title':title},{'creater':creater}]})
    if result:
        return json.dumps({'data': str(result),'ok': True})
    else:
        return jsonify({'ok':False})

if __name__ == "__main__":
    app.register_blueprint(auth,url_prefix='/auth')

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True)

import sys,os,json,uuid
from flask import Flask, render_template, request, redirect, url_for, session, current_app, Response

from werkzeug.utils import secure_filename

from .models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html',title="AAAAA")

@app.route('/upload',methods=['POST','GET'])
def upload_img():
    if request.method == 'POST':
        input_image = request.files['file']
        basepath = os.path.dirname(__file__)
        input_image.filename = str(uuid.uuid1()) + ".jpg"
        upload_path = os.path.join(basepath, 'static',secure_filename(input_image.filename))
        input_image.save(upload_path)
        return redirect(url_for('list_uploaded_files'))
    return render_template('upload_image.html')

@app.route('/show_user')
def show_user():
    all_users = db.session.query(USER_INFO.id).all()
    print(all_users)
    for i in all_users:
        print(i)
    return render_template('list_user.html',users = all_users)
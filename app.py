from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import shutil
from flask import Flask
from flask import send_file
from flask_socketio import SocketIO, emit

from facebook_scraper import get_posts

import pandas as pd

app = Flask(__name__)
app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
app.config['UPLOAD_FOLDER'] = "files"
UPLOAD_DIRECTORY = "files"
path = "C:/Users/ASUSPRO/Downloads/scrap/files/"
import requests



if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
socketio = SocketIO( app )

def scraperpage(page,n,path=path):

    path = path+str(page)+".csv"
    posts=get_posts(page, pages=n)
    dataframe =pd.DataFrame(posts)
    dataframe.to_csv(path,index=False)
    return(path)



@app.route('/')
def index_view():
    
    return render_template('index.html')


@app.route('/',methods=['POST','GET'])
@socketio.on( 'my eventes' )
def predict():
    text = request.form['text']
    number = int(request.form['number'])
    path=scraperpage(str(text),number)
    return send_file(path, as_attachment=True)


    






@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''



    return jsonify(output)

if __name__ == '__main__':
    app.run()
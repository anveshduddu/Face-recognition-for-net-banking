from flask import Flask, render_template, request, session,Response
from twilio.rest import Client
from flask_mysqldb import MySQL
import random
from camera1 import *

from flaskProject.camera1 import name1

app = Flask(__name__)
video_stream = VideoCamera()

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')


@app.route('/register')
def face1():
    return render_template('register.html')


@app.route('/login')
def log():
    return render_template('logi.html')


@app.route('/otp')
def otp():
    return render_template('otp.html')


@app.route('/bank')
def bank():
    return render_template('bank.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/help')
def hel():
    return render_template('help.html')


@app.route('/html')
def html():
    return render_template('html.html')


@app.route('/side')
def side():
    return render_template('side.html')


@app.route('/transaction')
def transaction():
    return render_template('transaction.html')


@app.route('/signup')
def signu():
    return render_template('signup.html')


@app.route('/fail')
def fail():
    return render_template('failed.html')



@app.route('/', methods=['POST'])
def getValue():
    name= request.form ['name']
    print(name)
    return render_template('get.html' , name=name)

#database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
app.config['MYSQL_DB'] = 'design'
app.config['MYSQL_PORT'] = ''
mysql = MySQL(app)


@app.route('/login_validate', methods=['POST'])
def login_validate():
    Mobile = request.form['Mobile']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from up where mobileno = %s and pasword = %s',(Mobile, password,))
    mysql.connection.commit()
    data1 = cur.fetchone()
    if data1 is None:
        return render_template('signup.html')

    else:
        return render_template('bank.html')


@app.route('/signup1', methods=['POST'])
def data():

    if request.method == "POST":
        name = request.form['name']
        Mobile = request.form['Mobile']
        account = request.form['account']
        password = request.form['password']
        cur = mysql.connection.cursor()
        query = "INSERT INTO up (name,mobileno,accountno, pasword) VALUES (%s,%s, %s, %s)"
        cur.execute(query, (name, Mobile,account,password,))
        mysql.connection.commit()
    return render_template('logi.html')



#otp

app.secret_key = 'otp'


@app.route('/getOTP', methods=['POST'])
def getOTP():
    number = request.form['number']
    val = getOTPApi(number)
    if val:
        return render_template('otp.html')

@app.route('/validateOTP', methods=['POST'])
def validateOTP():
    otp = request.form['otp']
    if 'response' in session:
        s= session['response']
        session.pop('response', None)
        if s == otp:
            return render_template('face.html')
        else:
            return render_template('failed.html')

def generateOTP():
    return random.randrange(100000, 999999)


def getOTPApi(number):
    account_sid = 'AC40580915e7e816619e96c507b9894108'
    auth_token = '1990c806402d111ea5e710776bea853e'
    client = Client(account_sid, auth_token)
    otp = generateOTP()
    session['response'] = str(otp)
    body = 'Your OTP is' +' '+ str(otp) + ' '+'to complete the transaction /n Thanq for using our bank '
    message = client.messages.create(from_='+12185165429',
                                     body=body,
                                     to=number
                                     )
    if message.sid:
        return True
    else:
        return False



def gen(camera):
    while True:
        data = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face', methods=['GET','POST'])
def face():
    return render_template('face.html')


@app.route('/otp1',methods=['POST'])
def otp1():
    print("Name")
    print(name1)
    if "anvesh" in name1:
        return render_template('sucess.html')
    else:
        return render_template('failed.html')


if __name__ == '__main__':
    app.run(debug=True)
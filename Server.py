from flask import Flask, render_template,url_for,request,redirect
import csv
from string import Template
from pathlib import Path
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/submitform',methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        data=request.form.to_dict()
        storingdata(data)
        print(data)
    else:
        return redirect(url_for('home'))
    return render_template('Submitform.html')

def storingdata(data):
    name=data['name']
    email=data['email']
    #password = str(Path("/home/MohithSai/My-Portfolio/MyPassword.txt").read_text())
    html = Template(Path("/home/MohithSai/My-Portfolio/mail.html").read_text())
    msg = EmailMessage()
    msg.set_content(html.substitute(name=name),'html')
    msg['Subject'] = f'Hi {name},Thanks for contacting me.'
    msg['From'] = "mohithsai77@gmail.com"
    msg['To'] = f'{email}'

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login('mohithsai77@gmail.com','Msdhoni@28')
    s.send_message(msg)
    s.quit()
    with open("/home/MohithSai/My-Portfolio/database.csv",newline='', mode='a') as database2:
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        print(database2)
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(csv_writer)
        csv_writer.writerow([name,email,subject,message])

    #print("Done Sending Mail")


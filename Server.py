from flask import Flask, render_template,url_for,request,redirect
import csv
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
    with open("F:/WebDevelopment/venv/database.csv",newline='', mode='a') as database2:
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        print(database2)
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(csv_writer)
        csv_writer.writerow([name,email,subject,message])


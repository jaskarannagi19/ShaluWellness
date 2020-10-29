from flask import Flask,request,render_template
from flask_mail import Mail,  Message
from flask_admin import Admin,BaseView, expose



app = Flask(__name__)
app.static_folder = 'static'



admin = Admin(app, name="Shalu Wellbeing")



app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'shaluwebsite@gmail.com',
    MAIL_PASSWORD = 'Happy2020'
)

mail = Mail(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_mail/',methods=['POST'])
def send_mail():
    print(request.form.getlist('name')[0])

    name = request.form.getlist('name')[0]
    email = request.form.getlist('email')[0]
    subject = request.form.getlist('subject')[0]
    user_message = request.form.getlist('message')[0]


    msg = Message("Message from Website: "+subject,
                  sender="shaluwebsite@gmail.com",
                  recipients=["shaluwellbeing@gmail.com"])

    msg.body = "Message from "+name+" with email: "+ email + "\r\n"+ user_message

    mail.send(msg)
    return {'mail':'Mail sent'}



if __name__=='__main__':
    app.run(debug=True)
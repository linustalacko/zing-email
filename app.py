import email
from fileinput import hook_encoded
from flask import Flask, flash, redirect, render_template, url_for, request, make_response, session, abort
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = 'uaydfgsiasdfadsfosadfdafs'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'youjustgotzinged@gmail.com'
app.config['MAIL_PASSWORD'] = 'wnedoxtnbfaabgcf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('normal.html')

@app.route('/sending', methods=['POST', 'GET'])
def sending():
    if request.method == 'POST':
        email_address = request.form['email_address']
        subject = request.form['subject']
        message = request.form['message']
        how_many_times = request.form['times']

        if email_address == '' or subject == '' or message == '' or how_many_times == '':
            flash('Enter details correctly')
            return redirect(url_for('index'))

        if email_address == 'linustalacko1@gmail.com':
            return "Not allowed to send to the alpha male"

        if int(how_many_times) < 0:
            return redirect(url_for('stupid'))

        for times in range(int(how_many_times)):
            msg = Message(
                subject, 
                sender='youjustgotzinged@gmail.com', 
                recipients=[email_address]
            )

            msg.html = "<b>" + message + "</b> <br> <p>sent with <b>app-zing.com</b></p>"
            mail.send(msg)

        return redirect(url_for('success'))

@app.route('/success')
def success():
    return "<h1>Success!</h1><br><h2>Congratulations, you are annoying!</h2><a href='/'>Back to start</a>"

@app.route('/stupid')
def stupid():
    return "you are stupid, how can you send negative emails?"

if __name__ == '__main__':
    app.run(debug=True)

#wnedoxtnbfaabgcf

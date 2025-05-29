import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    business = request.form.get('business')
    description = request.form.get('description')
    package = request.form.get('package')
    style = request.form.get('style')

    # --- Email alert setup ---
    sender_email = "the90proofstudios@gmail.com"
    receiver_email = "the90proofstudios@gmail.com"
    app_password = "oifk hceq qzoq jagn"

    subject = f"New Lead: {name} – {package}"
    body = f"""
    You've received a new intake form submission:

    Full Name: {name}
    Email: {email}
    Business: {business}
    Description: {description}
    Package: {package}
    Style Preferences: {style}

    Submitted via 90proofstudios.com
    """
    #compose email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

    return redirect('/thankyou')


if __name__ == '__main__':
    app.run(debug=True)

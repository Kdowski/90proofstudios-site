import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from prompt_email_util import generate_prompt, send_prompt_email
from sheet_sync_util import append_lead_to_sheet



from flask import Flask, render_template, request, redirect

import os
app_password = os.environ.get("EMAIL_APP_PASSWORD")


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

    if not name or not email or not package:
        return "Missing required fields", 400

    # Generate AI image prompt
    prompt = generate_prompt(name, description, style)

    sender_email = "the90proofstudios@gmail.com"
    receiver_email = "the90proofstudios@gmail.com"

    subject = f"New Lead: {name} – {package}"
    body = f"""\
You've received a new intake form submission:

Full Name: {name}
Email: {email}
Business: {business}
Description: {description}
Package: {package}
Style Preferences: {style}

📸 Generated AI Image Prompt:
-----------------------------------
{prompt}

Submitted via 90proofstudios.com
"""

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Auto-confirmation email to client
    confirmation_subject = "Thanks for contacting 90 Proof Studios!"
    confirmation_body = f"""\
Hi {name},

Thanks for reaching out to 90 Proof Studios. We’ve received your submission and will review it shortly.

Here’s what you sent us:
---------------------------------
Business Name: {business}
Package Selected: {package}
Style Preferences: {style}

We’ll be in touch soon to get started. If you have any questions in the meantime, just reply to this email.

– The 90 Proof Studios Team
"""

    confirmation_msg = MIMEText(confirmation_body, 'plain', 'utf-8')
    confirmation_msg['From'] = sender_email
    confirmation_msg['To'] = email
    confirmation_msg['Subject'] = confirmation_subject

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("✅ Email sent to admin")
            server.sendmail(sender_email, email, confirmation_msg.as_string())
            print("✅ Confirmation email sent to client")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

    # Optionally sync to Google Sheets (if configured)
    try:
        append_lead_to_sheet(name, email, business, description, package, style)
    except Exception as e:
        print(f"❌ Error syncing to Google Sheet: {e}")

    return redirect('/thankyou')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)

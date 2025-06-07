# prompt_email_util.py

import smtplib
from email.mime.text import MIMEText
import os
import openai
from generate_openai_prompt import generate_image_prompt


# Authenticate with OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_prompt(name, description, style):
    return generate_image_prompt(name, description, style)


def generate_image_url(prompt, size="1024x1024"):
    """
    Sends the prompt to OpenAI and returns a generated image URL.
    """
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size=size,
            quality="standard"
        )
        return response.data[0].url
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return "Error generating image"

def send_prompt_email(prompt, image_url, client_email, client_name):
    """
    Sends the generated prompt + image URL to your inbox via email.
    """
    sender_email = "the90proofstudios@gmail.com"
    receiver_email = "the90proofstudios@gmail.com"
    app_password = os.environ.get("EMAIL_APP_PASSWORD")

    subject = f"Prompt Generated – {client_name}"
    body = f"""
Prompt for: {client_name} ({client_email})

Prompt:
-------
{prompt}

Image URL:
----------
{image_url}

Generated via 90Proof intake form.
"""

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("📬 Prompt + Image URL email sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

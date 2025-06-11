import smtplib
from email.mime.text import MIMEText
import os

# Import your new static prompt generator
from generate_openai_prompt import generate_image_prompts



# ⛔️ DALL·E image generation is disabled but retained for future use.
# def generate_image_url(prompt, size="1024x1024"):
#     try:
#         response = openai.images.generate(
#             model="dall-e-3",
#             prompt=prompt,
#             n=1,
#             size=size,
#             quality="standard"
#         )
#         return response.data[0].url
#     except Exception as e:
#         print(f"❌ Error generating image: {e}")
#         return "Error generating image"

def send_prompt_email(prompt, client_email, client_name):
    """
    Sends the generated prompt to the admin's inbox via email.
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
        print("📬 Prompt email sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

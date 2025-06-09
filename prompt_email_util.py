import smtplib
from email.mime.text import MIMEText
import os
# import openai  # ⛔️ No longer using OpenAI image generation
from generate_openai_prompt import generate_image_prompt

# openai.api_key = os.environ.get("OPENAI_API_KEY")  # ⛔️ Commented out API key usage


def generate_prompt_openai(name, business, description, style):
    """
    Generates a prompt using custom logic only.
    The OpenAI image generation is disabled for now.
    """
    try:
        prompt = generate_image_prompt(name, business, description, style)
        # image_url = generate_image_url(prompt)  # ⛔️ Disabled
        return prompt  # only returning prompt now
    except Exception as e:
        print(f"❌ Error in prompt generation: {e}")
        return "Prompt generation failed"


# def generate_image_url(prompt, size="1024x1024"):
#     """
#     [DISABLED] Generates an image using OpenAI DALL·E API — commented out.
#     """
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
    Sends the generated prompt to your inbox via email (no image URL).
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


import smtplib
from email.mime.text import MIMEText
import os

def generate_prompt(name, description, style):
    """
    Generates a high-quality image prompt tailored for OpenAI's image generation models.

    Parameters:
        name (str): The client name or business name.
        description (str): User-provided brand/idea description.
        style (str): Preferred design style from user.

    Returns:
        str: A prompt crafted for OpenAI image generation.
    """
    return (
        f"Logo design for a brand called '{name}'. "
        f"The brand is described as: {description.strip()}. "
        f"Design style requested: {style.strip().lower()}. "
        "Generate a clean, professional vector-style logo. "
        "Centered layout, white background, sharp lines, no text, no watermark. "
        "Digital and print ready, suitable for web and business use. "
        "Render as a stylized vector illustration."
    )


def send_prompt_email(prompt, client_email, client_name):
    """Sends the generated prompt to your inbox via email."""
    sender_email = "the90proofstudios@gmail.com"
    receiver_email = "the90proofstudios@gmail.com"
    app_password = os.environ.get("EMAIL_APP_PASSWORD")

    subject = f"Prompt Generated – {client_name}"
    body = f"""
Prompt for: {client_name} ({client_email})

{prompt}

Generated automatically via intake form.
"""

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("📬 Prompt email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send prompt email: {e}")

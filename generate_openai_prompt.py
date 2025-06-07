import openai
import os

# Load API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_image_prompt(name, description, style):
    """Generates a prompt optimized for OpenAI's image model (DALL·E)."""
    base_prompt = f"""
You're an expert brand designer. Generate a single image prompt for DALL·E to create a logo based on the following:

Client Name: {name}
Brand Description: {description}
Style Preferences: {style}

Instructions:
- Make the prompt extremely clear, visual, and specific
- Focus on digital logo use cases
- Avoid words like 'logo' or 'text' in the prompt
- Avoid clutter or mixed metaphors
- Use design language, mood, and color references where appropriate
- Output only the final image prompt, no preamble or summary
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": base_prompt}],
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()

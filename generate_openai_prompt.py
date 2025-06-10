def generate_image_prompt(name, description, style):
    """
    Generates a static prompt using local logic only (no OpenAI API).
    This is a placeholder that mimics the style of a GPT-generated prompt.
    """

    prompt = (
        f"A modern, visually striking digital logo inspired by the brand '{name}', "
        f"which focuses on {description.lower().strip()}. "
        f"The design should reflect a {style.lower().strip()} aesthetic using clean lines, balanced composition, "
        f"and a professional color palette. Avoid using text or over-complicating the layout. "
        f"Think in terms of logo application for digital media, branding kits, and merch packaging."
    )

    return prompt

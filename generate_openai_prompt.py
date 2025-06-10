def generate_image_prompt(name, description, style):
    """
    Generates a polished, human-readable prompt for AI image tools.
    Designed for logos — clear, modern, and without mentioning 'logo' or 'text'.
    """
    prompt = (
        f"Design a minimalist, professional symbol representing the brand '{name}'. "
        f"The brand focuses on {description.strip().lower()}. "
        f"The visual style should be {style.strip().lower()} — think modern branding aesthetics with clean geometry, balanced negative space, and color harmony. "
        f"The image should work well in both light and dark themes, suitable for digital use such as social icons, product labels, and mobile apps. "
        f"Do not include any text, words, or lettering."
    )

    return prompt


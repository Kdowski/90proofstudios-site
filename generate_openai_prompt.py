def generate_image_prompts(name, description, style):
    """
    Returns two prompt styles for logo generation:
    - clean_prompt: straightforward, modern, and minimal
    - mood_prompt: more artistic, evocative, and abstract
    """
    name = name.strip()
    description = description.strip().lower()
    style = style.strip().lower()

    clean_prompt = (
        f"Design a minimalist, professional symbol representing the brand '{name}'. "
        f"The brand focuses on {description}. "
        f"The visual style should be {style} — think modern branding aesthetics with clean geometry, balanced negative space, and color harmony. "
        f"The image should work well in both light and dark themes, suitable for digital use such as social icons, product labels, and mobile apps. "
        f"Do not include any text, words, or lettering."
    )

    mood_prompt = (
        f"A concept-driven visual representation of the brand '{name}', evoking the essence of {description}. "
        f"Imagine a {style} tone — interpretive and rich in metaphor, with expressive shapes or symbolic imagery. "
        f"Think mood boards, packaging, and aesthetic-led design for creators who want their branding to tell a story without text."
    )

    return clean_prompt, mood_prompt

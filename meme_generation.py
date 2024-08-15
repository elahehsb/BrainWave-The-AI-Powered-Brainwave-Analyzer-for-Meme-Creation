import random
from PIL import Image, ImageDraw, ImageFont

def load_meme_templates():
    # Load a collection of meme templates
    templates = ["meme1.jpg", "meme2.jpg", "meme3.jpg"]
    return templates

def generate_meme(text, template_path):
    # Load template and add text
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Add text to image
    draw.text((10, 10), text, font=font, fill="white")
    meme_path = "generated_meme.jpg"
    image.save(meme_path)
    return meme_path

def create_meme(features):
    templates = load_meme_templates()
    template_path = random.choice(templates)
    text = f"Feeling {'happy' if features[0] > 0 else 'sad'}!"
    return generate_meme(text, template_path)

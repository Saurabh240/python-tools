# Batch resizes images using Pillow.

from PIL import Image
import os

for file in os.listdir('images'):
    if file.endswith('.jpg'):
        img = Image.open(f'images/{file}')
        img = img.resize((800, 600))
        img.save(f'resized/{file}')

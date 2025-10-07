import os
import sys
from PIL import Image

image_path = sys.argv[1]
image_format = sys.argv[2].lower()

if os.path.isfile(image_path):
  try:
    img = Image.open(image_path)
    base, ext = os.path.splitext(image_path)
    new_image_path = f"{base}.{image_format}"
    img.save(new_image_path, format=image_format.upper())
    print(f"Image converted and saved as {new_image_path}")
  except Exception as e:
    print(f"Error: {e}")

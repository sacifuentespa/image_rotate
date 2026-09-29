from PIL import Image
import os

old_path = os.path.join(os.getcwd(), 'images')
new_path = os.path.join('opt', 'icons')

print(new_path)

for image in os.listdir(old_path):
    try:
        img = Image.open(os.path.join(old_path, image))
        img.rotate(-90).resize((128, 128)).convert("RGB").save(os.path.join(new_path,image), 'jpeg')
        img.close()
    except:
        continue
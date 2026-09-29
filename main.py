from PIL import Image
import os

old_path = os.path.join(os.getcwd(), 'images')
new_path = os.path.join('opt', 'icons')

for image in os.listdir(old_path):
	if '.' not in image[0]:
		img = Image.open(os.path.join(old_path, image))
		img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
		img.close()
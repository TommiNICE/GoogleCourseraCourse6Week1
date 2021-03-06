#!/usr/bin/env python3

from PIL import Image
import os

directory = '/path/to/image/folder/'

for file in os.listdir(directory):
    if file == ".DS_Store":
        continue
    filename = file.split(".")
    img = Image.open('/path/to/image/folder/' + file)
    target_name = filename[0] + ".jpg"
    rgb_image = img.rotate(270).resize((128,128)).convert('RGB')
    rgb_image.save('/path/to/destination/folder' + target_name)




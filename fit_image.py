#!/usr/bin/env python3

from PIL import Image
import os

directory = '/home/tova/Documents/PycharmProjects/GoogleCourseraCourse6Week1/images'

for file in os.listdir(directory):
    if file == ".DS_Store":
        continue
    filename = file.split(".")
    img = Image.open('/home/tova/Documents/PycharmProjects/GoogleCourseraCourse6Week1/images/' + file)
    target_name = filename[0] + ".jpg"
    rgb_image = img.rotate(270).resize((128,128)).convert('RGB')
    rgb_image.save('/home/tova/Documents/PycharmProjects/GoogleCourseraCourse6Week1/src/' + target_name)




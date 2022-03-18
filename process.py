# source ./.env/Scripts/active
# Screenshots: C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots\
# ls ./map > fn.txt

import cv2
import os
import json
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

test = './test'
maps = './map'
proc = './proc'

with open('mappings.json') as file:
    mapping = json.load(file)

for subdir, dirs, files in os.walk(maps):
    # print(len(files))
    for file in files:
        filepath = subdir + os.sep + file
        img = cv2.imread(filepath)

        # Check if map or seed
        img_type = img[10:30, 10:50]
        img_text = pytesseract.image_to_string(img_type).strip()

        # If 'Map' is read from crop, cut and save minimap section
        if img_text == 'Map':
            crop_mm = img[0:0+340, 0:0+315]

            seed_filepath = subdir + os.sep + mapping[file]
            seed_img = cv2.imread(seed_filepath)
            crop_seed = seed_img[637:637+65, 1660:1660+80] # original 670, 1655
            # cv2.imshow('crop', crop_seed)
            # cv2.waitKey()
            seed_text = pytesseract.image_to_string(crop_seed).split()
            seed_text = '.'.join(seed_text)
            print(seed_text)

            seed_concat = seed_img[637:637+340, 1660:1660+315]
            concat_img = np.concatenate((crop_mm, seed_concat),axis=1)
            new_filepath = proc + os.sep + seed_text + '.jpg'
            print(new_filepath)
            cv2.imwrite(new_filepath, concat_img)
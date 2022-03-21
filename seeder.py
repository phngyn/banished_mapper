# source ./.env/Scripts/active
# Screenshots: C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots\
# ls ./map > fn.txt

from tkinter import N
import cv2
import os
import json
import subprocess
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


def mapper(filename):
    mapped = {}
    with open(filename) as f:
        lines = f.read().splitlines()
        mapped = dict(zip(lines[::2], lines[1::2]))
    return mapped


def make_seed_dictionary():
    with open("mappings.json", "w") as file:
        new_maps = mapper("fn.txt")
        json.dump(new_maps, file)
    return None


def process_maps(maps_dir, processed_dir, seed_mapping):

    for subdir, dirs, files in os.walk(maps_dir):
        # print(len(files))
        for file in files:
            filepath = subdir + os.sep + file
            img = cv2.imread(filepath)

            # Check if map or seed
            img_type = img[10 : 10 + 30, 10 : 10 + 50]
            img_text = pytesseract.image_to_string(img_type).strip()
            # print(img_text)

            # If 'Map' is read from crop, cut and save minimap section
            if img_text == "Map":
                crop_mm = img[0 : 0 + 450, 0 : 0 + 420] 

                seed_filepath = subdir + os.sep + seed_mapping[file]
                seed_img = cv2.imread(seed_filepath)
                crop_seed = seed_img[
                    620 : 620 + 90, 1635 : 1635 + 110
                ]  # original 670, 1655 # y620, x1635 -> y710, x1745  

                # cv2.imshow('crop', crop_seed)
                # cv2.waitKey()
                seed_text = pytesseract.image_to_string(crop_seed).split()
                seed_text = ".".join(seed_text)
                # print(seed_text)

                seed_concat = seed_img[620 : 620 + 450, 1635 : 1635 + 420]
                concat_img = np.concatenate((crop_mm, seed_concat), axis=1)
                new_filepath = processed_dir + os.sep + seed_text + ".jpg"
                print("Making:", filepath, seed_filepath, new_filepath)
                cv2.imwrite(new_filepath, concat_img)

    return None


def make_map_dict(map_dir):
    process = subprocess.run(f"ls {map_dir}", capture_output=True)
    process = process.stdout.decode("utf-8").split("\n")
    process = process[0 : len(process) - 1]
    process = dict(zip(process[::2], process[1::2]))
    return process


if __name__ == "__main__":

    test_dir = "./test"
    map_dir = "./map"
    proc_dir = "./proc"

    map_dict = make_map_dict(map_dir)

    process_maps(map_dir, proc_dir, map_dict)

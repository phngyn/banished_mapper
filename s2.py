# source ./.env/Scripts/active
# Screenshots: C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots\
# ls ./map > fn.txt


import re
import cv2
import os
import json
import subprocess
import pytesseract
import numpy as np
import natsort

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
        for file in files:
            try:
                filepath = subdir + os.sep + file
                img = cv2.imread(filepath)
                crop_mm = img[0 : 0 + 450, 0 : 0 + 420]
                crop_mm = cv2.putText(
                    img=crop_mm,
                    text=str(seed_mapping[file]),
                    org=(70, 35),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=0.8,
                    color=(255, 255, 0),
                    thickness=1,
                )
                new_filepath = (
                    processed_dir + os.sep + str(seed_mapping[file]) + ".jpg"
                )  #
                print("Making:", filepath, new_filepath)
                cv2.imwrite(new_filepath, crop_mm)
            except KeyError:
                continue

    return None


def make_map_dict(map_dir):
    process = subprocess.run(f"ls {map_dir}", capture_output=True)
    process = process.stdout.decode("utf-8").split("\n")
    process = process[0 : len(process) - 1]
    process = dict(zip(process[::2], process[1::2]))
    return process


def make_map_dict2(map_dir, start_seed):
    process = subprocess.run(f"ls {map_dir}", capture_output=True)
    process = process.stdout.decode("utf-8").split("\n")
    process = process[0 : len(process) - 1]

    process = dict(zip(process[1::2], process[::2]))
    for key in process.keys():
        process[key] = start_seed
        start_seed += 1

    return process


def get_map_names(map_dir):
    process = subprocess.run(f"ls {map_dir}", capture_output=True)
    process = process.stdout.decode("utf-8").split("\n")
    process = process[0 : len(process) - 1]
    return process


def concat_imgs_along_y(map_dir, processed_dir, units, map_list):
    while len(map_list) > 0:
        img_list = map_list[:units]
        img_final = np.empty([450, 1, 3])

        for subdir, dirs, files in os.walk(map_dir):
            for file in img_list:
                filepath = subdir + os.sep + file
                img_new = cv2.imread(filepath)
                img_final = np.concatenate((img_final, img_new), axis=1)
        new_filepath = (
            processed_dir + os.sep + img_list[0] + "_" + img_list[units - 1] + ".jpg"
        )
        cv2.imwrite(new_filepath, img_final)
        del map_list[:units]
    return None


def concat_imgs_along_x(map_dir, processed_dir, units, map_list):
    while len(map_list) > 0:
        img_list = map_list[:units]
        img_final = np.empty([1, 4201, 3])

        for subdir, dirs, files in os.walk(map_dir):
            for file in img_list:
                filepath = subdir + os.sep + file
                img_new = cv2.imread(filepath)
                img_final = np.concatenate((img_final, img_new), axis=0)
        new_filepath = (
            processed_dir
            + os.sep
            + img_list[0]
            + "_"
            + img_list[units - 1]
            + ".jpg"
        )
        cv2.imwrite(new_filepath, img_final)
        del map_list[:units]
    return None


if __name__ == "__main__":

    # Top seeds
    #   100000075; 328  
    #   100000121; 328
    #   100000264; 328
    
    test_dir = "./test"
    map_dir = "./maps"
    map_dir2 = "./maps2"
    proc_dir = "./proc"
    map_1x1 = "./proc_final/1x1"
    ss_dir = r"'C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots'"

    map_dict = make_map_dict2(map_dir, 256)
    print(map_dict)
    process_maps(map_dir,proc_dir,map_dict)
    map_list = natsort.natsorted(get_map_names(map_1x1))
    map_list = map_list[0:800]
    concat_imgs_along_y(map_1x1, map_dir2, 10, map_list)
    map_list = natsort.natsorted(get_map_names(map_dir2))
    print(map_list)
    concat_imgs_along_x(map_dir2, proc_dir, 10, map_list)

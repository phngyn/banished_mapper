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
            filepath = subdir + os.sep + file
            img = cv2.imread(filepath)
            crop_mm = img[0 : 0 + 450, 0 : 0 + 420]
            crop_mm = cv2.putText(
                img=crop_mm,
                text=seed_mapping[file],
                org=(70, 35),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=0.8,
                color=(255, 255, 0),
                thickness=1,
            )
            new_filepath = processed_dir + os.sep + seed_mapping[file] + ".jpg"  #
            print("Making:", filepath, new_filepath)
            cv2.imwrite(new_filepath, crop_mm)

    return None


def make_map_dict(map_dir):
    process = subprocess.run(f"ls {map_dir}", capture_output=True)
    process = process.stdout.decode("utf-8").split("\n")
    process = process[0 : len(process) - 1]
    process = dict(zip(process[::2], process[1::2]))
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
        new_filepath = processed_dir + os.sep + img_list[0] + "_" + img_list[units-1] + ".jpg"
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
        new_filepath = processed_dir + os.sep + img_list[0] + "_" + img_list[units-1] + ".jpg"
        cv2.imwrite(new_filepath, img_final)
        del map_list[:units]
    return None


if __name__ == "__main__":

    test_dir = "./test"
    map_dir = "./maps"
    map_dir2 = "./maps2"
    proc_dir = "./proc"
    ss_dir = (
        r"C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots"
    )

    # =""""&A1&""""&":"&""""&B1&""""&","
    map_dict = {
        "20220322134341_1.jpg": "1",
        "20220322134407_1.jpg": "2",
        "20220322134434_1.jpg": "3",
        "20220322134501_1.jpg": "4",
        "20220322134528_1.jpg": "5",
        "20220322134555_1.jpg": "6",
        "20220322134622_1.jpg": "7",
        "20220322134649_1.jpg": "8",
        "20220322134716_1.jpg": "9",
        "20220322134742_1.jpg": "10",
        "20220322134809_1.jpg": "11",
        "20220322134836_1.jpg": "12",
        "20220322134903_1.jpg": "13",
        "20220322134930_1.jpg": "14",
        "20220322134957_1.jpg": "15",
        "20220322135024_1.jpg": "16",
        "20220322135051_1.jpg": "17",
        "20220322135118_1.jpg": "18",
        "20220322135145_1.jpg": "19",
        "20220322135212_1.jpg": "20",
        "20220322135239_1.jpg": "21",
        "20220322135306_1.jpg": "22",
        "20220322135333_1.jpg": "23",
        "20220322135400_1.jpg": "24",
        "20220322135427_1.jpg": "25",
        "20220322135454_1.jpg": "26",
        "20220322135521_1.jpg": "27",
        "20220322135548_1.jpg": "28",
        "20220322135615_1.jpg": "29",
        "20220322135642_1.jpg": "30",
        "20220322135709_1.jpg": "31",
        "20220322135736_1.jpg": "32",
        "20220322135803_1.jpg": "33",
        "20220322135830_1.jpg": "34",
        "20220322135857_1.jpg": "35",
        "20220322135924_1.jpg": "36",
        "20220322135951_1.jpg": "37",
        "20220322140017_1.jpg": "38",
        "20220322140044_1.jpg": "39",
        "20220322140111_1.jpg": "40",
        "20220322140138_1.jpg": "41",
        "20220322140205_1.jpg": "42",
        "20220322140232_1.jpg": "43",
        "20220322140259_1.jpg": "44",
        "20220322140326_1.jpg": "45",
        "20220322140353_1.jpg": "46",
        "20220322140420_1.jpg": "47",
        "20220322140447_1.jpg": "48",
        "20220322140514_1.jpg": "49",
        "20220322140541_1.jpg": "50",
        "20220322140608_1.jpg": "51",
        "20220322140635_1.jpg": "52",
        "20220322140702_1.jpg": "53",
        "20220322140729_1.jpg": "54",
        "20220322140756_1.jpg": "55",
        "20220322140823_1.jpg": "56",
        "20220322140850_1.jpg": "57",
        "20220322140917_1.jpg": "58",
        "20220322140944_1.jpg": "59",
        "20220322141011_1.jpg": "60",
        "20220322141038_1.jpg": "61",
        "20220322141104_1.jpg": "62",
        "20220322141131_1.jpg": "63",
        "20220322141158_1.jpg": "64",
        "20220322141225_1.jpg": "65",
        "20220322141252_1.jpg": "66",
        "20220322141319_1.jpg": "67",
        "20220322141346_1.jpg": "68",
        "20220322141413_1.jpg": "69",
        "20220322141440_1.jpg": "70",
        "20220322141507_1.jpg": "71",
        "20220322141534_1.jpg": "72",
        "20220322141601_1.jpg": "73",
        "20220322141628_1.jpg": "74",
        "20220322141655_1.jpg": "75",
        "20220322141722_1.jpg": "76",
        "20220322141749_1.jpg": "77",
        "20220322141816_1.jpg": "78",
        "20220322141843_1.jpg": "79",
        "20220322141910_1.jpg": "80",
        "20220322141937_1.jpg": "81",
        "20220322142004_1.jpg": "82",
        "20220322142031_1.jpg": "83",
        "20220322142058_1.jpg": "84",
        "20220322142125_1.jpg": "85",
        "20220322142152_1.jpg": "86",
        "20220322142219_1.jpg": "87",
        "20220322142246_1.jpg": "88",
        "20220322142313_1.jpg": "89",
        "20220322142340_1.jpg": "90",
        "20220322142406_1.jpg": "91",
        "20220322142433_1.jpg": "92",
        "20220322142500_1.jpg": "93",
        "20220322142527_1.jpg": "94",
        "20220322142554_1.jpg": "95",
        "20220322142621_1.jpg": "96",
        "20220322142648_1.jpg": "97",
        "20220322142715_1.jpg": "98",
        "20220322142742_1.jpg": "99",
        "20220322142809_1.jpg": "100",
        "20220322142836_1.jpg": "101",
        "20220322142903_1.jpg": "102",
        "20220322142930_1.jpg": "103",
        "20220322142957_1.jpg": "104",
        "20220322143025_1.jpg": "105",
        "20220322143052_1.jpg": "106",
        "20220322143119_1.jpg": "107",
        "20220322143146_1.jpg": "108",
        "20220322143213_1.jpg": "109",
        "20220322143240_1.jpg": "110",
        "20220322143307_1.jpg": "111",
        "20220322143334_1.jpg": "112",
        "20220322143401_1.jpg": "113",
        "20220322143428_1.jpg": "114",
        "20220322143455_1.jpg": "115",
        "20220322143522_1.jpg": "116",
        "20220322143549_1.jpg": "117",
        "20220322143616_1.jpg": "118",
        "20220322143643_1.jpg": "119",
        "20220322143710_1.jpg": "120",
        "20220322143737_1.jpg": "121",
        "20220322143804_1.jpg": "122",
        "20220322143832_1.jpg": "123",
        "20220322143859_1.jpg": "124",
        "20220322143926_1.jpg": "125",
        "20220322143953_1.jpg": "126",
        "20220322144020_1.jpg": "127",
        "20220322144047_1.jpg": "128",
        "20220322144114_1.jpg": "129",
        "20220322144141_1.jpg": "130",
        "20220322144208_1.jpg": "131",
        "20220322144235_1.jpg": "132",
        "20220322144302_1.jpg": "133",
        "20220322144329_1.jpg": "134",
        "20220322144356_1.jpg": "135",
        "20220322144423_1.jpg": "136",
        "20220322144450_1.jpg": "137",
        "20220322144518_1.jpg": "138",
        "20220322144545_1.jpg": "139",
        "20220322144612_1.jpg": "140",
        "20220322144639_1.jpg": "141",
        "20220322144706_1.jpg": "142",
        "20220322144733_1.jpg": "143",
        "20220322144800_1.jpg": "144",
        "20220322144827_1.jpg": "145",
        "20220322144854_1.jpg": "146",
        "20220322144921_1.jpg": "147",
        "20220322144948_1.jpg": "148",
        "20220322145015_1.jpg": "149",
        "20220322145042_1.jpg": "150",
        "20220322145109_1.jpg": "151",
        "20220322145137_1.jpg": "152",
        "20220322145204_1.jpg": "153",
        "20220322145231_1.jpg": "154",
        "20220322145258_1.jpg": "155",
        "20220322145325_1.jpg": "156",
        "20220322145352_1.jpg": "157",
        "20220322145419_1.jpg": "158",
        "20220322145446_1.jpg": "159",
        "20220322145513_1.jpg": "160",
        "20220322145540_1.jpg": "161",
        "20220322145607_1.jpg": "162",
        "20220322145634_1.jpg": "163",
        "20220322145701_1.jpg": "164",
        "20220322145728_1.jpg": "165",
        "20220322145755_1.jpg": "166",
        "20220322145822_1.jpg": "167",
        "20220322145849_1.jpg": "168",
        "20220322145917_1.jpg": "169",
        "20220322145944_1.jpg": "170",
        "20220322150011_1.jpg": "171",
        "20220322150038_1.jpg": "172",
        "20220322150105_1.jpg": "173",
        "20220322150132_1.jpg": "174",
        "20220322150159_1.jpg": "175",
        "20220322150226_1.jpg": "176",
        "20220322150253_1.jpg": "177",
        "20220322150320_1.jpg": "178",
        "20220322150347_1.jpg": "179",
        "20220322150414_1.jpg": "180",
        "20220322150441_1.jpg": "181",
        "20220322150508_1.jpg": "182",
        "20220322150535_1.jpg": "183",
        "20220322150602_1.jpg": "184",
        "20220322150629_1.jpg": "185",
        "20220322150657_1.jpg": "186",
        "20220322150724_1.jpg": "187",
        "20220322150751_1.jpg": "188",
        "20220322150818_1.jpg": "189",
        "20220322150845_1.jpg": "190",
        "20220322150912_1.jpg": "191",
        "20220322150939_1.jpg": "192",
        "20220322151006_1.jpg": "193",
        "20220322151033_1.jpg": "194",
        "20220322151100_1.jpg": "195",
        "20220322151127_1.jpg": "196",
        "20220322151154_1.jpg": "197",
        "20220322151221_1.jpg": "198",
        "20220322151248_1.jpg": "199",
        "20220322151315_1.jpg": "200"
    }

    # process_maps(map_dir, proc_dir, map_dict)
    map_list = natsort.natsorted(get_map_names(map_dir2))
    print(map_list)
    # img_test = cv2.imread("./maps2/100000000.jpg_100000009.jpg.jpg")
    # print(img_test.shape)
    # concat_imgs_along_y(map_dir, proc_dir, 10, map_list)
    concat_imgs_along_x(map_dir2, proc_dir, 10, map_list)

    # 100000264 - trade posts; 328/4
    # 100000121 - trade posts; 320/4


    # 1. Read screenshot directory
    # 1a. Delete
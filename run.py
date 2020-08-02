#!/usr/bin/env python3
import os
import requests
import json

PATH = '/home/student-00-2f21e74338af/supplier-data/descriptions'
PATHIMG = '/home/student-00-2f21e74338af/supplier-data/images'

def get_files():
    texts = []
    files = os.listdir(PATH)
    for file in files:
        if '.txt' in file:
            texts.append(file)
    return texts


def dic_maker(txt, images, image_number):

    path = PATH+'/'+txt
    dictt = {}
    with open(path) as text:
        lines = text.readlines()
        dictt['name'] = lines[0].strip()
        dictt['weight'] = int(lines[1][:3].strip())
        dictt['description'] = lines[2].strip()
        dictt['image_name'] = images[image_number]


    return dictt


def main():
    image_number = 0
    files = get_files()
    images = [item for item in os.listdir(PATHIMG)]
    files.sort()
    images.sort()

    for txt in files:
        p = dic_maker(txt, images, image_number)
        response = requests.post("http://34.72.254.112/fruits/", json=p)
        print(response.status_code)
        image_number+=1
        p = {}

if __name__ == "__main__":
    main()

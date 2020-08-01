#!/usr/bin/env python3
import os
import requests

PATH = 'C:\\Users\\OSCAR\\Desktop\\PythonIT\\final_projects\\module4\\Data'


def get_files():
    texts = []
    files = os.listdir(PATH)
    for file in files:
        if '.txt' in file:
            texts.append(file)
    return texts


def dic_maker(txt):
    path = PATH+'\\'+txt
    dictt = {}
    with open(path) as text:
        lines = text.readlines()
        dictt['name'] = lines[0].strip()
        dictt['weight'] = lines[1].strip()
        dictt['description'] = lines[2].strip()
        #dictt['image_name'] = lines[3].strip()
    return dictt


def main():
    files = get_files()
    print(files)
    for txt in files:
        p = dic_maker(txt)
        print(p)

    """
    for txt in files:
        p = dic_maker(txt)
        response = requests.post("http://34.66.47.98/feedback", data=p)
        print(response.status_code)
        p = {}
    """


if __name__ == "__main__":
    main()

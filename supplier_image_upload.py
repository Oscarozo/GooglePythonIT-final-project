#!/usr/bin/env python3
import requests

PATH = ''


def get_images():
    files = []
    for (root, path, filename) in os.walk('/home/student-00-b40cf9a1ca5d/images'):
        files.extend(filename)
    return files


images = get_images()
url = "http://localhost/upload/"
for img in images:
    full_img = PATH+'/'+img
    with open(full_img, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        print(r.status_code)

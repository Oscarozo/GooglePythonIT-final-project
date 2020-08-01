#!/usr/bin/env python3
import os
from PIL import Image


def get_images():
    files = []
    for (root, path, filename) in os.walk('/home/student-00-b40cf9a1ca5d/images'):
        files.extend(filename)
    return files


images = get_images()
for img in images:
    ini = '/home/student-00-b40cf9a1ca5d/images/'+img
    out = '/opt/icons/'+img
    with Image.open(ini) as im:
        newim = im.convert('RGB').resize((600, 400))
        newim.save(out, 'jpeg')

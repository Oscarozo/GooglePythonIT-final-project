#!/usr/bin/env python3
import reports
import datetime
import os
import run

files = run.get_files()
add_info = ''
for text in files:
    txt = run.PATH+'\\'+text
    with open(txt, 'r') as txt:
        add_info += 'name: '+txt.readline()
        add_info += 'weight: '+txt.readline()
    add_info += '\n'
print(add_info)

"""
time = datetime.datetime.now()
title = "Processed Update on "+time.strftime("%B")+" "+str(time.day)+", "+str(time.year)
"""

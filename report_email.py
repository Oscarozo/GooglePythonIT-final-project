#!/usr/bin/env python3
import reports
import datetime
import os
import run

time = datetime.datetime.now()
title = "Processed Update on "+time.strftime("%B")+" "+str(time.day)+", "+str(time.year)

files = run.get_files()
add_info = ''
for text in files:
    txt = run.PATH+'\\'+text
    with open(txt, 'r') as txt:
        add_info += 'name: '+txt.readline()+'<br/>'
        add_info += 'weight: '+txt.readline()+'<br/>'
    add_info += '<br/> <br/>'

reports.generate_report("C:\\Users\\OSCAR\\Desktop\\Processed.pdf", title, add_info)

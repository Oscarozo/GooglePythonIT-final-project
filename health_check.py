#!/usr/bin/env python3.8
import sys
import os
import shutil
import socket
import emails


def check_disk_usage(disk_name):  # checks if the available disk space is less than 20% percent
    disk_usage = shutil.disk_usage(disk_name)
    percentage = int((disk_usage.free/disk_usage.total)*100)
    if percentage < 20:
        return True
    else:
        return False


def check_no_network():
    """Returns True if it fails to resolve localhost to 127.0.0.1 URL"""
    try:
        socket.gethostbyname("localhost")
        return False
    except:
        return True


def check_cpu():  # checks if the cpu usage is over 80%
    if psutil.cpu_percent() > 80:
        return True
    else:
        return False


def check_memory():  # checks if the available memory is less than 500MB
    available_memory = psutil.virtual_memory().free >> 20  # gets the free space amount in MB
    if available_memory < 500:
        return True
    else:
        return False


def main():
    checks = [
        (check_disk_usage, "Error - Available disk space is less than 20%"),
        (check_cpu, "Error - CPU usage is over 80%"),
        (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1"),
        (check_memory, "Error - Available memory is less than 500MB")
    ]

    sender = 'automation@example.com'
    recipient = 'username@example.com'
    body = 'Please check your system and resolve the issue as soon as possible.'

    for check, msg in checks:
        if check():
            message = emails.generate_email(sender, recipient, msg, body, None)
            emails.send_email(message)


main()

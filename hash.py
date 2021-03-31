#!/usr/bin/python

#Lab 8
#Hash file that will recursively run through directories and files to hash. Some will be ignore.

import csv 
import datetime
import hashlib
import os 
import sys

list_ignore = ["/dev","/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]

path = '/'


if os.path.isfile("/var/www/html/hashinfo.csv"):
    print("Found Hashed File, will start comparing")
    f = open("hashinfo.csv", "r+")
    for line in f:
        newlist = f.readline()
        newlist2 = line.split(",")
        newlist3 = newlist2[1]
    for root, dirs, files in os.walk(path):
        if root in list_ignore:
            dirs[:] = []
            files[:] = [] 
        else:
            for x in files:
                current_file = os.path.join(root, x)
                hashlist = hashlib.sha256()
                hashlist2 = hashlist.hexdigest()
                time_date = str(datetime.datetime.now())
            if newlist3 != hashlist2:    
                f.write(current_file + ", ")
                f.write(hashlist.hexdigest() + ", ")
                f.write(time_date + "\n")
            else:
                continue
    f.close()
    print("Changes made in" + newlist + time_date + hashlist2)
    quit()
else:
    print("No file was found, creating file.")
    f = open("hashinfo.csv", "w")
    for root, dirs, files in os.walk(path):
        if root in list_ignore:
            dirs[:] = []
            files[:] = []
        else:
            for x in files:
                current_file = os.path.join(root, x)
                hashlist = hashlib.sha256()
                time_date = str(datetime.datetime.now())
        f.write(current_file + ", ")
        f.write(hashlist.hexdigest() + ", ")
        f.write(time_date +"\n")
    f.close()
    quit()


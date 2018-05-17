#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import download_file
import config
import sys


def task():
    details = download_file.get_filelist(config.Config.code)
    for i in range(len(details)):
        fileid = details[i]["id"]
        fileurl = details[i]["fileUrl"]
        filetype = details[i]["type"]
        wget_status = os.system("wget -P %s %s " %(config.Config.download_path,fileurl))
        if wget_status == 0:
            download_file.notify(config.Config.code,0,1,fileid)
        else:
            download_file.notify(config.Config.code,0,0,fileid)
            sys.exit()
        filename = details[i]["fileName"]
        notify_status = download_file.perform_file(filename,filetype)
        if notify_status == 1:
            download_file.notify(config.Config.code, 1, 1, fileid)
        else:
            download_file.notify(config.Config.code, 1, 0, fileid)
            sys.exit()
    p = os.system("sh tomcat_restart.sh")
    if p == 0:
        download_file.notify(config.Config.code,2,1,detailid="")
    else:
        download_file.notify(config.Config.code,2,0,detailid="")
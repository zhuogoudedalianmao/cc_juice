#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
import os

class Config():
    def __init__(self):
        super(Config, self).__init__()

    basedir = os.path.abspath(os.path.dirname(__file__))
    base_dir = '/'.join([basedir, "axinfu/upload"])

    code = "008"
    date_format_string = '%Y-%m-%d_%H-%M-%S'
    root_url = "http://192.168.0.96:8082/opd/sysc"
    get_project_url = "syncPerject"
    notify_url = "syncResult"
    mysql_user = "root"
    mysql_password = "Brhey9tp"
    mysql_host = "172.18.0.1"
    #mysql_file_name = "123.sql"
    bak_path = "/home/dalianmao/axinfu/bak"
    download_path = "/home/dalianmao/download"
    webapps_path = "/home/dalianmao/webapps"



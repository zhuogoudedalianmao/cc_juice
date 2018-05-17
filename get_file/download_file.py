#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import json
import os
from datetime import datetime
import requests
import config

def get_filetime(code):
    """
    获取部署时间
    :param code: 
    :return: 
    """
    try:
        filelist_url = "/".join([config.Config.root_url, config.Config.get_project_url])
        json_str = json.dumps({"code": code})
        params = {"json": json_str}
        r = requests.post(filelist_url, data=params)
        response = r.json()["result"]["strategy"]
        date = response["strategyValue"]
        return date
    except Exception:
        return None

def get_filelist(code):
    """
    获取需要部署的项目
    :return: 
    """
    try:
        filelist_url = "/".join([config.Config.root_url, config.Config.get_project_url])
        json_str = json.dumps({"code": code})
        params = {"json": json_str}
        r = requests.post(filelist_url, data=params)
        response = r.json()["result"]
        print response
        if response["code"] == code:
            details = response["details"]
            print "successful"
            return details
        else:
            #gen_log.error(u"学校编码不匹配，获取参数失败")
            return None
    except Exception:
        #gen_log.exception(u"获取项目失败")
        return None


def perform_file(filename,filetype):
    """
    文件更新策略
    :param strategy: 
    :param detail: 
    :return: 
    """
    try:
        if filetype == 1:
            war_path = "/".join([config.Config.download_path,filename])
            time = datetime.now().strftime(config.Config.date_format_string)
            bak_dir = "/".join([config.Config.bak_path,time])
            webapps_file_path = "/".join([config.Config.webapps_path,filename])
            if os.path.exists(webapps_file_path):
                print u"已有文件，备份替换！"
                cmd_war = "mkdir %s && mv %s %s && cp %s %s" % (
                    bak_dir, webapps_file_path, bak_dir,war_path, config.Config.webapps_path)
            else:
                print u"无文件，直接拷贝文件！"
                cmd_war = "cp %s %s" % (
                     war_path, config.Config.webapps_path)
            print cmd_war
            status = os.system(cmd_war)
            print status
            if status == 0:
                return 1
            else:
                return 0
        elif filetype == 2:
            sql_path = "/".join([config.Config.download_path,filename])
            cmd_sql = "mysql -u%s -p%s -P1433 -h'%s'< %s" % (
                config.Config.mysql_user, config.Config.mysql_password, config.Config.mysql_host, sql_path)
            status = os.system(cmd_sql)
            if status == 0:
                return 1
            else:
                return 0
        else:
            return 0
    except Exception as msg:
        print msg
        #return 0

def notify(code,type,status,detailid):
    """
    部署成功与否
    :param code: 
    :return: 
    """
    try:
        notify_url = "/".join([config.Config.root_url, config.Config.notify_url])
        json_str = json.dumps({"code":code, "type":type, "status":status, "detailid":detailid})
        params = {"json": json_str}
        requests.post(notify_url,data=params)
    except Exception:
        #gen_log.exception("部署异常")
        return False

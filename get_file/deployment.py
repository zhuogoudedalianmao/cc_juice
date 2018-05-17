#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler

import config
import download_file
from package import task


def Deployment():
    date = download_file.get_filetime(config.Config.code)
    print date
    if date == "1":
        task()
    else:
        print "时间不对"
        """
        sched = BlockingScheduler()
        sched.add_job(task,"date",run_date=date)
        sched.start()
        """
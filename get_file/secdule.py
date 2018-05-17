#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from deployment import Deployment

if __name__=="__main__":
    sched = BlockingScheduler()
    sched.add_job(Deployment,"cron",hour="*/1")#会返回一个date时间
    sched.start()

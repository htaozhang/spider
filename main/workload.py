#coding: utf-8

import time
import logging
from gevent.queue import Queue, Empty

class Workload:
    def __init__(self):
        self.timeout = 3
        self.__max_qsize = 1000
        self.__tasks = Queue(maxsize = self.__max_qsize)
        self.__status = []
        logging.debug("[Workload::__init__][ok]")
        pass

    def add_task(self, tasks):
        for task in tasks:
            if self.__tasks.qsize() >= self.__max_qsize:
                break
            self.__tasks.put(task)


    def get_task(self):
        # 向master请求任务
        tasks = []
        for task in tasks:
            self.__tasks.put(task)
            pass
        logging.debug("[Workload::get_task][ok]")
        return True

    
    def complete_task(self):
        # 向master反馈任务已完成的任务
        logging.debug("[Workload::complete_task][ok]")
        return True

    def get_one(self):
        if self.__tasks.qsize() <= 0:
            return None
        
        task = self.__tasks.get()
        logging.debug("[Workload::get_one][%s]" % task)
        return task

    def complete_one(self, task):
        status = {}
        self.__status.append(status)
        time.sleep(2)
        logging.debug("[Workload::complete_one][%s]" % task)
        return True



if __name__ == "__main__":
    logging.basicConfig(filename = None, level = logging.DEBUG)

    workload = Workload()
    
    workload.get_task()
    workload.add_task(["task1", "task2"])
    task = workload.get_one()
    workload.complete_one(task)
    workload.complete_task()




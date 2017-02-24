#coding: utf-8

import logging
import threading
import timer
import time
from slaveinfo import SlaveInfo

class Slave:
    def __init__(self, host, workers):
        #self.info = SlaveInfo()
        self.__host = host
        self.__timer = timer.Timer(10, self.heartbeat)
        self.__sem = threading.Semaphore()
        self.__workers = workers

    def run(self):
        self.__timer.start()
        self.__workers.start()

    def register(self):
        pass
    
    def heartbeat(self):
        pass

    def set_thread_num():
        pass

if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)

    from workload import Workload
    workload = Workload()
    workload.add_task(["task1", "task2", "tsak3", "task4"])

    def work(task):
        workload.complete_one(task)
        return True

    from workers import Workers
    workers = Workers(workload, work, 3, 40)

    slave = Slave("10.10.99.53", workers)
    slave.run()



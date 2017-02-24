#coding: utf-8

import time
import logging
import threading
from worker import Worker

class Workers:
    def __init__(self, workload, func, thread_num, coroutine_num):
        self.__workers = []
        self.__workload = workload
        self.__func = func
        self.__thread_num = thread_num
        self.__coroutine_num = coroutine_num
        self.__index = 0

        for i in range(self.__thread_num):
            self.add_worker()
            pass

        pass

    def run(self):
        #self.__workload.get()
        #self.__workload.add_task(["task" + str(i) for i in xrange(100)])
        pass
    
    def start(self):
        # 生产任务线程启动
        producter = threading.Thread(target = self.run, args = ())
        producter.start()

        # 消费任务线程组启动
        for worker in self.__workers:
            worker.start()
            pass
        pass

    def stop(self):
        for worker in self.__workers:
            worker.stop()
            pass

    def add_worker(self):
        self.__index += 1
        thread_name = "workload_thread_" + str(self.__index)
        worker = Worker(thread_name, self.__coroutine_num, self.__func, self.__workload)
        self.__workers.append(worker)
        return worker



if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)

    from workload import Workload
    workload = Workload()
    workload.add_task(["task" + str(i) for i in xrange(100)])

    def work(task):
        workload.complete_one(task)
        return True

    workers = Workers(workload, work, 3, 40)
    workers.start()

    time.sleep(5)
    workers.stop()





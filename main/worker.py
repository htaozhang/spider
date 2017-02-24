#coding: utf-8

import logging
import time
import threading
import gevent
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()

class Worker(threading.Thread):
    def __init__(self, name, coroutine_num, func, workload):
        self.__name = name
        self.__coroutine_num = coroutine_num
        self.__func = func
        self.__workload = workload
        self.__pool = Pool(coroutine_num + 1)
        self.__busy = False
        threading.Thread.__init__(self, None, None, self.__name, (), {})
        logging.debug("[Worker(%s)::__init__][ok]" % (self.__name))
        pass
    
    def entry(self, task):
        with gevent.Timeout(self.__workload.timeout):
            self.__func(task)
            pass
        pass

    def run(self):
        logging.debug("[Worker(%s) running]" % (self.__name))
        self.__busy = True

        while (self.__busy):
            task = self.__workload.get_one()
            
            if not task:
                time.sleep(1)
            elif self.__pool.full():
                time.sleep(1)
                #logging.debug("[Worker::run][at maxinum gevent.pool size]")
            else:
                self.__pool.spawn(self.entry, task)
                logging.debug("[Worer(%s)::run][get task: %s]" % (self.__name, task))
                time.sleep(0.1)
            pass
            
        self.__busy = False
        pass

    def is_busy(self):
        return self.__busy

    def stop(self):
        self.__busy = False
        time.sleep(0.5)
        logging.debug("[Worker::stop][ok]")

    

if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)

    from workload import Workload
    workload = Workload()
    workload.add_task(["task1", "task2", "task3"])

    def work(task):
        workload.complete_one(task)
        return True

    worker = Worker("test_worker", 5, work, workload)
    worker.start()

    time.sleep(3)
    worker.stop()





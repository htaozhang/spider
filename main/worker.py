#coding: utf-8

import logging
import time
import threading
import gevent
from gevent.pool import Pool


class Worker(threading.Thread):
    def __init__(self, name, coroutine_num, func, workload):
        self.__name = name
        self.__coroutine_num = coroutine_num
        self.__pool = Pool(coroutine_num)
        self.__func = func
        self.__workload = workload
        self.__busy = False
        threading.Thread.__init__(self, None, None, self.__name, (), {})
        logging.debug("[Worker::__init__][ok]")
        pass
    
    def entry(self):
        with gevent.Timeout(self.__workload.timeout):
            self.__func(task)
            pass
        logging.debug("[Worker::entry][ok]")
        pass

    def run(self):
        self.__busy = True

        while (self.__busy):
            task = self.__workload.get_one()
            if not task:
                time.sleep(1)
            elif self.__pool.full():
                logging.debug("[Worker::run][at maxinum gevent.pool size]")
            else:
                self.__pool.spawn(self.entry, task)
                pass
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

    worker = Worker("test_worker", 2, work, workload)
    worker.start()

    time.sleep(5)
    worker.stop()





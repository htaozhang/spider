#coding: utf-8

import gevent
from geven.pool import Pool


class Worker(threading.Thread):
    def __init__(self, name, coroutine_num, func, workload):
        self.__name = name
        self.__coroutine_num = coroutine_num
        self.__pool = Pool(coroutine_num)
        self.__func = func
        self.__workload = workload
        threading.Thread.__init__(self, None, None, self.__name, (), {})
        pass
    
    def entry(self):
        with gevent.Timeout(self.__workload.timeout):
            self.__func(task)
        pass

    def run(self):
        while (self.__busy):
            task = self.__workload.assign()
            self.__pool.spawn(self.entry, task)
            pass

        self.__busy = False
        pass

    def is_busy(self):
        return self.__busy

    def stop(self):
        self._busy = False
        time.sleep(0.5)




#coding: utf-8

import gevent
from geven.pool import Pool


class Worker(threading.Thread):
    def __init__(self, name, coroutine_num, func, workload):
        self.name = name
        self.coroutine_num = coroutine_num
        self.__pool = Pool(greent_num)
        self.__func = func
        self.workload = workload
        threading.Thread.__init__(self, None, None, self.name, (), {})

        pass
    
    def entry():
        with gevent.Timeout(self.workload.timeout):
            self.__func(task)

        pass

    def run(self):
        while (self.__busy):
            task = self.workload.get_workload()
            self.__pool.spawn(self.entry, task)
            pass

        self.__busy = False
        pass

    def is_busy():
        return self.__busy

    def stop():
        self._busy = False
        time.sleep(0.5)




#coding: utf-8


class Workers:
    def __init__(self, workload, func, thread_num, coroutine_num):
        self.__workers = []
        self.__workload = workload
        self.__func = func
        self.__thread_num = thread_num
        self.__coroutine_num = coroutine_name
        self.__index = 0

        for i in range(self.__thread_num):
            self.add_worker()
            pass

        pass

    def run():
        self.__workload.get()
        pass
    
    def start():
        for worker in self.__workers:
            worker.start()
            pass
        pass

    def stop():
        for worker in self.__workers:
            worker.stop()
            pass


    def add_worker():
        self.__index += 1
        worker = Worker(self, "work_thread_" + str(self.__index), self.__coroutine_num, self.__func, self.__workload)
        self.__workers.append(worker)
        return worker



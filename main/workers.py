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
        # 生产任务线程启动
        producter = Threading.Thread(target = self.run, args = ())
        producter.start()

        # 消费任务线程组启动
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
        thread_name = "workload_thread_" + str(self.__index)
        worker = Worker(self, thread_name, self.__coroutine_num, self.__func, self.__workload)
        self.__workers.append(worker)
        return worker



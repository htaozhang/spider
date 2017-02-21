#coding: utf-8


class Workers:
    def __init__(self, workload, func, thread_num, greent_num):
        self.__workers = []
        self.__greent_num
        self.__func
        self.__workload
        
        for i in range(thread_num):
            self.add_worker()

        pass

    def run():
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
        worker = Worker()
        self.__workers.append(worker)
        return worker


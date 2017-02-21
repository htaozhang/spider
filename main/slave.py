#coding: utf-8


class Slave:
    def __init__(self, self_host, port, master_host, workers):
        self.__server = http_server.HttpServer("0.0.0.0", port)
        self.__client
        self.__master_host
        self.info = SlaveInfo()
        self.info.server
        self.info.server_ip
        self.info.path
        
        self.__timer = timer.Timer()
        self.__sem = threading.Semaphore()
        self.__workers = workers

    def run(self):
        self.__timer.start()
        self.__workers.start()
        self.__server.run()

    def register(self):
        pass
    
    def heartbeat(self):
        pass

    def set_thread_num():
        pass



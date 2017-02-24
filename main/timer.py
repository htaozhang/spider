#coding: utf-8

import time
import threading

class Timer(threading.Thread):
    def __init__(self, seconds, func, **args):
        self.__seconds = seconds
        self.__func = func
        self.__args = args
        self.__running = True
        threading.Thread.__init__(self)
        pass

    def run(self):
        while self.__running:
            time.sleep(self.__seconds)
            self.__func(**self.__args)
            pass
        pass

    def stop(self):
        self.__running = False
        time.sleep(0.1)



if __name__ == "__main__":
    def func(s):
        print s

    timer = Timer(2, func, s = "hello")
    timer.start()

    time.sleep(5)
    timer.stop()



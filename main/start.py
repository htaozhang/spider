#coding: utf-8

from workers import Workers
from slave import Slave
from workload import Workload

def work(task):
    # working

    workload.complete_one(task)

    return


if __name__ == "__main__":
    # 读取配置

    # 设置代理

    # 实例化workload
    workload = Workload()

    # 实例化workers
    workers = Workers(workload, work, thread_num, coroutine_num)

    # 实例化slave
    slave = Slave(host, port, master_host, workers)

    # 启动slave
    slvae.run()



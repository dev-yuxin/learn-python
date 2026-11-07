import random
import time
from multiprocessing import Process


def write(output_file, count):
    with open(output_file, 'wt', encoding="utf-8") as f:
        print(f"{output_file}开始写入")
        for i in range(count):
            num = random.randint(0, 100)
            f.write(str(num) + "\n")
            time.sleep(1)
        print(f"{output_file}写入完成")


# 执行多进程需要在主进程中创建子进程
if __name__ == '__main__':
    print("主进程开始")

    # Process() 创建子进程对象，入参如下
    # group: 进程必须是None
    # target: 传入一个函数对象
    # args: 函数对象的可变位置参数，是个元组
    # kwargs: 函数对象的可变关键字参数，是个字典
    # name: 进程名，不传默认None，将自动分配名字
    # daemon: 是否是守护进程（不能独立存在，依赖别的进程，别的进程结束自己哪怕没执行完也结束），默认None，继承父进程
    p1 = Process(target=write, args=("assets/1.txt", 10))
    p2 = Process(target=write, args=("assets/2.txt", 5))

    # 启动子进程
    # 无法获得子进程的返回值，因为进程之间无法直接共享数据，需要用通信手段解决
    p1.start()
    p2.start()

    print("主进程结束")

import time
from multiprocessing import Process, current_process

nums = []


def add():
    global nums
    for i in range(10):
        nums.append(i)
        time.sleep(1)
    print(f"{current_process().name} nums={nums} 地址值={id(nums)}")


if __name__ == '__main__':
    p1 = Process(target=add, name="子进程1")
    p2 = Process(target=add, name="子进程2")

    p1.start()
    p2.start()

    for i in range(10):
        nums.append(i)
        time.sleep(1)
    print(f"主进程 nums={nums} 地址值={id(nums)}")

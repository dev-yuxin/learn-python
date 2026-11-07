import os
import time
from multiprocessing import Event, Process


def write(file, event):
    with open(file, "wt", encoding="utf-8") as f:
        print(f"写进程开始")
        for _ in range(10):
            f.write("hello world\n")
            f.flush()
            time.sleep(1)
        # 设置信号量
        event.set()
        print(f"写进程结束")


def read(file, event):
    while True:
        if os.path.isfile(file):
            break
        else:
            time.sleep(0.1)
    with open(file, "rt", encoding="utf-8") as f:
        print("读进程开始")
        while True:
            char = f.read(1)
            print(char, end="", flush=True)
            time.sleep(0.1)
            if not char and event.is_set():
                break
        print("读进程结束")


if __name__ == '__main__':
    # 当通信比较简单时，使用信号量通信
    # 一个进程 event.set() 设置信号量
    # 另一个进程 event.is_set() 判断信号量是否已设置
    event = Event()
    p1 = Process(target=read, args=("assets/a.txt", event))
    p2 = Process(target=write, args=("assets/a.txt", event))
    p1.start()
    p2.start()

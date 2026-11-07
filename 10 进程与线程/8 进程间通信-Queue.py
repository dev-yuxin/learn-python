import random
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager


def put(count, queue):
    for _ in range(count):
        num = random.randint(1, 100)
        queue.put(num)
        print(f"存进程放入：{num}")
        time.sleep(1)
    queue.put(None)


def get(count: int, queue):
    for _ in range(count):
        num = queue.get()
        print(f"取进程取出：{num}")


if __name__ == '__main__':
    # 队列：队尾放，队头取
    # Manager().Queue() 可以兼容进程池
    # 进程队列 get() 操作如果队列为空会阻塞，等到有元素了再取出
    # 多进程中的队列判断是否为空是不准确的，只能通过特殊元素来区分是否结束
    queue = Manager().Queue()
    pool = ProcessPoolExecutor(max_workers=2)
    f1 = pool.submit(put, 10, queue)
    f2 = pool.submit(get, 5, queue)

    # 等f2取完，主进程再取
    f2.result()
    print("主进程取剩余的数")

    while True:
        num = queue.get()
        if num is None:
            break
        print(f"主进程取出：{num}")

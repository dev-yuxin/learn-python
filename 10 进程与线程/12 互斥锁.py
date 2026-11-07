import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, Lock

total_ticket = 100


def sell_ticket(lock: Lock):
    global total_ticket
    while True:
        # 注意锁加的位置
        # 1 只能限制本次操作，不能扩大到 while 以外，这样让一个线程一直占据
        # 2 判断 total_ticket 前就要加锁，不管进入哪个分支还是发生异常最后都要释放锁
        try:
            lock.acquire()
            if total_ticket > 0:
                time.sleep(0.1)
                print(f"{current_thread().name}卖了第{total_ticket}张票")
                total_ticket -= 1
            else:
                break
        finally:
            lock.release()


if __name__ == "__main__":
    # 互斥锁
    lock = Lock()
    pool = ThreadPoolExecutor(3)
    pool.map(sell_ticket, [lock for _ in range(3)])

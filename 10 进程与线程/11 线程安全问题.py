import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

# 线程之间可以直接共享数据，不需要通信
# 但是会引发线程安全问题：多个线程，有共享数据，有写操作就会有线程安全问题
total_ticket = 100


def sell_ticket():
    global total_ticket
    while total_ticket > 0:
        time.sleep(0.1)
        print(f"{current_thread().name}卖了第{total_ticket}张票")
        total_ticket -= 1


if __name__ == "__main__":
    pool = ThreadPoolExecutor(3)
    # 注意，函数无参形式提交多个任务的方式
    # 也可以把 sell_ticker() 加入可变位置参数
    pool.map(lambda _: sell_ticket(), range(3))

import random
import time
from multiprocessing import Pipe, Process


def put_num_get_letter(con):
    for _ in range(10):
        num = random.randint(1, 100)
        con.send(num)
        print(f"进程1存放: {num}")
        char = con.recv()
        print(f"进程1取: {char}")
        time.sleep(1)


def put_letter_get_num(con):
    for _ in range(10):
        char = chr(random.randint(97, 122))
        con.send(char)
        print(f"进程2存放: {char}")
        num = con.recv()
        print(f"进程2取: {num}")
        time.sleep(0.5)


if __name__ == "__main__":
    # Pipe 创建一个管道，返回2个端口 con1,con2
    # 进程1通过con1读和写，进程2通过con2读和写
    # con.send(val) 存
    # con.recv() 取，如果管道为空会阻塞，等到有结果再取
    con1, con2 = Pipe()
    p1 = Process(target=put_num_get_letter, args=(con1,))
    p2 = Process(target=put_letter_get_num, args=(con2,))
    p1.start()
    p2.start()

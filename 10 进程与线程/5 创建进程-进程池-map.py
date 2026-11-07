import random
import time
from concurrent.futures import ProcessPoolExecutor


def write(output_file, count):
    with open(output_file, 'wt', encoding="utf-8") as f:
        nums = []
        print(f"{output_file}开始写入")
        for i in range(count):
            num = random.randint(0, 100)
            nums.append(num)
            f.write(str(num) + "\n")
            time.sleep(1)
        print(f"{output_file}写入完成")
    return nums


if __name__ == '__main__':
    print("主进程开始")

    # 创建一个进程池，最多10个进程
    pool = ProcessPoolExecutor(10)

    # map() 一次提交n个任务，并启动n个子进程
    # 第一个参数：任务函数 fn
    # 第二个参数：把多个 fn 的入参组成可变位置参数，它的长度会决定提交几个任务
    # 第三个参数：超时时间，对所有任务都生效
    # 返回值是一个可迭代对象，遍历这个可迭代对象会阻塞（设置超时时间以超时时间为准，没设置则要等所有任务执行完）
    #   如果都未发生超时，那么把函数执行结果依照传参顺序放入（不管谁先完成谁后完成）
    #   如果某个任务发生超时，主进程抛出异常，但不影响子进程
    result_iter = pool.map(write, ("assets/1.txt", "assets/2.txt", "assets/3.txt"), (5, 10, 1), timeout=6)

    try:
        i = 0
        for result in result_iter:
            print(f"任务{i + 1}结果", result)
            i += 1
    except TimeoutError as e:
        print(f"任务{i + 1}超时")

    print("主进程结束")

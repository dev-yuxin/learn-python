import random
import time
from concurrent.futures import as_completed, ProcessPoolExecutor


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


def f3_callback(future):
    print("任务3结果：", future.result())


if __name__ == '__main__':
    print("主进程开始")

    pool = ProcessPoolExecutor(10)
    # 单个提交任务，并创建子进程，返回一个 Future 对象
    f1 = pool.submit(write, "assets/1.txt", 5)
    f2 = pool.submit(write, "assets/2.txt", 10)
    f3 = pool.submit(write, "assets/3.txt", 1)

    # 单独给f3添加回调函数，当f3执行完后会自动执行回调函数
    f3.add_done_callback(f3_callback)

    # future.result() 会阻塞主进程，必须得要拿到结果才继续执行后面代码
    result1 = f1.result()
    print(f"任务1结果：", result1)

    # future.result() 可以设置超时时间，超时主进程抛异常得不到结果，但不影响子进程
    try:
        result2 = f2.result(3)
        print(f"任务2结果：", result2)
    except TimeoutError as e:
        print("任务2超时")

    # as_completed() 传入一个元素都是future的可迭代对象，可以按照完成的先后顺序遍历，同样会阻塞主进程
    f4 = pool.submit(write, "assets/4.txt", 3)
    f5 = pool.submit(write, "assets/5.txt", 2)
    for f in as_completed([f4, f5]):
        print(f.result())

    print("主进程结束")

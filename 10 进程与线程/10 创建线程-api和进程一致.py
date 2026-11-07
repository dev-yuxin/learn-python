import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def write(output_file, count):
    with open(output_file, 'wt', encoding="utf-8") as f:
        print(f"{output_file}开始写入")
        nums = []
        for i in range(count):
            num = random.randint(0, 100)
            f.write(str(num) + "\n")
            nums.append(num)
            time.sleep(1)
        print(f"{output_file}写入完成")
    return nums


class MyThread(Thread):
    def __init__(self, output_file, count):
        Thread.__init__(self)
        self.output_file = output_file
        self.count = count

    def run(self):
        with open(self.output_file, 'wt', encoding="utf-8") as f:
            print(f"{self.output_file}开始写入")
            nums = []
            for i in range(self.count):
                num = random.randint(0, 100)
                f.write(str(num) + "\n")
                nums.append(num)
                time.sleep(1)
            print(f"{self.output_file}写入完成")
        return nums


if __name__ == '__main__':
    print("主线程开始")

    t1 = Thread(target=write, args=("assets/1.txt", 10))
    t2 = MyThread("assets/2.txt", 5)
    pool = ThreadPoolExecutor(max_workers=3)
    t1.start()
    t2.start()
    f3 = pool.submit(write, "assets/3.txt", 4)
    result_iter = pool.map(write, ("assets/4.txt", "assets/5.txt"), (3, 2))

    print(f3.result())
    for result in result_iter:
        print(result)

    print("主线程结束")

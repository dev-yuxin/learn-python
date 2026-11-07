import random
import time
from multiprocessing import Process


# 继承 Process 类并重写 run 方法
class MyProcess(Process):
    # 如果带参数，则参数在 __init__ 中初始化
    # 如果重写了 __init__ 方法，需要手动调用父类 __init__ 方法。如果没有重写，那么会根据 MRO 自动调用父类的 __init__

    def __init__(self, output_file, count):
        Process.__init__(self)
        self.output_file = output_file
        self.count = count

    # 重写 run 方法
    def run(self):
        with open(self.output_file, 'wt', encoding="utf-8") as f:
            print(f"{self.output_file}开始写入")
            for i in range(self.count):
                num = random.randint(0, 100)
                f.write(str(num) + "\n")
                time.sleep(1)
            print(f"{self.output_file}写入完成")


if __name__ == '__main__':
    print("主进程开始")

    # 创建子进程
    p1 = MyProcess("assets/1.txt", 10)
    p2 = MyProcess("assets/2.txt", 5)

    # 启动子进程
    p1.start()
    p2.start()

    print("主进程结束")

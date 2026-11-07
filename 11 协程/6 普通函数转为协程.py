import asyncio
import time


async def f(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


# 普通的同步函数
def f2(name, delay):
    print(f"{name} start")
    time.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


async def main():
    # 普通函数无法直接变为协程对象，必须开一个新的线程执行，然后再创建一个协程对象来控制这个线程
    task_a = asyncio.to_thread(f2, "任务A", 3)
    task_b = asyncio.create_task(f("任务B", 2))
    results = await asyncio.gather(task_a, task_b)
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())

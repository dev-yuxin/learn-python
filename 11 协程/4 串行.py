import asyncio


async def f(name, delay):
    print(f"{name} start")
    # time.sleep() 是同步代码，由操作系统调用，会阻塞当前线程，包括事件循环。
    # asyncio.sleep() 是异步代码，返回一个协程对象，由程序调用，只阻塞当前协程，不会阻塞整个事件循环。
    await asyncio.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


async def main():
    result_a = await f("任务A", 3)
    result_b = await f("任务B", 2)
    print(result_a, result_b)


if __name__ == '__main__':
    # 1 main 加入事件循环
    # 2 执行到14行，a进入事件循环就绪队列，main进入IO队列，main必须等a执行完毕
    # 3 执行a，执行到第8行，a的sleep进入事件循环就绪队列，a进入IO队列（此时IO队列里有a和main，a要等a的sleep，main要等a）
    # 4 a的sleep执行完
    # 5 IO队列里取出a（此时IO队列还剩main）放入就绪队列（就绪队列里只有a的剩余部分）
    # 6 执行完a的剩余部分
    # 7 IO队列里取出main放入就绪队列
    # 8 继续执行main执行到第15行，b的操作同a一样
    # ...
    # 9 执行完b的剩余部分
    # 10 IO队列里取出main放入就绪队列
    # 11 执行完main的剩余部分
    asyncio.run(main())

import asyncio


async def f(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


async def main():
    # create_task() 将返回任务对象，同时会放入事件循环
    # 任务对象是Future对象的子类，它内部包装了一个协程，并且已加入事件循环
    task_a = asyncio.create_task(f("任务A", 3))
    task_b = asyncio.create_task(f("任务B", 2))
    # 如果不加后面的代码，主协程结束就全部结束了
    # await asyncio.gather() 传入可等待对象（Future/任务/协程对象），用于获取结果，会阻塞当前协程
    results = await asyncio.gather(task_a, task_b)
    for result in results:
        print(result)


if __name__ == '__main__':
    # 1 main 协程进入就绪队列并执行
    # 2 执行到第13行，task_a 协程进入就绪队列（下一轮事件循环task_a会被执行），继续执行
    # 3 执行到第14行，task_b 协程进入就绪队列（下一轮事件循环task_b会被执行），继续执行
    # 4 下一轮事件循环时 main, task_a, task_b 在并发执行
    # 5 执行到第17行，main 协程进入IO队列需要等 task_a, task_b 执行完毕
    # 5 等 task_b 先执行完，task_a 再执行完，main 从IO队列取出放入就绪队列，然后取出执行剩余代码
    asyncio.run(main())

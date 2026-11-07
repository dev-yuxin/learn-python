import asyncio


async def f(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")
    return f"{name} result"


async def main1():
    max_time = 4
    # wait_for() 可以设置超时，返回协程对象
    coro_a = asyncio.wait_for(f("任务A", 5), timeout=max_time)
    coro_b = asyncio.wait_for(f("任务B", 3), timeout=max_time)
    # await 会把协程对象放入事件循环执行。
    # 如果超时不设置return_exceptions会抛异常，设置了return_exceptions 则不抛异常把异常对象放入列表
    results = await asyncio.gather(coro_a, coro_b, return_exceptions=True)
    for result in results:
        print(result, type(result))


async def main2():
    max_time = 4
    task_a = asyncio.create_task(f("任务A", 5))
    task_b = asyncio.create_task(f("任务B", 3))
    # 主协程最多等待4s后手动取消，如果没有执行完，就会抛异常
    await asyncio.sleep(max_time)
    task_a.cancel()
    task_b.cancel()
    results = await asyncio.gather(task_a, task_b, return_exceptions=True)
    for result in results:
        print(result, type(result))


if __name__ == '__main__':
    asyncio.run(main1())
    asyncio.run(main2())

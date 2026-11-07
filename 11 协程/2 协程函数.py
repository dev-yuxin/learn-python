import asyncio


# 使用 async 关键字定义一个协程函数
async def f():
    print('hello world')


# 调用协程函数后，不会执行函数体，而是返回一个协程对象
# 协程对象就是一段还没放入事件循环执行的异步代码
coro_obj = f()
print(type(coro_obj))

if __name__ == '__main__':
    # 真正放入事件循环，并执行函数体代码
    asyncio.run(coro_obj)

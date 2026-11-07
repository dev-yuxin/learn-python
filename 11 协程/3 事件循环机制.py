# 哪些方式可以加入事件循环？
# asyncio.run(main_coro) 主协程，当主协程结束则不管其他，全部结束
# await 协程对象 会阻塞，必须等后面代码执行完毕才能继续执行（await必须配合async使用，await后面必须是协程对象）
# asyncio.create_task(coro) 不会阻塞，如果想拿结果需使用 await asyncio.gather()

# 1 先检查 IO 队列，把完成 IO 的放入就绪队列
# 2 从就绪队列中取出任务执行
#   2.1 一种情况是直接完成
#   2.2 另一种情况是又遇到了 await，再放回 IO 队列
# 3 所有任务都完成了就结束，否则循环执行1和2
# 内置的 list 是连续的数组结构。
# 而 deque（双端队列）是分块的双向链表结构。在增加删除队头元素时性能更好。
from collections import deque
# heapq 是优先队列，又或者叫最小堆
import heapq

# 初始化一个双端队列
dq = deque([1, 2, 3])
# 队尾加入元素
dq.append(4)
print(dq)
# 队头加入元素
dq.appendleft(0)
print(dq)
# 取队头队尾元素（不出队）
print(dq[0], dq[-1])
# 队头出队
item = dq.popleft()
print(item, dq)
# 队尾出队
item = dq.pop()
print(item, dq)
# 队列是否空
print(len(dq) == 0)

nums = [7, 9, 6, 1, 7, 3, 6]
# 建最小堆（就地操作）
heapq.heapify(nums)
print(nums)
# 插入元素（就地操作）
heapq.heappush(nums, 4)
print(nums)
# 查看堆顶元素（不出堆）
print(nums[0])
# 查看最小/最大的n个元素（不出堆）
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums))
# 弹出堆顶元素（就地操作）
while len(nums):
    item = heapq.heappop(nums)
    print(item, nums)

# 如何实现最大堆呢
nums = [7, 9, 6, 1, 7, 3, 6]
# 存一个 (-val, val) 的元组，会根据元组第 0 位去比较，第0位相同比较第1位, ... （堆排序是不稳定的）
_nums = [(-val, val) for val in nums]
heapq.heapify(_nums)
while _nums:
    _, val = heapq.heappop(_nums)
    print(val, [item[1] for item in _nums])

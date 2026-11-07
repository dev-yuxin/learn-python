import heapq
from functools import reduce


# 匿名函数作为返回值
def calculate(sign):
    match sign:
        case "-":
            return lambda a, b: a - b
        case "*":
            return lambda a, b: a * b
        case "/":
            return lambda a, b: a / b
        case _:
            return lambda a, b: a + b


print(calculate("+")(1, 2))

# 一些内置函数，使用匿名函数作为参数
list1 = [1, -2, 3, 4, 5, -2]
list2 = [{"name": "张三", "salary": 10000}, {"name": "李四"}, {"name": "王五", "salary": 9000},
         {"name": "赵六", "salary": 20000}]

# reduce() 归并
# 求和，如果不指定初始值则以第0个元素为初始值，从第1个元素开始归并
print(reduce(lambda x, y: x + y, list1))
# 求各元素绝对值的和，如果指定初始值则以初始值为准，从第0个元素开始归并
print(reduce(lambda x, y: x + abs(y), list1, 0))
# 求工资总和
print(reduce(lambda x, y: x + y.get("salary", 0), list2, 0))
# 求薪资最大值
print(reduce(lambda x, y: max(x, y.get("salary", 0)), list2, 0))
print(max(list2, key=lambda x: x.get("salary", 0)))

# heapq.nlargest(), heapq.nsmallest
# 找出最小的3个数
print(heapq.nsmallest(3, list1))
# 找出工资最高的2个员工
print(heapq.nlargest(2, list2, key=lambda x: x.get("salary", 0)))

# sorted()
# 按薪资从高到低排序
print(sorted(list2, reverse=True, key=lambda x: x.get("salary", 0)))

# map()
# 把 list1 每个数转为绝对值
print(list(map(lambda x: abs(x), list1)))

# filter()
# 筛选出薪资>=10000的员工
print(list(filter(lambda x: x.get("salary", 0) >= 10000, list2)))

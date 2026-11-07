list1 = [10, 20, 10, 30, 20, 0]

# 就地升序排序
list1.sort()
print(list1)

# 就地降序排序
list1.sort(reverse=True)
print(list1)

list2 = ["hello", "world", "java", "python", "llm"]
# 字符串默认按字典序升序
list2.sort()
print(list2)
# 指定比较规则按照 len(item) 降序
list2.sort(key=len, reverse=True)
print(list2)

# sorted() 返回一个新序列，不改变传入的序列
list1 = [10, 20, 10, 30, 20, 0]
list2 = sorted(list1)
print(list1)
print(list2)

list1 = [1, 2, 3, 4, 5]
# 就地逆置
list1.reverse()
print(list1)
# 利用切片返回一个逆置后的新列表，不改变原列表
list2 = list1[::-1]
print(list1)
print(list2)

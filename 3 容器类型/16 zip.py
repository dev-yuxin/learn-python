list1 = [1, 2, 3]
list2 = ["一", "二", "三", "四"]
list3 = ["first", "second"]

# zip() 得到的是一个 zip 对象（也是可迭代对象）
# 传入3个容器，每个元素就是一个3元组
# 长度取所有容器的最小值，超出部分截掉
zipped = zip(list1, list2, list3)
for item1, item2, item3 in zipped:
    print(item1, item2, item3)

# 可以直接把 zip 对象传入 dict()
dict1 = dict(zip(list1, list2))
print(dict1)

# 可变与不可变：元素创建好后，元素个数、元素值是否可以被修改
# 可变容器支持增、删、改、查、遍历操作
# 不可变容器只支持查和遍历
# 有序和无序：能不能通数字索引和切片来操作元素

# 容器    是否可变    是否有序    元素是否可重复
# list      是       是           是
# tuple     否       是           是
# str       否       是           是
# set       是       否           否
# dict      是       否           键唯一，值可以重复

# 所有容器都支持的操作
# in
print(1 in [1, 2, 3])
print("ll" in "hello")
# len()
print(len([1, 2, 3]))
# max(), min() 要求元素可比较
print(max([1, 2, 3]))
print(min("abc"))
# sum() 要求元素可求和
print(sum([1, 2, 3]))
# 遍历操作，容器都是可迭代对象
for item in [1, 2, 3, 4, 5]:
    print(item, end=" ")
else:
    print()

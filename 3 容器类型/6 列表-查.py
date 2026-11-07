list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 20]

# 查询元素出现的索引
# 默认从索引 0 往右查返回首次出现的索引，也可以指定开始索引
# 如果不存在则报错
print(list1.index(20))
print(list1.index(20, 2))
if -10 in list1:
    print(list1.index(10))
else:
    print("-10不在列表中")

# 统计元素出现个数
print(list1.count(20))

# 索引
# 正索引：从 0 到 length -1
# 负索引：从 -1（最后一个）到 -length
# 越界报错
print(list1[2])
print(list1[-2])

# 切片
# [start:end:step]
# 从 start（包含start） 到 end（不包含end），步长为 step
# start 表示起始值，如果省略则根据 step 方向确定，从左向右则为最左，从右向左则为最右
# end 表示终止值，如果省略根据 step 方向确定，从左向右则为最右，从右向左则为最左
# step 表示步长，如果省略默认为 1，表示从左往右步长为 1。如果是负数则从右往左
# 从索引 1（包含） 到 -1（不包含），步长为2
print(list1[1:-1:2])
# 前 5 个
print(list1[:5])
# 最后 5 个
print(list1[-5:])
# 最后 4 个取反
print(list1[:-5:-1])
# 复制
print(list1[:])
# 列表取反
print(list1[::-1])

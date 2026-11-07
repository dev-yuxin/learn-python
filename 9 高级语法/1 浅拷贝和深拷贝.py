from copy import copy, deepcopy

# 直接赋值（list1和list2指向同一个对象）
list1 = [1, 2, [3]]
list2 = list1
list1[0] = 10
print(list1)
print(list2)

# 浅拷贝（只拷贝最外层地址值）
list1 = [1, 2, [3]]
# list1[:], list(list1) 也是浅拷贝
list2 = copy(list1)
list2[0] = 10
list2[2][0] = 30
print(list1)
print(list2)

# 深拷贝（每一层都拷贝）
list1 = [1, 2, [3]]
list2 = deepcopy(list1)
list2[0] = 10
list2[2][0] = 30
print(list1)
print(list2)

# 不可变对象即使调用 copy() 或 deepcopy() 还是赋值操作

# tuple1 和 tuple2 指向不同对象
# tuple1[0] 和 tuple2[0] 指向相同对象
# tuple1[1] 和 tuple2[1] 指向不同对象
tuple1 = (1, [2])
tuple2 = deepcopy(tuple1)
print(tuple1 is tuple2, tuple1[0] is tuple2[0], tuple1[1] is tuple2[1])

# tuple1 和 tuple2 以及里面的每一个元素都指向相同对象
tuple1 = (1, (2,))
tuple2 = deepcopy(tuple1)
print(tuple1 is tuple2, tuple1[0] is tuple2[0], tuple1[1] is tuple2[1])

# list1 和 list2 指向不同对象
# list1 和 list2 里面的每个元素都指向相同对象
list1 = [1, (2,)]
list2 = deepcopy(list1)
print(list1 is list2, list1[0] is list2[0], list1[1] is list2[1])

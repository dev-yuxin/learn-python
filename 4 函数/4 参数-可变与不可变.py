# 当函数传入不可变类型参数时，形参操作不影响实参
# 当函数传入可变类型参数时，如果形参的操作是就地更新，形参操作会影响实参
#                      如果形参的操作是指向新对象，形参操作不影响实参
def swap(a, b):
    a, b = b, a


# 列表去重，返回新列表
def remove_same(nums):
    return list(set(nums))


# 列表就地去重
def remove_same_updated(nums):
    _set = set()
    i = 0
    while i < len(nums):
        if nums[i] not in _set:
            _set.add(nums[i])
            i += 1
        else:
            del nums[i]


a = 1
b = 2
swap(a, b)
print(a, b)

nums = [1, 2, 2, 2, 3, 1]
new_nums = remove_same(nums)
print(nums, new_nums)

remove_same_updated(nums)
print(nums)

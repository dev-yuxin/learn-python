# 字典是存储键值对的
# 可变：可以增删键值对，改只能改value不能改key。key用不可变对象，如 int,str,tuple 等
# 无序，不能用数字索引和切片
# key不能重复，value可以

# 字面量创建字典
dict1 = {"name": "tom", "age": 18}
print(dict1)

# 创建空字典
dict1 = {}
dict2 = dict()
print(dict1)
print(dict2)

# dict() 传入其它可迭代对象，元素是二元组
dict1 = dict([("name", "tom"), ("age", 18)])
print(dict1)

# dict() 关键字传参
dict1 = dict(name="tom", age=18)
print(dict1)

# 字典推导式
# 找出所有出现次数>1的字母
str1 = "hello world"
dict1 = {letter: str1.count(letter) for letter in str1 if str1.count(letter) > 1}
print(dict1)

# 集合添加/修改键值对
# 键不存在是添加，键已存在是修改
dict1 = {}
dict1["name"] = "tom"
dict1["age"] = 18
dict1["age"] = 19
print(dict1)

# 删除键值对（删除时key必须存在，否则报错）
dict1 = {"name": "tom", "age": 18, "city": "beijing", "salary": 10000}
del dict1["age"]
print(dict1)
# 删除并返回值
city_val = dict1.pop("city")
print(city_val, dict1)
# 清空
dict1.clear()
print(dict1)

# 查
dict1 = {"name": "tom", "age": 18, "city": "beijing", "salary": 10000}
# in 判断的是 key 是否在 dict 中
print("name" in dict1)
print("tom" in dict1)
# 根据键获取值
# 直接使用[] key 不存在会报错
# get() key 不存在会返回兜底值，默认None
print(dict1["name"])
print(dict1.get("phone"))
print(dict1.get("gender", "male"))

# 遍历
dict1 = {"name": "tom", "age": 18, "city": "beijing", "salary": 10000}
# for in 拿到的是 key
for key in dict1:
    print(key, end=" ")
else:
    print()
# 也可以使用 keys() 获取键组成的列表
for key in dict1.keys():
    print(key, end=" ")
else:
    print()
# 使用 values 获取值组成的列表
for value in dict1.values():
    print(value, end=" ")
else:
    print()
# 使用 items 获取 (key,value)二元组组成的列表
for key, value in dict1.items():
    print(key, value)

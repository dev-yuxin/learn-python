# 形参，函数定义时的参数，内存不会开辟空间，只有函数调用时才接收实参传入的值
def print_person(name, age, gender, city):
    print(f"{name=}, {age=}, {gender=}, {city=}")


# 实参，函数调用时传入的值
# 位置参数，要求实参和形参位置一一对应，不能多不能少
print_person("张三", 18, "男", "北京")
# 关键字参数，要求实参关键字和形参名一一对应，位置无所谓
print_person(name="张三", age=18, city="北京", gender="男")
# 位置和关键字参数混用，要求关键字参数必须在位置参数后面
print_person("张三", 18, city="北京", gender="男")


# python 没有函数重载，同名直接覆盖原函数
# / 前面必须用位置参数，* 后面必须用关键字参数，之间则都可以
def print_person(name, age, /, gender, *, city):
    print(f"{name=}, {age=}, {gender=}, {city=}")


print_person("张三", 18, "男", city="北京")
print_person("张三", 18, gender="男", city="北京")


# 形参带默认值，必须放在普通形参后面
def print_person(name, age, gender="男", city="北京"):
    print(f"{name=}, {age=}, {gender=}, {city=}")


# 实参传了默认值，使用传的值，不传则使用默认值
print_person("张三", 18, gender="女")


# 形参 *args 可变位置参数，接收0~n个位置参数，args是一个元组
# 实参传入 *列表/元组/字符串等 将解包为位置参数
def print_person(name, age, *hobbies):
    print(f"{name=}, {age=}, {hobbies=}")


print_person("张三", 18, "唱", "跳", "篮球")
print_person("张三", 18, *["唱", "跳", "篮球"])


# 形参 **kwargs 可变关键字参数，接收0~n个关键字参数，kwargs是一个字典
# 实参传入 **字典 将解包为关键字参数
def print_person(name, age, **kwargs):
    print(f"{name=}, {age=}, {kwargs=}")


print_person("张三", 18, gender="男", city="北京")
print_person("张三", 18, **{"gender": "男", "city": "北京"})


# 形参顺序
# def func(普通位置参数, 带默认值的位置参数, *args, 普通关键字参数, 带默认值的关键字参数, **kwargs):
def print_person(name, age, gender="男", *hobbies, city, email=None, **others):
    print(f"{name=},{age=}, {gender=}, {hobbies=}, {city=}, {email=}, {others=}")


# 实参顺序
# 关键字参数永远在位置参数后面
print_person("张三", 18, city="北京", job="llm工程师")

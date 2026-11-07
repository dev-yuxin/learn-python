class Person:
    # 实例方法里有一类特殊的方法称为魔法方法
    # 命名时使用 __方法名__
    # 我们一般不会主动去调用，而是在一些特殊操作的时候，底层自动帮我们调用

    # 在创建对象时，Person("张三", 18) 底层
    # 先自动调用 __new__ 在内存里创建一个对象，这个方法我们一般不用去重写
    # 再调用 __init__ 初始化方法去初始化实例属性，这个方法需要我们去重写
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当调用 str() 时，底层会自动调用
    # 先看有没有 __str__ 方法（面向用户）
    # 再看 __repr__ 方法（面向开发者）
    # 都没有输出地址值
    # 比如 print(xxx) 就会自动调用 str() 去转字符串
    # 如果 xxx 是容器类型，又会对每个元素去调用 __repr__ 方法
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}"

    def __repr__(self):
        return str({
            "name": self.name,
            "age": self.age
        })

    # 比较大小，==, !=, <, >, <=, >= 底层会调用以下魔法方法
    # __eq__ => ==, != 。如果有 __ne__ 则 != 会优先调用 __ne__
    # __lt__ => <, > 。如果有 __gt__ 则 > 会优先调用 __gt__
    # __le__ => <=, >= 。如果有 __ge__ 则 >= 会优先调用 __ge__
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age


p1 = Person("张三", 18)
p2 = Person("李四", 20)
p3 = Person("张三", 18)

print(p1)
print([p1, p2])
print(p1 == p3)
print(p1 < p2)
print(p1 <= p2)

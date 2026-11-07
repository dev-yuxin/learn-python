# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def happy_birthday(self):
        self.age += 1
        print(f"祝{self.name}生日快乐")


# 创建对象
p1 = Person("张三", 18)
p1.happy_birthday()

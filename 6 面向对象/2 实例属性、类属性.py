class Person:
    # 类属性
    # 变量直接定义在类中
    # 类加载时完会存储到一个字典：类.__dict__，key是属性名，value是属性值（复杂对象是地址值），被类所有对象共享
    # 访问方式：类名.类属性名
    home = "earth"

    def __init__(self, name, age):
        # 实例属性
        # 变量定义在初始化实例方法中，一般是 __init__ 中
        # 实例化对象时会存储到一个字典：对象.__dict__，key是属性名，value是属性值（复杂对象是地址值），每一个对象独享
        # 访问方式：对象.实例属性，不推荐使用：对象.类属性，可能被同名覆盖
        self.name = name
        self.age = age


p1 = Person("张三", 18)
p2 = Person("李四", 20)

# 访问实例属性和类属性
print(p1.name, p1.age, Person.home, p1.home)
print(p2.name, p2.age, Person.home, p2.home)

# 修改实例属性，只影响自己
p1.age += 1
print(p1.name, p1.age, p1.home, Person.home)
print(p2.name, p2.age, p2.home, Person.home)

# 修改类属性（影响所有对象）
Person.home = "火星"
print(p1.name, p1.age, p1.home, Person.home)
print(p2.name, p2.age, p2.home, Person.home)

# 注意，这不是修改类属性，而是动态给 p1 添加一个 home 实例属性
p1.home = "地球"
print(p1.name, p1.age, p1.home, Person.home)
print(p2.name, p2.age, p2.home, Person.home)

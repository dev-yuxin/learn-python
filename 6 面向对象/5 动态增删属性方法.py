import types


class Person:
    # 限定了 Person 类可以有哪些实例属性，不在范围里的实例属性会报错
    # 不限制 类属性、类方法、静态方法、实例方法，但不允许和实例属性同名
    # 只对该类生效，不对子类生效
    __slots__ = ("name", "age", "sleep")


# 方法可以写到类外面（但不推荐）
def eat(self):
    print(f"{self.name}在吃饭")


def sleep(self):
    print(f"{self.name}在睡觉")


@classmethod
def greet(cls):
    print(f"你好，{cls.home}人")


@staticmethod
def add(a, b):
    return a + b


# 增加类成员（类属性、类方法、静态方法）
Person.home = "地球"
Person.greet = greet
Person.add = add
Person.greet()
print(Person.add(1, 2))
# 删除类成员（类属性、类方法、静态方法）
del Person.home
del Person.greet
del Person.add

p1 = Person()
p2 = Person()

# 给单个对象增加实例属性
p1.name = "张三"
p1.age = 20
p2.name = "李四"
# 删除单个对象的实例属性
del p1.age

# 给所有对象增加实例方法
Person.eat = eat
p1.eat()
p2.eat()
# 删除所有对象的实例方法
# 如果所有对象都共享实例方法，只能 del 类名.方法名，不能单独给某个对象删
del Person.eat

# 单独给某个对象增加属性值为函数的实例属性（本质上还是实例属性，是对象独有的）
# 错误写法：p1.sleep = sleep
p1.sleep = types.MethodType(sleep, p1)
p1.sleep()
# 单独删除实例属性
# 这时只有 p1 对象上有 sleep 实例方法，只能 del p1.sleep，不能 del Person.sleep
del p1.sleep

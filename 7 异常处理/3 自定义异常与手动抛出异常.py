# 自定义异常，继承 Exception
class AgeError(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int) and 0 <= age <= 200:
            self.age = age
        else:
            # 抛出自定义异常
            raise AgeError(f"年龄{age}不合法（0~200的整数）")

    def __repr__(self):
        return str({
            "name": self.name,
            "age": self.age
        })


try:
    p1 = Person("张三", 18)
    print(p1)
    p2 = Person("李四", -10)
    print(p2)
except AgeError as e:
    print(e)
except Exception as e:
    print(e)

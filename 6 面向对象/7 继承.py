class Moving:
    # 这个类无法直接实例化，应该继承使用
    def move(self):
        print(f"{self.name}在移动")


# 单继承
class Swimming(Moving):
    def move(self):
        print(f"{self.name}在游")


class Flying(Moving):
    def move(self):
        print(f"{self.name}在飞")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}吃东西")


# 多继承
class Dark(Animal, Swimming, Flying):
    def __init__(self, name):
        # 调用的是 Animal.__init__
        super().__init__(name)


d = Dark("鸭子")
d.eat()
# 调用的是 Swimming 的 move
d.move()

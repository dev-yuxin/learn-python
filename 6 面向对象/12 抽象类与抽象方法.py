import abc


class Shape(abc.ABC):
    # 如果一个类含有抽象方法，那么这个类就是抽象类，应该让他继承 abc.ABC 声明为抽象类
    # 抽象类不能实例化，只能交由子类去实例化
    # 如果子类全部实现了父类的抽象方法，那么子类可以实例化。否则子类还是一个抽象类，必须交由它的子类去实现

    # 如果一个实例方法不确定如何实现，必须交由子类重写
    # 这样的方法没有方法体，称其为抽象方法
    # 使用 @abc.abstractmethod 装饰器
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a


class Circle(Shape):
    PI = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return self.PI * self.r * self.r

    def perimeter(self):
        return 2 * self.PI * self.r


shapes = [Square(1), Circle(1)]
for shape in shapes:
    print(f"area={shape.area()}, perimeter={shape.perimeter()}")

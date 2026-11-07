class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Car(Goods):
    def __init__(self, name, price, *, max_speed, **kwargs):
        super().__init__(name, price, **kwargs)
        self.max_speed = max_speed


class Electronic(Goods):
    def __init__(self, name, price, *, max_power, **kwargs):
        super().__init__(name, price, **kwargs)
        self.max_power = max_power


class ECar(Car, Electronic):
    def __init__(self, name, price, *, max_speed, max_power):
        super().__init__(name, price, max_speed=max_speed, max_power=max_power)


# 交换顺序
class ECar2(Electronic, Car):
    def __init__(self, name, price, *, max_speed, max_power):
        super().__init__(name, price, max_speed=max_speed, max_power=max_power)

# 多继承初始化有两种方法：
    # 父类名.__init__(self, ...)
    # 利用 **kwargs 和 super()
# 先调用 ECar 的 __init__
# 再调用 Car 的 __init__ ，把 name, price, max_power 传给 Electronic 的 __init__， max_speed 完成初始化
# 再调用 Electronic 的 __init__ 把 name, price 传给 Goods 的 __init__，max_power 完成初始化
# 最后调用 Goods 的 __init__，name 和 price 完成初始化
car1 = ECar("特斯拉model3", 200000, max_speed=150, max_power=4000)

# 交换继承的顺序也可以
car2 = ECar2("特斯拉model3", 200000, max_speed=150, max_power=4000)

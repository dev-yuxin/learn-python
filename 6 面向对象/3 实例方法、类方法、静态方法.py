class Goods:
    total_goods_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # 访问类属性
        # 这里不能使用 self.类属性名，否则会创建一个同名的实例属性
        Goods.total_goods_count += 1

    def show_goods(self):
        print(f"{self.name}: ￥{self.price:.2f}")


class Cart:
    # 类属性，每满100-10
    reach = 100
    sub = 10

    # 类方法
    # 函数定义在类中，使用 @classmethod 装饰器，第一个参数必须是 cls ，表示类本身
    # 类加载时会存储到一个字典：类.__dict__，key是方法名，value是函数的地址值，被类所有对象共享
    # 如果一个方法要访问类属性、类方法、静态方法，不需要也不能访问实例属性、实例方法，那么定义为类方法。
    # 调用方式：类名.方法名() 不用传入 cls 参数
    @classmethod
    def update_discount(cls, reach, sub):
        cls.reach = reach
        cls.sub = sub

    # 静态方法
    # 函数定义在类中，使用 @staticmethod 装饰器，没有额外参数
    # 类加载时会存储到一个字典：类.__dict__，key是方法名，value是函数的地址值，被类所有对象共享
    # 一般是工具方法，可能调用其它工具方法，不需要访问类属性、类方法（你可以通过类名.xxx调用，但这样你应该定义为类方法），不能访问实例属性、实例方法。
    # 调用方式：类名.方法名()
    @classmethod
    def calc_discounted_price(cls, original_price):
        return original_price - (original_price // cls.reach) * cls.sub

    # 实例方法
    # 函数定义在类中，没有装饰器，第一个参数必须是 self 表示当前实例对象
    # 类加载时会存储到一个字典：类.__dict__，key是方法名，value是函数的地址值，被类所有对象共享
    # 区分：实例属性属性值是个函数：存放在 对象.__dict__ 中，key是方法名，value是函数的地址值，被单个对象独享
    # 如果一个方法要访问实例属性或实例方法，应该定义为实例方法。实例方法可以访问类中所有成员。
    # 调用方式：
    #   对象.方法名() 不需要传入 self 参数，使用场景更多
    #   类名.方法名(self, ...) 需要传入 self 参数
    def __init__(self, owner, goods_list=[]):
        self.owner = owner
        # 函数参数使用默认值时，会公用同一个对象，所以这里要做一些处理
        self.goods_list = goods_list if goods_list else []
        self.update_total_price()

    def update_total_price(self):
        original_total_price = sum(goods.price for goods in self.goods_list)
        self.total_price = Cart.calc_discounted_price(original_total_price)

    def show_cart(self):
        print(f"{self.owner}的购物车:")
        for goods in self.goods_list:
            goods.show_goods()
        print(f"每满￥{Cart.reach:.2f}减￥{Cart.sub:.2f}")
        print(f"总价: ￥{self.total_price:.2f}")

    def add_goods(self, goods):
        self.goods_list.append(goods)

    def remove_goods(self, goods):
        self.goods_list.remove(goods)


goods_list = [
    Goods("电脑", 5000),
    Goods("鼠标", 100),
    Goods("键盘", 200),
    Goods("耳机", 100),
]
print(Goods.total_goods_count)

cart1 = Cart("张三")
cart1.add_goods(goods_list[0])
cart1.add_goods(goods_list[1])
cart1.add_goods(goods_list[2])

cart2 = Cart("李四")
cart2.add_goods(goods_list[1])
cart2.add_goods(goods_list[2])
cart2.add_goods(goods_list[3])
cart2.remove_goods(goods_list[2])

Cart.update_discount(100, 15)
cart1.update_total_price()
cart2.update_total_price()

cart1.show_cart()
cart2.show_cart()

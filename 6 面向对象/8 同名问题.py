# Python中没方法重载
# Python 中除了方法（类方法、静态方法、实例方法都可以重写，只看方法名是否相同，不看其它）重写，其余应该避免出现同名

# 同一个类里
# 类属性、类方法、静态方法、实例方法存在 类.__dict__ 中，同名后面将覆盖前面的。
# 实例属性存放在 对象.__dict__ 中，同名后面将覆盖前面的。
# 实例属性 和 类属性/类方法/静态方法/实例方法，如果出现同名，实例属性优先。
class Test:
    # 类属性（属性值是函数）
    f = lambda *args: print("类属性f")

    @staticmethod
    def f(*args):
        print("静态方法f")

    @classmethod
    def f(cls, *args):
        print("类方法f")

    def __init__(self):
        # 实例属性（属性值是函数）
        self.f = lambda: print("实例属性f")

    # 实例方法
    def f(self, *args):
        print("实例方法f")


test = Test()
# 调用的是实例属性f
test.f()
# 调用的是实例方法f
Test.f(test)


# 继承关系
# 类属性、类方法、静态方法、实例方法如果同名，分别存在 子类名.__dict__ 和 父类名.__dict__ 中
# 需要注意的是实例属性，Python区别于其它语言，它把实例属性存在 对象.__dict__ 里，同名将覆盖。
# 如果是 __xxx 的实例属性，会有改写机制。
# 查找顺序：对象自身.__dict__ => 当前类.__dict__ => super().__dict__ =>  ...MRO链... => Object.__dict__ => 报错
class A:
    a = 0
    b = 1

    def __init__(self):
        self.b = 2
        self.__c = 3


class B(A):
    a = 4

    def __init__(self):
        super().__init__()
        self.b = 5
        self.__c = 6

    def show(self):
        # 自身对象.__dict__（没有）=> B.__dict__（找到为4不再继续）=> A.__dict__ => Object.__dict__
        print(self.a)
        # 自身对象.__dict__（找到为5不再继续）
        print(self.b)
        # 跳过 B 从 A.__dict__ 找（找到为1不再继续）
        print(super().b)
        # 自身对象.__dict__（键转为 _B__c，找到为6）
        print(self.__c)
        # 自身对象.__dict__（找到为3）
        print(self._A__c)
        # 自身对象.__dict__（找到为6）
        print(self._B__c)


B().show()

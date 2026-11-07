# MRO （方法解析顺序）
# 先子后父
# 继承的父类按从左到右的顺序
# 有公共父类必须先遍历完它所有子类

#      A
#   /   \  \
# B     C    D
# |     |    |
# E     F    |
# \     /   /
#      G

# MRO: G => E => B => F => C => D => A
# 注意 super() 不是父类
# super(): 表示MRO链下一个，比如你在B里面就是F
# super(G, self): 指定下一个，不管你在哪里，都是E
# 你也可以使用 类名.方法(self, ...) 调用

class A:
    def f(self):
        print("A的实例方法")


class B(A):
    def f(self):
        print("B的实例方法")

    def test_super(self):
        # 按照MRO链，调用的是F的f
        super().f()
        # 指定调用E的f
        super(G, self).f()
        # 也可以用 类名.方法名(self, ...) 调用
        E.f(self)


class C(A):
    def f(self):
        print("C的实例方法")


class D(A):
    def f(self):
        print("D的实例方法")


class E(B):
    def f(self):
        print("E的实例方法")


class F(C):
    def f(self):
        print("F的实例方法")


class G(E, F, D):
    def f(self):
        print("G的实例方法")


g = G()
g.test_super()

# 多态是指相同的代码会有不同执行效果
# 在面向对象里一般指继承后方法重写，调用相同方法，执行效果不同

class Animal:
    def eat(self):
        print("动物在吃东西")


class Dog(Animal):
    def eat(self):
        print("狗在吃骨头")


class Cat(Animal):
    def eat(self):
        print("猫在吃鱼")


animals = [Cat(), Dog()]
for animal in animals:
    # 多态
    animal.eat()

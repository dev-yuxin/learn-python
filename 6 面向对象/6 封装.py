class Person:
    def __init__(self, name, age, phone):
        # 公开成员
        # 不要给公开成员设置 getter 和 setter ，一是不需要，二是会造成无限递归
        self.name = name
        # python 中没有 private, protected, public 关键字来实现私有成员，通过 _和__来约定
        # 约定：类中使用 _xxx 直接访问，而类外不应该使用 _xxx 访问，你应该提供方法或者 getter/setter 来操作
        self._age = age
        # __xxx 则是一种改写（对象.__dict__ 里的 key被改写），会被改写为 _类名__xxx
        # 类中使用 __xxx 直接访问，而类外不能使用 __xxx 访问，不应该使用 _类名__xxx，你应该提供方法或者 getter/setter 来操作
        self.__phone = phone

    # getter 装饰器
    @property
    def age(self):
        return self._age

    # setter 装饰器
    @age.setter
    def age(self, new_val):
        if isinstance(new_val, int) and 0 <= new_val <= 200:
            self._age = new_val
        else:
            print("年龄不合法，修改失败")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_val):
        if isinstance(new_val, str) and new_val.isdecimal():
            self.__phone = new_val
        else:
            print("手机号不合法，修改失败")


p = Person("张三", 20, "110")
p.age = -100
print(p.age)
p.phone = "120"
print(p.phone)

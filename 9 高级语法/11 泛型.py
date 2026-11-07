from typing import Generic, Optional, TypeVar

# python 和 ts 一样，也提供了泛型（只做提示，不会限制）
# 常用泛型（复杂类型大写需要从 typing 导入，3.9之后支持复杂类型的小写，无需导入）
# 内置基本类型 int, float, bool, str, None
# 任一类型: any(Any)
# 容器类型（元素类型是any）: list(List), tuple(Tuple), set(Set), dict(Dict)
#   list[int] 期望列表元素都是 int
#   tuple[int, ...] 期望元组元素都是 int
#   tuple[int,] 期望元组只有1个int元素
#   set[int] 期望集合元素都是 int
#   dict[str, int] 期望字典键是 str 值是 int
# Union[int, float] 期望类型是 int 或 float，也可以写为 int | float
# Optional[int] 期望类型是 int 或 None，也可以写为 int | None
# Literal[1, "1", True, False, 0, "0"] 期望值是这几个字面量值里的一个

# T 是任一类型，期望容器元素都是 T 类型
T = TypeVar('T')


def first(_list: list[T]) -> Optional[T]:
    return _list[0] if len(_list) else None


print(first([1, 2, 3]))
print(first(["1", "2", "3"]))


class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# A 期望是 Animal 及其子类，期望容器元素都是 Animal 及其子类
A = TypeVar('A', bound=Animal)


def last(_list: list[A]) -> Optional[A]:
    return _list[-1] if len(_list) else None


print(last([Cat(), Dog()]))

K = TypeVar('K')


# 在类中使用泛型，继承 Generic
class Node(Generic[K]):
    # 这里引用自身，必须使用 Optional[] + 字符串形式
    # 不能写成 next = Node[K] | None
    def __init__(self, data: T, next: Optional['Node[K]'] = None):
        self.value = data
        self.next = next


# 这里能根据值自动推断
node1 = Node[int](1)
node2 = Node(2)
node1.next = node2

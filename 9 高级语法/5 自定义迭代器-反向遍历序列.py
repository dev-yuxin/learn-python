# 既是一个可迭代对象，又是一个迭代器对象
class ReverseSequence:
    def __init__(self, seq):
        self.seq = seq

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index < -len(self.seq):
            raise StopIteration
        item = self.seq[self.__index]
        self.__index -= 1
        return item


list1 = ReverseSequence([1, 2, 3, 4, 5])
for item in list1:
    print(item)

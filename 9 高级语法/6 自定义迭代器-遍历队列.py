class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            pop_node = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return pop_node.data
        else:
            pop_node = self.head
            self.head = self.head.next
            self.size -= 1
            return pop_node.data

    def __iter__(self):
        self.__p = self.head
        return self

    def __next__(self):
        if not self.__p:
            raise StopIteration
        else:
            data = self.__p.data
            self.__p = self.__p.next
            return data


queue = Queue()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.pop()
queue.pop()

for item in queue:
    print(item)

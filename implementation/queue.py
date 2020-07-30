from take_home.base.base_queue import BaseQueue
import dill as pickle

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue(object):
    ''' Abstract base class for queue implementations. '''
    def __init__(self, max_in_memory: int):
        self.max_in_memory = max_in_memory
        self.head = None
        self.tail = None
        self.arr = bytearray()

    @property
    def count(self):
        temp = self.head
        cnt = 0
        while temp is not None:
            cnt = cnt + 1
            temp = temp.next
        return cnt
    
    @property
    # def in_memory_count(self) -> int:
    def in_memory_count(self):
        lenar = len(self.arr)
        return lenar
        
    @property
    # def on_disk_count(self) -> int:
    def on_disk_count(self):
        lenr = len(self.arr)
        return lenr

    def enqueue(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
            self.tail = self.head
        elif self.count() < self.max_in_memory:
            self.tail.next = new_value
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            tail = self.tail
        else:
            exi = value
            self.arr.append(exi)
            exval = new_value
            with open("excess_nodes.obj","wb+") as fi:
                pickle.dump(exval, fi)

    def dequeue(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail is None
        return value

    def peek(self):
        if self.head is not None:
            return self.head.value
        else:
            return False

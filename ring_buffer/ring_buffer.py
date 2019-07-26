class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current == len(self.storage):
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        temp = []
        for i in range(0, len(self.storage)):
            if self.storage[i] != None:
                temp.append(self.storage[i])
        return temp

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.capacity = k
        self.front = 0 # array index of front value
        self.count = 0 # number of elements in the queue
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.front+self.count)%self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = 0 # FIFO
        self.front = (self.front+1)%self.capacity # 把front指针往后挪一步。
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        if self.isEmpty(): 
            return -1
        # get the array index for the rear
        rear_index = (self.front + self.count - 1) % self.capacity
        return self.queue[rear_index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
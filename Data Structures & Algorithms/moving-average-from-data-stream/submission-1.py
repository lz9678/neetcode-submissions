from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.deque = deque()
        self.current_sum = 0
        

    def next(self, val: int) -> float:
        self.deque.append(val)
        self.current_sum +=  val

        if len(self.deque) > self.size:
            oldest_val = self.deque.popleft()
            self.current_sum -= oldest_val

        return self.current_sum/len(self.deque)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

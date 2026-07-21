
import collections

class MovingAverage:

    def __init__(self, size: int):
        self.size = size   #  instance attribute（实例属性）
        # 以后这个对象里的其他函数都可以通过self.size访问这个值。
        # Class variable不写在__init__里头，而是直接写在class里头，是所有对象共享的。
        self.deque = collections.deque() # 最近窗口里的数字 FIFO fixed-size circular buffer
        self.current_sum = 0

    def next(self, val: int) -> float:
        """
        接收一个新的整数，并返回当前滑动窗口的移动平均值。
        """
        # 1. 将新值添加到队列和总和中
        self.deque.append(val)
        self.current_sum += val

        # 2. 如果队列长度超过窗口大小，移除最旧的值
        if len(self.deque) > self.size:
            oldest_val = self.deque.popleft()
            self.current_sum -= oldest_val

        # 3.计算并返回当前窗口的平均值
        # deque的长度始终代表当前窗口中的元素数量
        return self.current_sum/len(self.deque)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

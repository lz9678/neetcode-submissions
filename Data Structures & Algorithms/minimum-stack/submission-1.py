class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # 存每一次push val的时候的最小值
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack: #如果min_stack是空的
            self.min_stack.append(val) #这个数就是目前最小的，加入min_stack
        else:
            # 如果min_stack不是空的
            # 比较val和min_stack最后一个数（也就是最小的）
            # 如果val更小，加入
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]


        

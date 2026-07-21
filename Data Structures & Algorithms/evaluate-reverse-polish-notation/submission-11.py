class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = set(["+","-","*","/"])
        n = len(tokens)
        nums = []
        for i in range(0, n):
            if tokens[i] not in operation:
                nums.append(int(tokens[i]))
            else:
                right = nums.pop()
                left = nums.pop()
                if tokens[i] == "+":
                    nums.append(left+right)
                elif tokens[i] == "-":
                    nums.append(left-right)
                elif tokens[i] == "*":
                    nums.append(left*right)
                elif tokens[i] == "/":
                    nums.append(int(left/right))
                
        return nums[0]


            

        
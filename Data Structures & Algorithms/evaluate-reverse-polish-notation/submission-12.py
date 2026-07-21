class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = set(["+","-","*","/"])
        nums = []
        for token in tokens:
            if token not in operation:
                nums.append(int(token))
            else:
                right = nums.pop()
                left = nums.pop()
                if token == "+":
                    nums.append(left+right)
                elif token == "-":
                    nums.append(left-right)
                elif token == "*":
                    nums.append(left*right)
                else:
                    nums.append(int(left/right))
                
        return nums[0]


            

        
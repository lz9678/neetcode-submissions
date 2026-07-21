class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        stack = []
        operation = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in operation:  # 如果有},],)
                if not stack:  # stack里没有东西：不对称  
                    return False
                
                last = stack.pop()  # 如果有},],) 而且stack里有东西
                if operation[char] != last:  #但是两者不对称
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
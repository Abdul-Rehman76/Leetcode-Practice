class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for char in tokens:
            if char in ["+","-","/","*"]:
                val1=stack.pop(-1)
                val2=stack.pop(-1)
                if char == "+":
                    stack.append(val2+val1)
                if char == "*":
                    stack.append(val2*val1)
                if char == "-":
                    stack.append(val2-val1)
                if char == "/":
                    stack.append(int(val2/val1))
            else:
                stack.append(int(char))
        return stack.pop(-1)
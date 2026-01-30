class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        for i in operations:
            if i.lstrip('-').isdigit():
                total.append(int(i))
            elif i == 'D': total.append((total[-1])*2)
            elif i == 'C': total.pop()
            else: 
                if len(total)>=2: 
                    total.append((total[-1] + total[-2]))
            print(total)
        return sum(total)
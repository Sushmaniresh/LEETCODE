class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch=='(' or ch == '{' or ch == '[':
                stack.append(ch)
            else: 
                if not stack:
                    return False
                top = stack[-1]
                if (ch == ')' and top!= '(') or \
                   (ch == '}' and top!= '{') or \
                   (ch == ']' and top!= '[') :
                   return False

                stack.pop()
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack

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
        mapping = { "(": ")", "[": "]", "{": "}"  }
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[top] != ch:
                    return False
        return not stack

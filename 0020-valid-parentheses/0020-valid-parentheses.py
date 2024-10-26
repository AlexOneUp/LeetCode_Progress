class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0 : return False
        
        compare = ['(', '{', '[']
        stack = []

        for i in range(len(s)):
            if s[i] in compare:
                stack.append(s[i])
            else:
                if s[i] not in compare and len(stack) == 0:     
                    return False
                elif s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i]== ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

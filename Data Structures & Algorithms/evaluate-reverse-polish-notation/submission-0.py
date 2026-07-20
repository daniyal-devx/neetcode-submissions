class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if stack and  tokens[i]=='+':
                s1=int(stack.pop())
                s2=int(stack.pop())
                stack.append(s2+s1)
            elif stack and tokens[i]=='-':
                s1=int(stack.pop())
                s2=int(stack.pop())
                stack.append(s2-s1)
            elif stack and tokens[i]=='*':
                s1=int(stack.pop())
                s2=int(stack.pop())
                stack.append(s2*s1)
            elif stack and tokens[i]=='/':
                s1=int(stack.pop())
                s2=int(stack.pop())
                stack.append(s2/s1)
            else:
                stack.append(tokens[i])
        return int(stack[-1])
            

                
        
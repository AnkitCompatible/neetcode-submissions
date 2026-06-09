class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a=stack.pop()
                b=stack.pop()
                print(f"{a} {tokens[i]} {b}")
                if tokens[i]=="+":
                    a+=b
                if tokens[i]=="-":
                    a=b-a
                if tokens[i]=="*":
                    a*=b
                if tokens[i]=="/":
                    a=int(b/a)
                stack.append(a)
            else:
                stack.append(int(tokens[i]))
        a=stack.pop()
        return a
    def removeStars(self, s: str) -> str:
        stack1 = []
        for i in s:
            if i != "*":
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        return("".join(stack1))

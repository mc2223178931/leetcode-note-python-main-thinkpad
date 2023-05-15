class CQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        n = len(self.stack1)
        if n != 0:
            for i in range(n):
                if i < len(self.stack1)-1:
                    self.stack2.append(self.stack1.pop())
                else:
                    res = self.stack1.pop()
                    for j in self.stack2:
                        self.stack1.append(j)
                    return res
        else:
            return -1
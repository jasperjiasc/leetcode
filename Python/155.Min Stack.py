class MinStack(object):
    def __init__(self):
        self.st = []        
    def push(self, x):
        cur_min = min(x, self.st[-1][1] if self.st else x)
        self.st.append((x, cur_min))                
    def pop(self):
        self.st.pop()        
    def top(self):
        return self.st[-1][0]        
    def getMin(self):
        return self.st[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(4)
    minStack.push(5)
    minStack.push(1)
    minStack.push(3)
    assert minStack.getMin() == 1
    minStack.pop()
    minStack.pop()
    assert minStack.top() == 5
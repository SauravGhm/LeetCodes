from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque() # this queue will always have the latest stack order
        self.q2 = deque() #this queue is used for pushing

    def push(self, x: int)-> None:
        self.q2.append(x)
        #push all the elements of q1 to q2 
        while self.q1:
            self.q2.append(self.q1.popleft())
        #swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()
    
    def top(self)-> int:
        return self.q1[0]
    
    def empty(self) ->bool:
        return not self.q1
    
myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)

myStack.push(5)


print(myStack.top())    # Output: 2
print(myStack.pop())    # Output: 2
print(myStack.empty())  # Output: False



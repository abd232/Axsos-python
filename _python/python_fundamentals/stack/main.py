class Stack:
    def __init__(self):
        self.stack = []
        self.topIndex = -1;
    
    def isEmpty(self):
        return self.topIndex == -1

    def push(self,element):
        self.stack.append(element)
        self.topIndex += 1;
    
    def pop(self):
        if self.topIndex == -1:
            return False;
        
        value = self.stack[self.topIndex]

        self.topIndex -= 1
        self.stack.pop()
        return value

    def display_stack_elements(self):
        print(self.stack)

mystack = Stack()
print(mystack.isEmpty())

mystack.push(1);
mystack.push(2);
mystack.push(3);
mystack.push(4);
mystack.push(5);
print(mystack.isEmpty())

mystack.display_stack_elements()

print(mystack.pop())
print(mystack.pop())

mystack.display_stack_elements()


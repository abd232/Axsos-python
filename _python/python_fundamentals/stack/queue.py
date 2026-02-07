class Queue:
    def __init__(self):
        self.queue = []
        self.elementCount = 0;
    
    def enqueue(self,element):
        self.queue.append(element)
        self.elementCount += 1
    
    def dequeue(self):
        if self.elementCount == 0:
            return False;
        
        value = self.queue[0]
        self.queue.pop(0)
        self.elementCount -= 1
        return value

    def display_queue_elements(self):
        print(self.queue)

    def queue_size(self):
        return self.elementCount

myQueue = Queue()

myQueue.enqueue(1);
myQueue.enqueue(2);
myQueue.enqueue(3);
myQueue.enqueue(4);
myQueue.enqueue(5);

myQueue.display_queue_elements()
print("element size:",myQueue.queue_size())

print(myQueue.dequeue())
print(myQueue.dequeue())

myQueue.display_queue_elements()
print("element size:",myQueue.queue_size())
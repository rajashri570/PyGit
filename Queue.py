class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return len(self.queue) == 0
    def add(self,val):
        self.queue.append(val)
        self.rear += 1
    def disp_queue(self):
        print(self.queue)
    def remove(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            self.front += 1
            return self.queue.pop(self.front)
    def get_size(self):
        return len(self.queue)
q1 = Queue()
q1.add(5)
q1.add(10)
q1.disp_queue()
print("Is empty Quaue:",q1.is_empty())
q1.remove()
q1.disp_queue()
q1.add(34)
q1.add(44)
q1.disp_queue()
q1.remove() 
q1.disp_queue()

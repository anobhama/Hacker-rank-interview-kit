class MyQueue(object):
    def __init__(self):
        self.first = []

    def peek(self):
        return self.first[0]

    def pop(self):
        value = self.first[0]
        self.first.remove(self.first[0])
        return value

    def put(self, value):
        return self.first.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
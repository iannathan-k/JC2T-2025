queue = [None for _ in range(4)]
front = 0
rear = -1
queue_length = 0
QUEUE_FULL = len(queue)

def enqueue(item):
    global queue_length
    global rear
    if queue_length == QUEUE_FULL:
        print("Queue Full!")
        return
    
    if rear == QUEUE_FULL - 1:
        rear = 0
    else:
        rear += 1

    queue[rear] = item
    queue_length += 1

def dequeue():
    global front
    global queue_length
    if queue_length == 0:
        print("Queue Empty")
        return
    
    value = queue[front]
    queue_length -= 1
    
    if front == QUEUE_FULL - 1:
        front = 0
    else:
        front += 1

    return value

print(queue)
print(dequeue())

print(queue)
enqueue(4)
print(queue)
enqueue(3)
print(queue)
enqueue(2)
print(queue)
enqueue(1)
print(queue)
enqueue(8)

print(queue)
print("element:", dequeue())
print(queue)
print("element:", dequeue())

print(queue)
enqueue(9)
print(queue)
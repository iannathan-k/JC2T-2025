queue = [None for _ in range(10)]
front = 0
rear = -1
queue_length = 0
QUEUE_FULL = len(queue)

def isEmpty():
    global queue_length
    return queue_length == 0

def isFull():
    global queue_length
    return queue_length == QUEUE_FULL

def enqueue(item):
    global queue_length
    global rear
    if isFull():
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
    if isEmpty():
        print("Queue Empty")
        return
    
    value = queue[front]
    queue_length -= 1
    
    if front == QUEUE_FULL - 1:
        front = 0
    else:
        front += 1

    return value
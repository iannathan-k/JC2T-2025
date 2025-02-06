import queueAbstraction
import stackAbstraction

queueAbstraction.enqueue(1)
queueAbstraction.enqueue(2)
queueAbstraction.enqueue(3)
queueAbstraction.enqueue(4)
print(queueAbstraction.queue)

def reverseQueue():
    while not queueAbstraction.isEmpty():
        stackAbstraction.pushStack(queueAbstraction.dequeue())
    
    while not stackAbstraction.isEmpty():
        queueAbstraction.enqueue(stackAbstraction.popStack())

reverseQueue()
print(queueAbstraction.queue)
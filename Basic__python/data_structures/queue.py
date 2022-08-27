# queue
# enqueue
# dequeue


size=int(input('enter the size '))
queue=[]
def enqueue():
    if len(queue)>=size:
        print('queue is full')
    else:
        u=int(input('enter the element '))
        queue.append(u)
        print(queue)
def dequeue():
    if len(queue)<1:
        print('queue is empty ')
    else:
        queue.remove(queue[0])
        print(queue)
while True:
    option = int(input('1.enqueu \n2.dequeue :'))
    if option == 1:
        enqueue()
    else:
        dequeue()
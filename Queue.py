# basic queue implementation using deque
'''
from collections import deque


def createQueue():
    queue = deque()
    return queue


def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    return queue.popleft()


q = createQueue()

enqueue(q, 1)
enqueue(q, 2)
enqueue(q, 3)

print(q)

dequeue(q)
print(q)

'''
# Queue using stacks
'''
from collections import deque

pushStack = deque()
popStack = deque()

def Enqueue(item):
  pushStack.append(item)

def Dequeue():
  if len(pushStack) == 0 and len(popStack) == 0:
    print('Queue Empty')
    return  

  elif len(popStack) == 0 and len(pushStack) > 0 :
    while len(pushStack):
      top  = pushStack.pop()
      popStack.append(top)
    return popStack.pop()  
  else:
    return popStack.pop()

def printl():
  print(pushStack)

Enqueue(1)
Enqueue(2)
Enqueue(3)
printl()
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
'''
# Reverse a queue
'''
from collections import deque

q = deque()

def enqueue(item):
  q.append(item)

def rev():
  start = 0
  last = len(q) - 1

  for _ in range(len(q)):
    while (start <= last  ):
      temp = q[start]
      q[start] = q[last]
      q[last] = temp

      start += 1
      last -= 1
  


def printq():
  print(  q )

enqueue(1)  
enqueue(2)  
enqueue(3)  
enqueue(4) 
enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)
enqueue(9)
enqueue(10)
enqueue(11)
enqueue(12)

printq()
rev()
printq()
'''
# reverse a queue using recursion
'''
from collections import deque


def createQ():
  q = deque()
  return q

def size(q):
  return len(q)-1


def enqueue(q,item):
  q.append(item)



def rev(q, start, last):
  if start> last:
    return
  else:
    temp = q[start]
    q[start] = q[last]
    q[last] = temp

    
    rev(q, start+1, last-1)

def printq(q):
  print(q)


Q = createQ()
enqueue(Q,1)
enqueue(Q,2)
enqueue(Q,3)
enqueue(Q,4)
enqueue(Q,5)
enqueue(Q,6)
enqueue(Q,7)
enqueue(Q,8)
enqueue(Q,9)
enqueue(Q,10)
enqueue(Q,11)
enqueue(Q,12)

printq(Q)

rev(Q, 0, size(Q))
printq(Q)
'''
# Reversing first  k elements of queue
'''
from collections import deque

q = deque()

def Enq(item):
  q.append(item)


def rev(k):
  start = 0
  last = k-1

  while(start <= last):
    temp = q[start]
    q[start] = q[last]
    q[last] = temp

    start += 1
    last -= 1

Enq(1)
Enq(2)
Enq(3)
Enq(4)
Enq(5)
print(q)
rev(4)
print(q)
'''

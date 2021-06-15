'''
#stack using list

# basic operations, insertion and deletion

stack = []

#inserting values
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

#poping
stack.pop()
stack.pop()
print(stack)
'''
# stack reverse using recursion
# my solution-->
'''
#reverse a stack using recursion

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
n = len(stack)-1
print(f'Stack before recursion: {stack}')
new_stack = deque()

def add(n):
  if n < 0:
    return
  else:
    new_stack.append(stack[n]) 
    add(n-1) 
  return new_stack

print(f' Stack after recursion : {add(n) }') 

'''
# sorting stack using another stack
'''
from collections import deque
#sort a stack with help of another stack

def createStack(): #creating an empty stack
  stack = deque()
  return stack

def top(stack):
  n = len(stack)
  return stack[n-1]

#general operations
def push(stack, item):
  stack.append(item)

def isEmpty(stack):
  return len(stack) == 0

def pop(stack):
  if isEmpty(stack):
    print('Stack underflow')
    exit(1)
  return stack.pop()

stack = createStack()
push(stack, 9)
push(stack, 11)
push(stack, 1)
push(stack, 5)
push(stack, 8)

print(stack)

# now, we will sort the stack
def sortStack(stack):
  new_stack = createStack()

  while(isEmpty(stack) == False):
    temp = top(stack)
    pop(stack)

    while(isEmpty(new_stack) == 0 and top(new_stack)>int(temp)):
      push(stack, top(new_stack))
      pop(new_stack)
    push(new_stack, temp)  
  return new_stack

sortedstack = sortStack(stack)    
print('stack after sorting is ',sortedstack)
'''
# reversing a stack without any extra space
# we will use linkedlist
# implement stack using a linkedlist

'''
class stackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top == None:
            self.top = stackNode(data)
            return
        s = stackNode(data)
        s.next = self.top
        self.top = s

    def printl(self):
        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.next

    def rev(self):
        prev = None
        curr = self.top

        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.top = prev

        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.next


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.printl()
print('after reversing')
s.rev()
'''
'''
#delete middle elements
class stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def isEmpty(self):
    return self.items == []

  def pop(self):
    self.items.pop()

  def top(self):
    n = len(self.items)-1
    return self.items[n] 

  def size(self):
    return len(self.items)
  
  def printl(self):
    print(self.items)

def delete(s, n, curr):#n--> size of stack
  if s.isEmpty() or curr == n :
    return
  x = s.top()  
  s.pop()

  delete(s, n, curr + 1)

  if curr != int(n/2) :
    s.push(x)




s = stack()
s.push(1)    
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.printl()
print('After deleting middle value')
delete(s, s.size(), 0)
s.printl()

'''
'''
#reversing words

def rev(string):
  s = list()

  for _ in range(len(string)):
    if string[_] != " ":
     s.append(string[_])

    else:
      while len(s) > 0:
        print(s[-1], end = '')
        s.pop()
      print(" ",end = '')    

  while len(s) > 0:
     print(s[-1], end = '')
     s.pop()

string = 'heyy Raj'
print(len(string))    
rev(string) 

'''
# reversing a number using stack
'''


def rev(n):
  stack = list()
  for _ in range(len(n)):
   
    stack.append(n[_])
      
    
    
  while len(stack)>0:
    print(stack[-1], end=' ') 
    stack.pop()

n = [2,3,4]

print('Number entered is :',*n)
print('Number after reversal:')
'''
# balanced Pranthesis check.
'''
def createStack():
  stack = list()
  return stack

def isEmpty(stack):
  return len(stack) == 0

def push(stack, item):
  stack.append(item)

def pop(stack):
  return stack.pop()

def peek(stack):
  return stack[len(stack)-1] 

def check(stack,input_symbol):
  for _ in (input_symbol):
    if _ in ['[','{','{']:
     push(stack, _)
     
    else:
      if _ == ']' and peek(stack) == '[':
        pop(stack)
      if _ == ')' and peek(stack) == '(':
        pop(stack)  
      if _ == '}' and peek(stack) == '{':
        pop(stack)      
      
     
    
  print(stack)
  if isEmpty(stack) :
    print('Balanced')   
  else:
    print('Not Balanced')        

s = createStack()
n = '[(){}]'
check(s, n)
'''
# next greater element
# create a stack


'''
def NGE(stack):
  lst =[]
  for _ in range(len(stack)):

    top = stack[len(stack) - 1 - _ ]
    if top == stack[len(stack) - 1]:
      lst.append(-1)
    else:
      if top < stack[len(stack) - 1 - _ + 1 ]:
        lst.append(stack[len(stack) - 1 - _ + 1 ])
      else:
        for i in range(len(stack) - 1 - _ + 1 , len(stack)):
          if stack[i] > top :
            lst.append(stack[i])
            break             
          else :
            while(stack[i] < top and i < len(stack)-1):
              i += 1
        if stack[i] == stack[len(stack)-1]:
          lst.append(-1)
          
            
           
             

             
  print(input_arr)
  print(lst[::-1])        

input_arr = [11,13,21,3]
NGE(input_arr)
'''
# Stack using queue
'''
from collections import deque 

pushQ = deque()
popQ = deque()

def push(item):
  pushQ.append(item)

def pop():
  if len(pushQ) == 0 and len(popQ) == 0:
    print('stack empty')
    return
  elif len(popQ) == 0 and len(pushQ) > 0:
    while (len(pushQ)-1):
      x = pushQ.popleft()
      popQ.append(x)
    poped = pushQ.popleft()

    while len(popQ):
      y = popQ.popleft()
      pushQ.append(y)
    return  poped

def printl():
  print(pushQ)

push(1)  
push(2)
push(3)
printl()
print(f' pop:{pop()}')
print(f' pop:{pop()}')
printl()
push(4)
printl()



  
 


  
    '''

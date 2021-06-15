'''
# linked List

class Node :
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printl(self)  :
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

if __name__=='__main__':
  llist = LinkedList()
  llist.head = Node(1)
  second = Node(2)
  third = Node(3)

  llist.head.next = second;
  second.next = third;


  llist.printl()
'''
#linkedlist + traversing
# step 1 create node and linklist class
# adding nodes
'''

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linkedlist:
  def __init__(self):
    self.head = None

  def push(self,new_data)  :
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def insertAfter(self, prev_node, new_data):
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def printl(self)  :
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def append(self,new_data)  :
    new_node = Node(new_data) 
    if self.head is None:
      self.head = new_node
      return
     
    last = self.head
    while(last.next):
      last = last.next
    last.next = new_node


#code starts running here      

if __name__=='__main__':
  #create objects of linkedlist and Node

  llist = linkedlist()
 
  #connecting the individual nodes
 
  # # llist.printl()
  # # llist.push(5)
  #llist.printl()
  #llist.insertAfter(2,7)
  llist.append(4)
  llist.push(7)
  llist.append(5)
  llist.append(8)
  llist.append(9)
  llist.insertAfter(llist.head.next,1)
  llist.printl()
 


'''
# delete a node based on key
'''
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
      temp = self.head

      #check if headnode itself is the node to be deleted
      if (temp is not None):
        if temp.data == key :
          self.head = temp.next
          temp = None
          return
      while (temp is not None) :
           
        if temp.data == key :
          break
        prev = temp 
        temp = temp.next 
          
      if temp == None:
          return    
          
      prev.next = temp.next
      temp = None  

    def Nnode(self,pos):
      temp = self.head
      if temp is None:
        print('No value')
      if pos == 0:
        print('value is ',temp.data)  

             
      else:
        for _ in range(pos):
          temp = temp.next
          if temp is None:
            print('No value')   
            return

          
           
        
             
        print('value is ',temp.data)   

    def printList(self):
      temp = self.head
      while(temp):
          print (" %d" %(temp.data)),
          temp = temp.next    

llinklist = LinkedList()
llinklist.push(2)        
llinklist.push(4)  
llinklist.push(7)
#llinklist.printList()
llinklist.deleteNode(4)
llinklist.printList()
'''
'''
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
      temp = self.head

      if temp is not None:
        if temp.data == key :
          self.head = temp.next
          temp = None
          return

      while( temp is not None)    :
        #traverse
        if temp.data == key:
          break
        prev = temp
        temp = temp.next  

      if temp is None:
        return

      

      prev.next = temp.next

      temp = None  

    def countNodes(self)  :
      temp = self.head
      count = 0

      if temp is None:
        count = 0
        

      while(temp) :
        temp = temp.next
        count = count + 1
            

      print('Count is ',count)

    def search(self, key):
      temp =  self.head

      while( temp is not None):
        if temp.data == key:
             
          return True
        temp = temp.next
      return False 

    def Nnode(self,pos):
      temp = self.head
      if temp is None:
        print('No value')
      if pos == 0:
        print('value is ',temp.data)  

             
      else:
        for _ in range(pos):
          temp = temp.next
          if temp is None:
            print('No value')   
            return         
           
        
             
        print('value is ',temp.data) 

    def nth(self, n):
      temp = self.head

      length = 0
      
      while temp is not None:
        temp = temp.next
        length = length + 1
      if n > length:
        print('No such value')
        return

      if n == 0:
        print('No such value') 
        return 

      temp = self.head
      for _ in range(0,length-n):
        temp = temp.next
      print('vlaue  is',temp.data) 


    def delnth(self,x) :
      #first find nth node from back
      length = 0
      temp = self.head
      
      while(temp):
        temp = temp.next
        length+=1

      if x > length :
        return

      if x == 0:

        return
      temp = self.head
      # for _ in range(0, length-n) :
      #   temp = temp.next
      #   return temp
      pos = length-x

      for _ in range(pos-1):
        temp = temp.next

      next = temp.next.next

      

      temp.next = None
      temp.next = next
      
    def mid(self) :
      length = 0

      temp = self.head

      while(temp):
        temp = temp.next
        length+=1

      
      if length % 2 == 0:
        temp = self.head
        new_pos = length // 2  

        for _ in range(new_pos-1):
          temp = temp.next
        print('Middle value 1:',temp.data)  
        temp = temp.next
        print('Middle value 2:',temp.data)

      else:
        temp = self.head
        odd_pos = (length + 1) // 2

        for _ in range(odd_pos-1):
          temp = temp.next
        print('Odd number of nodes. Middle value is', temp.data)  

    def rep(self, key):
      temp = self.head
      count = 0

      if temp is None:
        return
      if temp.next is None :
        return

      while(temp):
        if temp.data == key:
          count += 1
        temp = temp.next  
      if count == 1:
        print(f'Repeated {count-1} times')  
      else:  
        print(f'Repeated {count} times')
    

      

    def loop(self) :
      lst = set()
      temp = self.head

      while(temp):
        if temp in lst:
          print('Loop Found')
          break
       
          
        lst.add(temp)
        temp = temp.next

    def floyd(self):
      #two pointers
      slow = self.head
      fast = self.head
      count = 0

      while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        count += 1
        if slow == fast:
          print('Loop found')
          print('no of nodes in loop:',count)
          return

    def removeLoop(self):
      slow = self.head
      fast = self.head
      count = 0      

      while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        count += 1
        
        if slow == fast:
          print(count)               
          return
      for _ in range(count-1) :
        slow = slow.next
      slow.next = None  
      print('Loop removed')




       
      

    def printList(self):
      temp = self.head
      while(temp):
          print (" %d" %(temp.data),sep='\n'),
          temp = temp.next    

llinklist = LinkedList()
# llinklist.push(2)        
# llinklist.push(4)  
# llinklist.push(2)
# llinklist.push(6)
# llinklist.push(9)
# llinklist.push(11)
# llinklist.push(2)
# llinklist.push(2)
# llinklist.push(45)
# llinklist.push(2)
llinklist.push(20)
llinklist.push(4)
llinklist.push(15)
llinklist.push(10)
llinklist.head.next.next.next.next = llinklist.head
#llinklist.printList()
#llinklist.deleteNode(4)
#llinklist.deleteNode(2)
#llinklist.printList()
#llinklist.countNodes()
# if llinklist.search(7):
#   print('found')
# else:
#   print('Nope')  
# llinklist.Nnode(0)
# llinklist.Nnode(1)
# llinklist.Nnode(2)
# llinklist.Nnode(3)
# llinklist.Nnode(7)
# llinklist.Nnode(11)
#llinklist.nth(2)
#llinklist.countNodes()
#llinklist.delnth(3)
#llinklist.mid()
#llinklist.rep(2)
#llinklist.loop()
#llinklist.floyd()
llinklist.removeLoop()
'''
'''
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
      temp = self.head

      if temp is not None:
        if temp.data == key :
          self.head = temp.next
          temp = None
          return

      while( temp is not None)    :
        #traverse
        if temp.data == key:
          break
        prev = temp
        temp = temp.next  

      if temp is None:
        return

      

      prev.next = temp.next

      temp = None  

    def countNodes(self)  :
      temp = self.head
      count = 0

      if temp is None:
        count = 0
        

      while(temp) :
        temp = temp.next
        count = count + 1
            

      print('Count is ',count)

    def search(self, key):
      temp =  self.head

      while( temp is not None):
        if temp.data == key:
             
          return True
        temp = temp.next
      return False 

    def Nnode(self,pos):
      temp = self.head
      if temp is None:
        print('No value')
      if pos == 0:
        print('value is ',temp.data)  

             
      else:
        for _ in range(pos):
          temp = temp.next
          if temp is None:
            print('No value')   
            return         
           
        
             
        print('value is ',temp.data) 

    def nth(self, n):
      temp = self.head

      length = 0
      
      while temp is not None:
        temp = temp.next
        length = length + 1
      if n > length:
        print('No such value')
        return

      if n == 0:
        print('No such value') 
        return 

      temp = self.head
      for _ in range(0,length-n):
        temp = temp.next
      print('value  is',temp.data) 


    def delnth(self,x) :
      #first find nth node from back
      length = 0
      temp = self.head
      
      while(temp):
        temp = temp.next
        length+=1

      if x > length :
        return

      if x == 0:

        return
      temp = self.head
      # for _ in range(0, length-n) :
      #   temp = temp.next
      #   return temp
      pos = length-x

      for _ in range(pos-1):
        temp = temp.next

      next = temp.next.next

      

      temp.next = None
      temp.next = next
      
    def mid(self) :
      length = 0

      temp = self.head

      while(temp):
        temp = temp.next
        length+=1

      
      if length % 2 == 0:
        temp = self.head
        new_pos = length // 2  

        for _ in range(new_pos-1):
          temp = temp.next
        print('Middle value 1:',temp.data)  
        temp = temp.next
        print('Middle value 2:',temp.data)

      else:
        temp = self.head
        odd_pos = (length + 1) // 2

        for _ in range(odd_pos-1):
          temp = temp.next
        print('Odd number of nodes. Middle value is', temp.data)  

    def rep(self, key):
      temp = self.head
      count = 0

      if temp is None:
        return
      if temp.next is None :
        return

      while(temp):
        if temp.data == key:
          count += 1
        temp = temp.next  
      if count == 1:
        print(f'Repeated {count-1} times')  
      else:  
        print(f'Repeated {count} times')
    

      

    def loop(self) :
      lst = set()
      temp = self.head

      while(temp):
        if temp in lst:
          print('Loop Found')
          break
       
          
        lst.add(temp)
        temp = temp.next

    def floyd(self):
      #two pointers
      slow = self.head
      fast = self.head
      count = 0

      while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        count += 1
        if slow == fast:
          print('Loop found')
          print('no of nodes in loop:',count)
          return

    def removeLoop(self):
      slow = self.head
      fast = self.head
      entry = self.head
      count = 0
          

      while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        
        
        if slow == fast: #loop exists
          while(slow != entry):
            slow = slow.next 
            entry = entry.next          

          print(f'Starting node is {entry.data}') 
          
          #removing loop
          #print(slow.data)
          slow = slow.next
          
          while(slow != entry):
            slow = slow.next
            count += 1

          print(f'No of nodes are {count+1}') 

          for _ in range(count):
            entry = entry.next
          #print(entry.data) 
          entry.next = None
          print('loop: 10->15->4->20->10')
          
          print('Linked list after Loop removal:-')
          entry = self.head
          while(entry):
            print(entry.data)
            entry = entry.next
          
           



          return   
                   
          
           
        
      

    def printList(self):
      temp = self.head
      while(temp):
          print (" %d" %(temp.data),sep='\n'),
          temp = temp.next    

llinklist = LinkedList()
# llinklist.push(2)        
# llinklist.push(4)  
# llinklist.push(2)
# llinklist.push(6)
# llinklist.push(9)
# llinklist.push(11)
# llinklist.push(2)
# llinklist.push(2)
# llinklist.push(45)
# llinklist.push(2)
llinklist.push(20)
llinklist.push(4)
llinklist.push(15)
llinklist.push(10)
llinklist.head.next.next.next.next = llinklist.head
#llinklist.printList()
#llinklist.deleteNode(4)
#llinklist.deleteNode(2)
#llinklist.printList()
#llinklist.countNodes()
# if llinklist.search(7):
#   print('found')
# else:
#   print('Nope')  
# llinklist.Nnode(0)
# llinklist.Nnode(1)
# llinklist.Nnode(2)
# llinklist.Nnode(3)
# llinklist.Nnode(7)
# llinklist.Nnode(11)
#llinklist.nth(2)
#llinklist.countNodes()
#llinklist.delnth(3)
#llinklist.mid()
#llinklist.rep(2)
#llinklist.loop()
#llinklist.floyd()
llinklist.removeLoop()

'''
'''
#Finding the intersection pt of two linkedlist nodes

# best approach --> 

let's say we have two linkedlists A, B and C

temp1 = self.headA
temp2 = self.headB

while(temp1 != temp2):
  temp1 = temp1.next
  temp2 = temp2.next
  if(temp1 == None):
    temp1 = self.headB
  elif(temp2 == None):
    temp2 = self.headA
return temp1  

'''

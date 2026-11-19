'''
LINKED LISTS:
    1. single/ singly linked list
      a. insert data from begin
      b. insert data from end
      c. delete data from begin
      d. delete data from end
      e. insert data from position
      f. delete data from position
      g. delete data from value
    2. Double / doubly linked list
    3. Cirular linked list'''

#SLL insert from begining
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head= None
n= int(input("Enter number of nodes:"))
for i in  range(n):
    data=int(input("Enter values:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''



#SLL insert from end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next= None
head=None
n=int(input("Enter number of Nodes:"))
for i in range(n):
    data=int(input("Enter values:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''


#SLL (insert at end delete at beginning)
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter a value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL:before delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
#delete at begining
if head is None:
    print("SLL empty.......")
else:
    head=head.next
    
print("SLL:before delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#SLL (insert at end delete at end)
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL: before delete")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
#delete at end
if head is None:
    print("SLL empty....")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None

print("SLL:after delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#insert at position 
'''class node:
    def __init__(self,data):
        self.data= data
        self.next= None 
head = None 
n = int(input("Enter number of nodes : "))
for i in range(n):
    data = int(input("Enter a value : "))
    newnode = node(data)
    newnode.next = head
    head= newnode
print("SLL: before insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")
pos= int(input("Enter the position :"))
data = int(input("enter the data "))
newnode= node(data)
if pos==1 :
    newnode.next= head 
    head= newnode 
else:
    temp= head 
    count= 1 
    while temp and count <pos-1 :
        temp= temp.next 
        count+=1 
    if temp is None :
        print("Invalid position")
    else:
        newnode.next= temp.next 
        temp.next = newnode 
print("SLL: after insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")'''

#delete a value in a SLL by position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("After insertion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")

pos=int(input("enter position:"))
if pos<1 or head is None:
    print("Invalid position")
elif pos==1:
    head=head.next
else:
    temp=head
    count=1
    while temp.next and count<pos-1:
        temp=temp.next
        count+=1
    if temp.next is None:
        print("Invalid position")
    else:
        temp.next=temp.next.next
print("After deletion")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''


#delete by value
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("After insertion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")

value=int(input("enter value to be deleted:"))
if head is None:
    print("SLL is empty")
elif head.data==value:
    head=head.next
else:
    temp=head
    while temp.next and temp.next.data !=value:
        temp=temp.next
    if temp.next is None:
        print("value not found")
    else:
        temp.next= temp.next.next
print("after deletion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")'''

#Reverse a linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("After insertion:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")

prev=None
current =head
while current:
    nextnode=current.next
    current.next=prev
    prev =current
    current =nextnode
head=prev

print("Reverse SLL:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")







        
    













        

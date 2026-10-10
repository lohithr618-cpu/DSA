#natural number
#EVEN number
'''n=int(input("enter n: "))
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")'''

#odd numbers
'''n=int(input("enter n: "))
for i in range(1,n+1):
    if i%2==1:
        print(i,end=" ")'''

#2-D data
#square pattern with *,numbers
'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()'''

'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()'''

''''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        print((i,j),end=" ")
    print()'''

#hollow square pattern
'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#x pattern
'''n=int(input("entr n :"))
for i in range(n):
    for j in range(n):
        #if i==j or i+j==n-1:
        if i==j or j=n-1-i
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hollw with x pattern
'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#butterfly pattern
'''n=int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#sir task
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0  or j==n-1 or i==n//2 or j==n//2:#or i==n-3 or j==n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#star pattern
n=int(input("enter n :"))
#b=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:#or i==b or j==b
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    








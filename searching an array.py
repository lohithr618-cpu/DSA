#searching in array 1D/2D
'''1.search an element and return its index value  in a 1-D array'''

'''arr=list(map(int,input("enter values:").split()))
search =int(input("enter element to search:"))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print("elements found at :",i)
        found=True
        break
if  not found:
    print("element out of range")'''


#search element in 2-D array
'''n=int(input("enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
search=int(input("enter element to be search:"))
found=False
for i in range(n):
    for j in range(n):
        if arr[i][j]==search:
            print("element found at  row :",i,"col",j)
            found=True
            break
if not found:
    print("element out of range")'''


#sum of the matrix 
'''n=int(input("enter the size"))
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        s+=arr[i][j]
print("total:",s)'''

#sum of rows and colomuns
'''n=int(input("enter the size:"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
    print("row:",i+1,"sum:",s)
print()
for j in range(n):
    s=0
    for i in range(n):
        s+=arr[i][j]
    print("col:",j+1,"sum:",s)'''


#sum of diagonal and anti diagnol(X)
n=int(input("enter size:"))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            di+=arr[i][j]
        if i+j==n-1:
            ad+=arr[i][j]
print("daignol sum:",di)
print("anti diagonal sum:",ad)

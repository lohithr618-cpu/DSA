#data types in one roof
'''arr=[1,2,3,4,5]
arr=["lohiht","krishna"]
arr[True,False,True]
complex=[2+5i,6+5i]'''

#1D-2D-multi Dimen

#traverence a array and add 100 to each elements
'''arr=list(map(int,input("enter elements:").split()))
for val in arr:
    print(val+100,end=" ")'''

#summate the value in an array
'''arr=list(map(int,input("enter elements:").split()))
total=0
for i in arr:
    total+=i
print("sum:",total)'''

#maximum value in an array
'''arr=list(map(int,input("enter elements:").split()))
max=arr[0]
for val in arr:
    if val> max:
        max=val
print("largest value:",max)'''

#min value in an arr
'''arr=list(map(int,input("enter elements:").split()))
min=arr[0]
for val in arr:
    if val<min:
        min=val
print("min value:",min)'''

#reverse an arr without builtin
'''arr=list(map(int,input("enter  elements:").split()))
for val in range(len(arr)-1,-1,-1):
    print(arr[val],end="")'''

#remove the duplicates in arr
'''arr=list(map(int,input("enter elements:").split()))
result=[]
for val in arr:
    if val not in result:
        result.append(val)
print(*result)'''

#print count of even and odd
#self 
'''arr=list(map(int,input("enter elements:").split()))
even=[]
odd=[]
for val in arr:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(len(even))
print(len(odd))'''

#sir code
'''arr=list(map(int,input("enter elements:").split()))
even,odd=0,0
for val in arr:
    if val%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd",odd)'''

#rotate an array clock wise direction
'''arr=list(map(int,input("enter elements:").split()))
k=int(input("enter rotation:"))
k%=len(arr)
arr=arr[k:]+arr[:k]
print(*arr)'''


#rotate in anticlock wise direction
'''arr=list(map(int,input("enter elements:").split()))
k=int(input("enter rotation:"))
k%=len(arr)
arr=arr[-k:]+arr[:-k]
print(*arr)'''



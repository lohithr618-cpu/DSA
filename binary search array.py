#search in a rotated array
'''arr=list(map(int,input().split()))
search=int(input("enter a value to be searched: "))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==search:
        ans=mid
        break
    if arr[low]<=arr[mid]:
        if arr[low]<=search<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if arr[mid]<search<=arr[high]:
            low=mid+1
        else:
            high=mid-1
print(ans)'''

#finding the first occurrence of a number
'''arr=list(map(int,input("enter elements ").split()))
num=int(input("enter a value to be searched:"))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==num:
        ans=mid
        high=mid-1
    elif arr[mid]<num:
        low=mid+1
    else:
        high=mid-1
print("lowest occurrence index:",ans)'''

#finding the last occurrence of a number
'''arr= list(map(int, input("Enter elements ").split()))
num= int(input("Enter a value to be searched : "))
low= 0 
high = len(arr)-1
ans= -1 
while low<= high:
    mid= (low+high)//2
    if arr[mid]== num:
        ans= mid 
        low= mid+1 
    elif arr[mid]<num :
        low= mid+1
    else:
        high= mid-1 
print("highest  occurrence index :", ans)'''

#finding the count of occurrence of a number
arr=list(map(int,input("enter elements:").split()))
num=int(input("enter a value to be scared :"))
low=0
high=len(arr)-1
first,last=-1,-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=num:
        if arr[mid]==num:
            first=mid
        high=mid-1
    else:
        low=mid+1
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]<=num:
        if arr[mid]==num:
            last=mid
        low=mid+1
    else:
        high=mid-1
print(last-first+1 if first!=-1 else 0)












































#Types of searches
'''1.linear
   2.binary
   3.jump search'''


#binary search
'''arr=list(map(int,input("enter elements:").split()))
arr.sort()
val=int(input("enter element to be search:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        print("elements found at",mid)
        break
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("element not found")'''

#find the square root of a number using binary search pattern
val=int(input("enter a element to search: "))
low=0
high=val
while low<=high:
    mid=(low+high)//2
    if mid*mid==val:
        print("square root is:",mid)
        break
    elif mid*mid<val:
        low=mid+1
    else:
        high=mid-1
else:
    print("integer square root ",high)




#approches:
''' 1.Math
    2.Naive
    3.BruteForce
    4.greddy
    5.BackTracking'''

#Strong Number
'''n=int(input("enter a number :"))
copy=n
total=0
while n!=0:
    d=n%10
    f=1
    i=1
    while i<=d:
        f*=i
        i+=1
    total+=f
    n//=10
if total==copy:
    print(copy,"is a StrongNumber")
else:
    print(copy,"is not a Strong Number")'''

#1/21+2/3!+3/4!+4/5!=......n
'''n=int(input("enter a number:"))
total=0
f=1
for i in range(1,n+1):
    f*=i+1
    total+=i/f
print("sum:",total)'''

#naive approch-find the occrances of a number
'''arr=list(map(int,input("enter elements:").split()))
value=int(input("eneter value:"))
count=0
for i in arr:
    if i==value:
        count+=1
print(value,"occarance are:",count)'''

#bruteforce approach-find the posibilities
arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target:"))
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            count+=1
print(count)
        


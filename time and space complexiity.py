#O(1) - constant time complexxity,space complexxity O(1)
'''n=int(input("enter n :"))
print(n+100)'''

#O(n)-linear time cmomplexity  ,space complexity O(1)
'''n=int(input("enter n:"))
for i in range(1,n+1):
    print(i,end=" ")'''

#O(n)-linear time complexity O(n)and space complexity O(n)
'''n=int(input("enetr n:"))
arr=[]
for i in range(n):
    num=int(input("enter a value:"))
    arr.append(num)
print("list",arr)'''

#O(n^2) quadratic/pascals triangle TC
'''n=int(input("enter n:"))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()'''

#logarthmic TC ->O(logn)SC->O(1)
'''n=int(input("enter n:"))
while n>1:
    print(n)
    n//=2
print(1)'''

#logarthmic TC nlogn
'''n=int(input("enter n:"))
for i in range(n):
    j=n
    print(j)
    while j>1:
        j//=2
        print(j)
print("done")'''

#O(2^n) exponentional  time complexity
def count(n):
    if n==0:
        return 1
    return count(n-1)+count(n-1)
n=int(input("enter a num: " ))
print("result :",count(n))

        

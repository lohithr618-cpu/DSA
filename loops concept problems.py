#write a program to add the digits of a given number
'''n=int(input("enter a number:"))
s=0
while n!=0:
    d=n%10
    s+=d
    n//=10
print("sum:",s)'''

#write a program to reverse a given number
'''n=int(input("\nEnter a  number : "))
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)'''

#generate n even number :
n=int(input("enter n : "))
i=1
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1

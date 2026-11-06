#Recursions

#direct
'''def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)
n=int(input("enter n :"))
numbers(n)'''

#direct recursions-factorial of a num
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter n:"))
print("factorial :",fact(n))'''



#indirect recursion
'''def one(n):
    if n<=0:
        return
    print("one:",n)
    two(n-1)
def two(n):
    if n<=0:
        return
    print("two:",n)
    one(n-1)
n=int(input("enter n:"))
one(n)'''

'''def even(n):
    if n==0:
        print(num,"is even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(num,"is odd")
        return
    even(n-1)
n=int(input("enter n:"))
num=n
even(n)'''

def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    fun(n-1)
n=int(input("enter n:"))
fun(n)

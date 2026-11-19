#edge cases
#robustness
#comparator thinking

'''
test cases
10 20 30 -20
5 5 5 -
5-
20 20 10 10 5
-9 -3 -1
[]
'''

#second largest
'''arr=list(map(int,input("enter elements:").split()))
if len(arr)<2:
    print("not enought elements ")
else:
    largest=float('-inf')
    second= float('-inf')
    for val in arr:
        if val>largest:
            second=largest
            largest= val
        elif val>second and val !=largest :
            second = val
    if second==float('-inf'):
        print("No second value exits")
    else:
        print("Second largest",second)'''

#tom riddles anagram
'''s1=input("enter first string:").lower().replace(' ','')
s2=input("enter second string:").lower().replace(' ' ,'')
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print(" Tom Riddles Anagram ")
    else:
        print("Not")
else:
    print("Not")'''


'''s1=input("enter first string:").lower().replace(' ','')
s2=input("enter second string:").lower().replace(' ' ,'')
s1=''.join(ch for ch in s1 if ch.isalpha())
s2=''.join(ch for ch in s2 if ch.isalpha())
if len(s1)==0 or len(s2)==0:    #empty braces
    print("Not Tom Riddles Anagram")
elif len(s1)==1 or len(s2)==1:   #for single character
    print("Not Tom riddles Anagram")
elif len(s1)!=len(s2):
    print("Not Tom Riddles Anagram")
elif len(set(s1))==1 or  len(set(s2))==1:
    print("Not Tom Riddles Anagram")
elif sorted(s1)==sorted(s2):
        print(" Tom riddles Anagram")
    
else:
    print("Not")'''

#Robustness
arr=[11,22,33,44]
index =int(input("enter index:"))
if 0<=index<len(arr):
    print(arr[index])
else:
    print("invalid index")












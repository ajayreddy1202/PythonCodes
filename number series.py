#Number series programs 23/08/25
'''n=int(input("n:"))
even=2
odd=1
for i in range(1,n+1):
    if i%2!=0:
        print(even,end=" ")
        even+=2
    else:
        print(odd,end=" ")
        odd+=2'''



'''n=int(input("n:"))
x=1
for i in range(1,n+1):
    print(x,end=" ")
    x=x+3'''



'''n=int(input("n:"))
for i in range(1,n+1):
    print(n,end=" ")
    n=n*2'''



'''n=int(input("n:"))
for i in range(1,n+1):
    if i%2==0:
        print(i**3,end=" ")
    else:
        print(i**2,end=" ")'''



'''n=int(input("n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact,end=" ")'''



'''n=int(input("n:"))
left=10
right=1
for i in range(1,n+1):
    if i%2!=0:
        print(left,end=" ")
        left-=1
    else:
        print(right,end=" ")
        right+=1'''



'''n=int(input("n:"))
for i in range(1,n+1):
    print(bin(i)[2:],end=" ")'''



#Number series programs 28/08/25
'''num=int(input("n:"))
n1=0
n2=1
if num<=0:
    print("enter the number above zero",end=" ")
elif num==1:
    print(n1,end=" ")
else:
    print(n1,end=" ")
    print(n2,end=" ")
    for i in range(2,num):
        r=n1+n2
        n1=n2
        n2=r
        print(r,end=" ")'''



'''num=int(input("Enter the number:"))
n=1
str="*"
char=97
for i in range(num):
    print(n,end=" ")
    n+=1
    print(str,end=" ")
    if char<=122:
        print(chr(char),end=" ")
        char+=1
    else:
        char=97'''
    


'''n = int(input("Enter how many prime numbers you want: "))
count = 0   
num = 2    
print("First", n, "prime numbers are:")

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1'''



'''n = int(input("Enter n: "))
for i in range(1, n+1):
    pos = (i-1) % 15 + 1  
    if pos <= 5:
        print(pos, end=" ")
    elif pos <= 10:
        print("*", end=" ")
    else:
        print(chr(65 + (pos - 11)), end=" ") '''



'''s = "ajayreddy"
num = int(input("Enter num: "))
length = len(s)

for i in range(num):
    ch = s[i % length]   
    if (i+1) % 2 == 0:   
        print(ch.upper(), end=" ")
    else:                
        print(ch.lower(), end=" ")'''



















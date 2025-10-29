#swaping of two numbers
'''a=int(input('a:'))
b=int(input('b:'))
print(f"Before swap\na:{a}\tb:{b}")
c=a
a=b
b=c
print(f"After swap\na:{a}\tb:{b}")'''



'''a=int(input('a:'))
b=int(input('b:'))
print(f"Before swap\na:{a}\tb:{b}")
a=a+b
b=a-b
a=a-b
print(f"After swap\na:{a}\tb:{b}")'''



#swaping of three numbers
'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"a:{a}\tb:{b}\tc:{c}")
d=a
a=c
c=b
b=d
print(f"a:{a}\tb:{b}\tc:{c}")'''



'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"a:{a}\tb:{b}\tc:{c}")
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print(f"a:{a}\tb:{b}\tc:{c}")'''



'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"a:{a}\tb:{b}\tc:{c}")
a,b,c=c,a,b
print(f"a:{a}\tb:{b}\tc:{c}")'''



'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"a:{a}\tb:{b}\tc:{c}")
a=a*b*c
b=a//(b*c)
c=a//(b*c)
a=a//(b*c)
print(f"a:{a}\tb:{b}\tc:{c}")'''



'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"a:{a}\tb:{b}\tc:{c}")
a=a^b^c
b=a^b^c
c=a^b^c
a=a^b^c
print(f"a:{a}\tb:{b}\tc:{c}")'''



#Entered integer is odd or even
'''n=int(input("n:"))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''



'''n=int(input("n:"))
if n%2!=0:
    print(f"{n} is odd")
else:
    print(f"{n} is even")'''


'''n=int(input("n:"))
if (n//2)*2==n:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''



'''n=int(input("n:"))
if (n//2)*2==n-1:
    print(f"{n} is odd")
else:
    print(f"{n} is even")'''



'''n=int(input("n:"))
if n&1==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''



'''n=int(input("n:"))
if n&1!=0:
    print(f"{n} is odd")
else:
    print(f"{n} is even")'''



'''n=int(input("n:"))
if n&1==1:
    print(f"{n} is odd")
else:
    print(f"{n} is even")'''



'''n=int(input("n:"))
if n|1==n+1:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''



'''n=int(input("n:"))
if n|1==n:
    print(f"{n} is odd")
else:
    print(f"{n} is even")'''



'''n=int(input("n:"))
if n|1!=n:
    print(f"{n} is even")
else:
    print(f"{n} is odd")'''



#given number is amstrong number or not 18/08/25
'''num=153
res=0
temp=num
while num!=0:
    rem=num%10
    res=res+rem**3
    num=num//10
if temp==res:
    print("amstrong number")
else:
    print("not an amstrong number")'''



#factorial number
'''n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of",n,"is ->",fact)'''



#strong number or not
'''num=145
temp=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    res=res+fact
    num=num//10
if temp==res:
    print("strong number")
else:
    print("not a strong number")'''



#find the sum of given number    
'''n=int(input("enter number:"))
res=0
while n!=0:
        num=n%10
        res+=num
        n=n//10
        print(res)'''



#given number is perfect number or not
'''n=int(input("enter number:"))
res=0
for i in range(1,n):
    if n%i==0:
        res+=i
if n==res:
    print("perfect")
else:
    print("not perfect")'''



#Given number is palindrom number or not 19/08/25
'''n=int(input("enter the number:"))
n=str(n)
if n==n[::-1]:
    print("palindrom number")
else:
    print("not palindrom number")'''



'''n=int(input("number:"))
res=""
temp=n
while n>0:
    la=n%10
    res=res+str(la)
    n=n//10
print("Reverse the number:",res)
if temp==int(res):
    print("palindrom number")
else:
    print("not palindrom number")'''



'''n=int(input("number:"))
temp=n
res=0
while n!=0:
    rem=n%10
    res=res*10+rem
    n=n//10
print("Reverse the number:",res)
if temp==res:
    print("palindrom number")
else:
    print("not palindrom number")'''



#write a program frequency of each number from given number
'''n=int(input("enter number:"))
d={}
while n!=0:
    rem=n%10
    if rem not in d:
        d[rem]=1
    else:
        d[rem]+=1
    n=n//10
for i,j in d.items():
    print(i,"->",j)'''



#write a program to check given number disarium number or not
'''n=int(input("enter the number:"))
val=n
temp=n
cnt=0
res=0
while temp!=0:
    cnt+=1
    temp=temp//10
print("count->",cnt)

while val!=0:
    rem=val%10
    res=res+rem**cnt
    val=val//10
    cnt=cnt-1
if res==n:
    print("Disarium number")
else:
    print("not disarium number")'''



#program to find superdigit of a given number
'''n=int(input("enter the number:"))
while n>=10:
    res=0
    x=n
    while x!=0:

        la=n%10
        res+=la
        x=x//10
        n=res
print(n)'''



#write a program to given number is automaphic number or not 20/08/25
'''num=int(input("enter number:"))
a=str(num)
num1=num**2
b=str(num1)
if b.endswith(a):
    print("automaphic number")
else:
    print("Not automophic number")'''



'''n=int(input("enter number:"))
temp=n
c=10
flag=False
sq=n*n
while n!=0:
    rem=sq%c
    if temp==rem:
        flag=True
        break
    c=c*10
    n=n//10
if flag==True:
    print("Automorphic number")
else:
    print("Not Automorphic number")'''



#write a program given number is mirror number or not
'''n = int(input("Enter the number: "))
cnt = 0
temp = n
while n != 0:
    cnt += 1
    n = n // 10
print("Total digits:", cnt)
if cnt % 2 == 0:   
    first_half = temp // (10 ** (cnt // 2))
    second_half = temp % (10 ** (cnt // 2))
else:   
    first_half = temp // (10 ** ((cnt // 2) + 1))
    second_half = temp % (10 ** (cnt // 2))
rev = 0
sec = second_half
while sec != 0:
    rev = rev * 10 + sec % 10
    sec //= 10

if first_half == rev:
    print(temp, "is a Mirror Number")
else:
    print(temp, "is NOT a Mirror Number")'''



'''n=int(input("enter the number:"))
cnt=0
temp=n
while n!=0:
    cnt+=1
    n=n//10
print(cnt)
if cnt%2==0:
    print(temp%10**(cnt//2))'''



#write a program maximum number to given anumber 21/08/25
'''n=int(input("enter the number:"))
max_ele=0
while n!=0:
    rem=n%10
    if rem>max_ele:
        max_ele=rem
    n=n//10
print("max element is->",max_ele)'''



#write a program to print 2 maximum numbers and display its difference
'''num = int(input("Enter a number: "))
max1 = 0
max2 = 0
while num > 0:
    rem = num % 10  
    if rem > max1:
        max2 = max1
        max1 = rem
    elif rem > max2:
        max2 = rem
    num = num // 10 

print("First maximum digit:", max1)
print("Second maximum digit:", max2)
print("Difference:", max1 - max2)'''
 


#write a program to check given number is facinating number or not
'''n=int(input("enter:"))
res=""
for i in range(1,4):
    res=res+str(n*i)
arr=sorted(res)
a=['1','2','3','4','5','6','7','8','9']
if a==arr:
    print("fasinating number")
else:
    print("not fasinating number")'''



'''n=int(input("enter:"))
l1=[0]*10
print(l1)
n1=n
n2=n*2
n3=n*3
print(n1)
print(n2)
print(n3)

while n1!=0:
    rem=n1%10
    l1[rem]+=1
    n1=n1//10

while n2!=0:
    rem=n2%10
    l1[rem]+=1
    n2=n2//10

while n3!=0:
    rem=n3%10
    l1[rem]+=1
    n3=n3//10

print(l1)
for i in range(1,len(l1)):
    if l1[i]!=1:
        print("Not a facinating number")
        break
else:
    print("facinating number")'''



#write a program to check given number is a prime number or not 22/08/25
'''n=int(input("enter:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime nmber")
else:
    print("enter the valid number")'''



#write a program to convert given number into its binary format
'''n=int(input("enter:"))
temp=1
bi=0
while n!=0:
    rem=n%2
    bi=bi+temp*rem
    temp=temp*10
    n=n//2
print("Binary value is->",bi)'''



#write a program to check the given number is a evil number or not
'''n=int(input("enter:"))
count=0
temp=1
bi=0
while n!=0:
    rem=n%2
    if rem==1:
        count+=1
        bi=bi+temp*rem
    temp=temp*10
    n=n//2
print(bi)
if count%2==0:
    print("evil number")
else:
    print("not a evil number")'''



'''n=int(input("enter:"))
cnt=0
while n!=0:
    rem=n%2
    if rem==1:
        cnt+=1
    n=n//2
if cnt%2==0:
    print("evil number")
else:
    print("not evil number")'''



# Program to convert binary to decimal without using inbuilt functions
'''binary=input("Enter a binary number: ")
decimal=0
power=len(binary)-1  

for digit in binary:
    if digit=='1':
        decimal+=2**power
    power-= 1

print("Decimal value:",decimal)
'''































































































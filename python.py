'''l1=[10,20,30,40]
l2=[10,20.3,2+5j,True]
print(type(l1))
print(type(l2))'''

'''l1=[10,20,30,40,30,20,10]
print(l1,len(l1))'''

'''l=[10,20,30,40,50]
print(l,l[0])'''

'''l=[10,20,30,40,50]
print(l[-1])'''

'''l=[10,20,30,40,50]
print(l[::])
print(l[-1::-1])'''

'''l=[10,20,30]
l[0]="ajay"
print(l)'''

'''l=[10,20,30,40,50,60]
for i in l:
    print(i,end=" ")'''

'''l=[10,20,30,40,50,60]
for i in range(len(l)):
    print(l[i],end=" ")'''

'''l=[10,20,30,40,50,60]
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")'''

'''l=[10,20,30,40,50,60]
i=0
while i<len(l):
    print(l[i],end=" ")
    i+=1'''

'''l=[10,20,30,40,50,60]
l.clear()
print(l)'''

'''l=[10,20,30,40,50,60]
print(l)
l1=l.copy()
print(l1)'''

'''l=[10,20,30,40,50,20]
l1=l.count(20)
print(l1)'''

'''l=[10,20,30,40,50,60]
l.append(100)
l.append("ajay")
print(a)'''

'''l=[10,20,30,40,50,60]
l.append([1,2,3])
l.extend([1,2,3])
print(l)'''

'''l=[10,20,30,40,50,60]
l.append('don')
l.extend('don')
print(l)'''

'''l=[10,20,30,40]
l.insert(3,50)
print(l)'''

'''l=[10,20,30,40]
l.insert(-3,50)
print(l)'''

'''l=[10,20,30,40]
l.insert(100,500)
print(l)'''

'''l=[10,20,30,40]
l1=l.pop(2)
print(l1)
print(l)'''

'''l=[10,20,30,40]
l1=l.pop()
print(l1)
print(l)'''

'''l=[10,20,30,40]
l1=l.pop(1000)
print(l1)
print(l)'''

'''l=[10,20,30,40]
l.remove(30)
print(l)'''

'''l=[10,20,30,40]
l.remove(100)
print(l)'''

'''l=[10,20,30,[1,2,3]]
l[3].remove(3)
print(l)'''

'''l=[10,2,30,6]
l.sort()
print(l)
l.sort(reverse=True)
print(l)'''

'''l=['bhumana','reddy','ajay']
l.sort()
print(l)
l.sort(reverse=True)
print(l)'''

'''l=[10,5.4,5+3j,True]
l.reverse()
print(l)'''

'''l=[10,20,30,40]
l1=l.index(10)
print(l1)
l2=l.index(30,0,3)
print(l2)'''

'''l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
l4=l1*4
print(l4)'''

'''t=(10,20,30)
t[1]="py"
print(t)'''

'''t=(10,20,30,20,10)
t1=t.count(10)
print(t1)'''

'''t=(10,20,30,40)
t1=t.index(20)
print(t1)
t2=t.index(30,0,len(t))
print(t2)
t3=t.index(100)
print(t3)'''

'''t=(10,20,30,40)
for i in range(0,len(t)):
    print(t[i],end=" ")'''

'''t=(10,20,30,40)
for i in t:
    print(i,end=" ")'''

'''t=(10,20,30,40)
i=0
while i<len(t):
    print(t[i],end=" ")
    i+=1'''

'''print((1,2,3)+(4,5,6))
print((1,2,3)*3)'''

'''s={23,78,23,90,54}
s.add(23)
print(s)'''

'''s={23,78,23,90,54}
s.add("python")
print(s)'''

'''s={23,78,23,90,54}
p=s.pop()
print(s,p)
p1=s.pop()
print(s,p1)'''

'''s={23,78,9.9,54}
s.remove(9.9)
print(s)'''

'''s={23,78,9.9,54}
s.remove(23,54)
print(s)'''

'''s={23,78,9.9,54}
s.remove(100)
print(s)'''

'''s={23,78,9.9,54}
s.discard(100)
print(s)'''

'''s={23,78,9.9,54}
s.discard(9.9)
print(s)'''

'''s={23,78,9.9,54}
s.discard(23,78)
print(s)'''

'''s1={12,36,49,50}
s2={33,99,17,12}
s3=s1.union(s2)
print(s3)'''

'''s1={12,36,49,50}
s2={33,99,17,12}
s1.update(s2)
print(s1)
print(s2)
'''

'''s1={12,36,49,50,33}
s2={33,99,17,12,36}
res=s1.intersection(s2)
print(res)'''

'''s1={12,36,49,50,33}
s2={33,99,17,12,36}
s1.intersection_update(s2)
print(s1)'''

'''s1={12,36,49,50,33}
s2={33,99,17,12,36}
res=s1.difference(s2)
print(res)'''

'''s1={12,36,49,50,33}
s2={33,99,17,12,36}
s1.difference_update(s2)
print(s1)'''

'''s1={1,2,3,4,5,10,40}
s2={10,20,30,40,50,1,3}
print(s1)
s1.intersection_update(s2)
print(s1)'''

'''s1={1,2,3,4,5,10,40}
s2={10,20,30,40,50,1,3}
res=s1.difference(s2)
print(res)'''

'''s1={1,2,3,4,5,10,40}
s2={10,20,30,40,50,1,3}
s1.difference_update(s2)
print(s1)'''

'''s1={1,2,3,4,5,10,40}
s2={10,20,30,40,50,1,3}
res=s1.symmetric_difference(s2)
print(res)'''    
    
'''s1={1,2,3,4,5,10,40}
s2={10,20,30,40,50,1,3}
print(s1)
s1.symmetric_difference_update(s2)
print(s1)'''   

'''s1={1,2,3,4,5,6}
s2={2,4}
s3={2,100,3}
print(s1.issuperset(s2))
print(s1.issuperset(s3))'''

'''s1={1,2,3,4,5,6}
s2={2,4}
s3={2,100,3}
print(s2.issubset(s1))
print(s3.issubset(s1))'''

'''s1={1,2,3,4,5,6}
s2={10,20,30,40}
s3={100,200,4}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))'''  

'''s={1,2.4,"apple",3+5j} 
s.clear()
print(s) '''  

'''s={"red","green","blue"}
s2=s.copy()
print(s2)
print(s)'''

'''d1={'ename':'sneha','exp':3}
for i in d1:
    print(i)

for k in d1:
    print('key=',k,', value=',d1[k])'''

'''d={'id':101,'sal':1000}
d.clear()
print(d)'''

'''d1={'id':101,'sal':1000}
d2=d1.copy()
print('before updation')
print(d1,d2,sep='\n')
d1['sal']=5000
print('after updation')
print(d1,d2,sep='\n')'''

'''d1={'id':101,'sal':1000}
amount=d1.get('sal')
print(amount)'''

'''d1={'id':101,'sal':1000}
list=d1.items()
print(list)'''

'''d1={'id':101,'sal':1000}
list=d1.keys()
print(list)'''

'''d1={'id':101,'sal':1000}
list=d1.values()
print(list)'''

'''d={}
t=('id','sal')
v=(100)
emp=d.fromkeys(t,v)
print(emp)'''

'''d1={'id':101,'sal':1000}
d1.update({'id':202,'exp':5})
print(d1)'''

'''d1={'id':101,'sal':1000}
val=d1.setdefault('sal')
print(val)
print(d1)'''

'''d1={'id':101,'sal':1000}
val=d1.setdefault('sal',900)
print(val)'''

'''d1={'id':101,'sal':1000}
val=d1.setdefault('exp')
print(d1)
print(val)'''

'''d1={'id':101,'sal':1000}
val=d1.setdefault('loc','banguluru')
print(d1)
print(val)'''


'''d1={'id':101,'sal':1000}
v=d1.pop('sal')
print(v)
print(d1)'''

'''d1={'id':101,'sal':1000}
v=d1.popitem()
print(d1)'''

'''s="python"
for i in range(len(s)):
    print(s[i],end=" ")'''

'''s="python"
for i in s:
    print(i,end="\n")'''

'''s="python"
i=0
while i<len(s):
    print(s[i],end="\n")
    i+=1'''

'''s='PYspiderS'
s1=s.upper()
print(s1)'''

'''s='PYspiderS'
s1=s.lower()
print(s1)'''

'''s="PYspiderS"
s1=s.swapcase()
print(s1)
print(s)'''

'''s="ajAY a@bhumANa r9eddY VishNU"
s1=s.title()
print(s1)'''

'''s="ajay reddy"
s1=s.capitalize()
print(s1)'''

'''s="BHUana AjaY REdDy "
s1=s.lower()
print(s1)
s2=s.casefold()
print(s2)'''

'''s="roses are beautiful"
c=s.count("e")
print(c)
c1=s.count("ea")
print(c1)
c2=s.count("z")
print(c2)
c3=s.count("e",4)
print(c3)'''

'''s="roses are beautiful"
i=s.index("t")
print(i)
i1=s.index("ful")
print(i1)
i2=s.index("ar",0,5)
print(i2)'''

'''s="roses are beautiful"
i=s.rindex("a")
print(i)
i1=s.rindex("be")
print(i1)
i2=s.rindex("ar",0,5)
print(i2)'''

'''s="roses are beautiful"
i=s.find("a")
print(i)
i1=s.find("be")
print(i1)
i2=s.find("ar",0,5)
print(i2)'''

'''s="roses are beautiful"
i=s.rfind("a")
print(i)
i1=s.rfind("be")
print(i1)
i2=s.rfind("ar",0,5)
print(i2)'''

'''s="roses are beautiful"
s1=s.split()
print(s1)
s2=s.split("s")
print(s2)
s3=s.split("e",4)
print(s3)
s4=s.split("z")
print(s4)'''

'''s="roses are beautiful"
s1=s.rsplit()
print(s1)
s2=s.rsplit("s")
print(s2)
s3=s.rsplit("e",1)
print(s3)
s4=s.rsplit("z")
print(s4)'''

'''s="roses \nare \nbeautiful"
print(s)
s1=s.splitlines()
print(s1)
s2=s.splitlines(True)
print(s2)'''

'''s="roses are beautiful"
s1=s.partition("u")
print(s1)
s2=s.partition("a")
print(s2)'''

'''s="roses are beautiful"
s1=s.rpartition("u")
print(s1)
s2=s.rpartition("a")
print(s2)'''

'''s="good"
s1=s.center(6)
print(s1)
s2=s.center(7,"*")
print(s2)'''

'''s="god"
s1=s.center(6)
print(s1)
s2=s.center(8,"*")
print(s2)'''

'''s="python"
s1=s.rjust(8)
print(s1)
s2=s.rjust(8,"*")
print(s2)'''

'''s="   python  "
print(len(s))
s1=s.strip()
print(s1,len(s1))'''

'''s="...python.."
print(len(s))
s1=s.strip(".n")
print(s1,len(s1))'''

'''# 1. Print a greeting
def greet():
    print("Hello, welcome to Python!")
greet()'''

'''# 2. Display sum of two fixed numbers
def sum_fixed():
    a, b = 5, 7
    print("Sum =", a + b)
sum_fixed()'''

'''# 3. Print a table of 5
def table_5():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")
table_5()'''

'''# 4. Check even/odd for fixed number
def check_even_odd():
    num = 8
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd()'''

'''# 5. Print stars pattern
def stars():
    for i in range(5):
        print("*" *(i+1))
stars()'''


'''# 1. Return sum of fixed numbers
def sum_fixed():
    return 5 + 7
print(sum_fixed())'''

'''# 2. Return current year (fixed for example)
def get_year():
    return 2025
print(get_year())'''

'''# 3. Return square of fixed number
def square():
    return 6 ** 2
print(square())'''

'''# 4. Return a greeting message
def greet():
    return "Hello, World!"
print(greet())'''

'''# 5. Return factorial of fixed number
def factorial():
    fact, num = 1, 5
    for i in range(1, num+1):
        fact *= i
    return fact
print(factorial())'''


'''# 1. Print sum of two numbers
def sum_nums(a, b):
    print("Sum =", a + b)
sum_nums(5, 3)'''

'''# 2. Print multiplication table of a number
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
table(7)'''

'''# 3. Print greeting for given name
def greet(name):
    print(f"Hello, {name}!")
greet("Ajay")'''

'''# 4. Check if number is positive or negative
def check_sign(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
check_sign(-10)'''

'''# 5. Display reverse of a string
def reverse_str(s):
    print(s[::-1])
reverse_str("Python")'''


'''# 1. Return sum of two numbers
def sum_nums(a, b):
    return a + b
print(sum_nums(5, 3))'''

'''# 2. Return factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(6))'''

'''# 3. Return square of a number
def square(n):
    return n ** 2
print(square(8))'''

'''# 4. Return greatest of two numbers
def greatest(a, b):
    return a if a > b else b
print(greatest(12, 20))'''

'''# 5. Return reversed string
def reverse_str(s):
    return s[::-1]
print(reverse_str("Python"))'''

'''def greet():
    print("hi ajay")
greet()
greet()'''

'''l=[1,4,8,9,3,0]
print(min(l),max(l),sum(l))'''

'''n=int(input("enter:"))
res=[n%2==0,n%3==0,n%4==0]
print(res)
if all(res):
    print("yes")
else:
    print("no")'''

'''n=int(input("enter:"))
res=[n%2==0,n%3==0,n%4==0]
print(res)
if any(res):
    print("yes")
else:
    print("no")'''

'''def add_two_nums():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    print(c)
add_two_nums()'''

'''def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(90)
even_odd(int(input("enter:")))'''

'''def add_two_nums():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    return c
res=add_two_nums()
print(res)'''

'''def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(int(input("enter:"))))'''

'''def greet():
    print("welcome")
res=greet()
print(res)
print(greet)
res()'''

'''sq=lambda x:x**2
print(sq(int(input("enter:"))))'''

'''def add_two_nums(a,b):
    c=a+b
    print(c)
# add_two_nums()
# add_two_nums(34)
# add_two_nums(3,8,9)
add_two_nums(4,8)'''

'''def fun(a,b=9):
    print(a,b)
fun(10)
fun(10,6)'''

'''def fun(b=9,a):
    print(a,b)
fun(12)'''

'''def bio(name,age,place):
    print(name,age,place)
bio(name="ajay",age=21,place="goa")'''

'''def bio(name,age,place="bangalore"):
    print(name,age,place)
bio(name="ajay",age=21)'''

'''def bio(name,age,place="bangalore"):
    print(name,age,place)
bio(name="ajay",21)'''

'''def bio(name,age,place):
    print(name,age,place)
bio(name="ajay",age=34,place="nellore")'''

'''def fun(*a):
    print(a,type(a))
fun()
fun(12)
fun(10,4.5,True)'''

'''def fun(**a):
    print(a,type(a))
fun()
fun(a=56,b="ajay")'''

'''def fun(a,b=9,*c,d,**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
fun(10,20,50,d="ajay",a1=100,b1=200,c1=300)'''

'''def outer_fun():
    def nested_fun():
        print(" nested function")
    nested_fun()
outer_fun()'''

'''def fun():
    a=100
    print("inside the function=>",a)
fun()
print("outside the function=>",a)'''

'''def fun():
    global a
    a=100
    print("inside the function=>",a)
fun()
print("outside the function=>",a)'''

'''def outer():
    a="enclosed"
    def inner():
        b=900
        print(a)
    inner()
outer()'''

'''def outer():
    a=100
    def inner():
        a=200
        print("inside the nested function:",a)
    inner()
    print("outside the nested function:",a)
outer()'''

'''def outer():
    a=100
    def inner():
        nonlocal a
        a=200
        print("inside the nested function:",a)
    inner()
    print("outside the nested function:",a)
outer()'''

'''a=100
def outer():
    print("inside the function:",a)
outer()
print("outside the function:",a)'''

'''s="hello"
print(len(s))'''

'''l=[]
for i in range(1,101):
    l.append(i)
print(l)'''

'''l=[i for i in range(1,11)]
print(l)'''

'''l=[i for i in range(1,11) if i%2==0]
print(l)'''

'''n=int(input("n:"))
l=[i for i in range(1,n+1)]
print(l)'''

'''n=int(input("n:"))
l=[i**2 for i in range(1,n+1)]
print(l)'''

'''n=int(input("n:"))
l=[100 for i in range(1,n+1)]
print(l)'''

'''n=int(input("n:"))
l=[[1,2,3,4] for i in range(1,n+1)]
print(l)'''

'''n=int(input("n:"))
r=int(input("r:"))
l=[[x for x in range(1,r+1)] for i in range(1,n+1)]
print(l)'''

'''n=int(input("n:"))
l=[int(input(f"value {i}:")) for i in range(1,n+1)]
print(l)'''

'''l=[i for i in range(1,5) for j in range(1,5)]
print(l)'''

'''l=["ajay","reddy","bhumana"]
res=[i.upper() for i in l]
print(res)'''

'''t=(i for i in range(1,11))
print(t)'''

'''s={x for x in range(1,11)}
print(s)'''

'''s={int(input("value:")) for i in range(1,5)}
print(s)'''

'''d={i:i**2 for i in range(1,6)}
print(d)'''

'''l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
res=zip(l1,l2)
print(list(res))'''

'''l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
s='ajayreddy'
res=zip(l1,l2,s)
print(list(res))'''

'''l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d={x:y for x,y in zip(l1,l2)}
print(d)'''

'''l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d=dict(zip(l1,l2))
print(d)'''

'''l=[1,2,3,4]
a,b,c,d=l
print(a,b,c,d)
print(l)'''

'''l=[1,2,3,4,5,6,7]
a,b,c,d=l
print(a,b,c,d)'''

'''l=[1,2]
a,b,c,d=l
print(a,b,c,d)'''

'''l=[1,2,3,4,5,6,7]
a,b,*c=l
print(a,b,c)'''

'''l=[1,2,3,4,5,6,7]
a,*b,c=l
print(a,b,c)'''

'''l=[1,2,3,4,5,6,7]
*a,b,c=l
print(a,b,c)'''

'''l=[1,2,3,4,5]
print(l)
print(*l,sep="__")
print(*l)
print(*l,sep="--")'''


'''s=input("enter the string:")
a=s[0].lower()
if a in ['a','e','i','o','u']:
    print("buzz")'''


'''n=int(input("enter the number:"))
if n%3==0 and n%5==0:
    print("macha")'''


'''n=abs(int(input("enter the number:")))
if 100<=n<=999:
    print("YO")'''


'''n=int(input("enter the number:"))
if n%2==0:
    print("even number")
else:
    print("odd number")'''


'''n=int(input("enter the number:"))
if n%10==0:
    print("yes")
else:
    print("no")'''


'''n=int(input("enter:"))
if n%3==0:
    if n%7==0:
        print("divisible by 3&7")
    else:
        print("not divisible by 7")
else:
    print("not divisible by 3" )'''
    

'''gender=input("enter:")
age=int(input("enter:"))
if gender=='male' or gender=='other':
    if age>=18 and age<65:
        print("eligible to vote")
    else:
        print("not eligible to vote")
elif gender=='female':
    if age>=18 and age<=45:
        print("eligible to vote")
    else:
        print("not eligible to vote")
else:
    print("invalid gender")'''
    

'''a=200
b=300
if a>b:
    print("a>b")
elif a==b:
    print("a==b")
else:
    print("a<b")'''


'''s=input("enter:")
a=int(input("enter:"))
b=int(input("enter:"))
match s:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)'''


'''for val in range(1,11,1):
    print(val,end=" ")'''


'''for val in range(-1,-11,-1):
    print(val, end=" ")'''


'''name="ajay reddy bhumana"
for value in name:
    print(value,end=" ")'''


'''for i in range(1,3):
    for j in range(1,3):
        for k in range(1,3):
            print(i,end=" ")
            print(j,end=" ")
            print(k,end=" ")'''


'''i=1
while i<=5:
    print(i,end=" ")
    i+=1'''


'''n=int(input("enter:"))
i=1
while i<=n:
    print(i,end=" ")
    i+=1'''


'''n=int(input("enter:"))
product=1
for i in range(1,n+1):
    product*=i
print(product)'''


'''for i in range(1,11):
    for j in range(1,6):
        if j==3:
            break
        print(i,end=" ")'''


'''for i in range(1,11):
    if i==8 or i==7:
        continue
    print(i,end=" ")'''


'''l=[10,20,30,40,50,60]
for i in l:
    print(i,end=" ")
print()'''


'''for i in range(len(l)):
    print(l[i],end=" ")
print()'''


'''for i in range(len(l)-1,-1,-1):
    print(l[i],end="\n")'''


'''i=0
while i<len(l):
    print(l[i],end=" ")
    i+=1'''


'''l1=[10,20,30,40]
print(l1)
l1.clear()
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
l2=l1.copy()
print(l2)'''


'''l1=[10,20,30,40,10]
print(l1)
res=l1.count(10)
print(res)'''


'''l1=[10,20,30,40]
print(l1)
l1.append(50)
l1.append('don')
l1.append([1,2,3])
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
l1.append([1,2,3,4])
l1.extend([1,2,3,4])
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
l1.insert(2,300)
l1.insert(-1,800)
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
c1=l1.pop()
print(c1)
print(l1)'''


'''l1=[10,20,30,[1,2,3]]
print(l1)
l1[3].remove(3)
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
l1.sort(reverse=True)
print(l1)
l1.sort()
print(l1)'''


'''l1=[10,20,30,40]
print(l1)
l1.reverse()
print(l1)'''


'''l1=[10,20,10,30,40,10,10]
print(l1)
i1=l1.index(10)
print(i1)
i2=l1.index(10,1)
print(i2)
i3=l1.index(10,4,9)
print(i3)'''


'''t=(12,20,30,40,12)
c=t.count(12)
print(c)
c1=t.count(90)
print(c1)'''


'''t=(12,67,12,23)
i=t.index(12)
print(i)
i1=t.index(12,1)
print(i1)
i2=t.index(900)
print(i2)'''


'''t=(12,67,12,23)
for i in range(0,len(t)):
    print(t[i],end=" ")'''


'''t=(12,67,12,23)
for i in t:
    print(i,end=" ")'''


'''t=(12,67,12,23)
i=0
while i<len(t):
    print(t[i],end=" ")
    i+=1'''


'''s={10,20,30,40,50}
s.add("py")
print(s)'''


'''s={10,20,30,40,50}
p=s.pop()
print(p)'''


'''s={10,20,30,40,50}
s.remove(10)
print(s)'''


'''s={10,20,30,40,50}
s.discard(20)
print(s)'''


'''s1={10,20,30,40}
s2={50,60,70,80}
s3=s1.union(s2)
print(s3)'''


'''s1={10,20,30,40}
s2={50,60,70,80}
s1.update(s2)
print(s1)
print(s2)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
res=s1.intersection(s2)
print(res)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
print(s1)
s1.intersection_update(s2)
print(s1)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
res=s1.difference(s2)
print(res)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
print(s1)
s1.difference_update(s2)
print(s1)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
res=s1.symmetric_difference(s2)
print(res)'''


'''s1={10,20,30,40}
s2={30,20,70,80}
print(s1)
s1.symmetric_difference_update(s2)
print(s1)'''


'''s1={10,20,30,40,50}
s2={20,40,50}
s3={40,100}
print(s1.issuperset(s2))
print(s1.issubset(s2))'''


'''s1={10,20,30,40,50}
s2={20,40,50}
s3={40,100}
print(s2.issubset(s1))
print(s3.issubset(s1))'''


'''s1={10,20,30,40,50}
s2={20,40,50}
s3={400,100}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))'''


'''s1={10,20,30,40,50}
s1.clear()
print(s1)'''


'''s1={10,20,30,40,50}
s2=s1.copy()
print(s2)'''


'''d1={'ename':'sneha','exp':3}
for i in d1:
    print(i)
print('..............')
for k in d1:
    print('key=',k,', value=',d1[k])'''


'''d={'id':101,'sal':1000}
d.clear()
print(d)'''


'''d1={'id':101,'sal':1000}
d2=d1.copy()
print(d2)
d1['sal']=50000
print(d1)'''


'''d1={'id':101,'sal':1000}
amount=d1.get('sal')
print(amount)'''


'''d1={'id':101,'sal':1000}
list=d1.items()
print(list)'''


'''d1={'id':101,'sal':1000}
list=d1.keys()
print(list)'''


'''d1={'id':101,'sal':1000}
list=d1.values()
print(list)'''


'''d1={}
t=('id','sal')
v=500
emp=d1.fromkeys(t,v)
print(emp)'''


'''d1={'id':101,'sal':1000}
d1.update({'sal':90000,'exp':3})
print(d1)'''


'''d1={'id':101,'sal':1000}
val=d1.setdefault('exp')
print(val)'''


'''d1={'id':101,'sal':1000}
v=d1.pop('sal')
print(d1)
print(v)'''


'''d1={'id':101,'sal':1000}
v=d1.popitem()
print(d1)
print(v)'''


'''s="python"
for i in range(len(s)):
    print(s[i],end=" ")'''


'''s="python"
for i in s:
    print(i,end=" ")'''


'''s="python"
i=0
while i<len(s):
    print(s[i],end=" ")
    i+=1'''


'''s="aJay ReddY"
s1=s.upper()
print(s1)'''


'''s="aJay ReddY"
s1=s.lower()
print(s1)'''


'''s="aJay ReddY"
s1=s.swapcase()
print(s1)'''


'''s="rOsE's @re bEautiful"
s1=s.title()
print(s)
print(s1)'''


'''s="rOsE's @re bEautiful"
s1=s.capitalize()
print(s1)'''


'''s="rOsE's @re bEautiful"
s1=s.lower()
print(s1)
s1=s.casefold()
print(s1)'''


'''s="rOsE's @re bEautiful"
c=s.count("u")
print(c)'''


'''s="rOsE's @re bEautiful"
i=s.index("u",15,20)
print(i)'''


'''s="rOsE's @re bEautiful"
i=s.rindex("u")
print(i)'''


'''s="rOsE's @re bEautiful"
f=s.find("u")
print(f)'''


'''s="rOsE's @re bEautiful"
f=s.rfind("u")
print(f)'''


'''s="roses are beautiful"
s1=s.split()
print(s1)'''


'''s="roses are beautiful"
s1=s.rsplit("s",maxsplit=2)
print(s1)'''


'''s="roses\nare\nbeautiful"
print(s)
s1=s.splitlines(True)
print(s1)'''


'''s="beautiful"
s1=s.partition("u")
print(s1)'''


'''s="beautiful"
s1=s.rpartition("p")
print(s1)'''



'''s="good"
s1=s.center(7,"*")
print(s1)'''



'''s="bad"
s1=s.center(8,"*")
print(s1)'''


'''s="python"
s1=s.ljust(10,"*")
print(s1)'''



'''s="python"
s1=s.rjust(10,"*")
print(s1)'''



'''s="....python...."
print(len(s))
s1=s.strip(".py")
print(s1,len(s1))'''



'''s="...ajay..."
print(s,len(s))
s1=s.lstrip(".")
print(s1,len(s1))'''



'''s1="Ajayreddy"
s2="ajay@123"
s3=""
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())'''



'''s1="Ajayreddy"
s2="ajay@123"
print(s1.islower())
print(s2.islower())'''



'''s1="Ajayreddy"
s2="AJAY@123"
print(s1.isupper())
print(s2.isupper())'''



'''s1="My Name Is Ajay"
s2="From nellore"
print(s1.istitle())
print(s2.istitle())'''



'''s1="    "
s2="   ajay   "
print(s1.isspace())
print(s2.isspace())'''



'''s1="ajay@123 "
s2="😜😜"                 "windows + . or ;"
print(s1.isascii())
print(s2.isascii())'''



'''s1="ajay@123"
s2="ajay123"
print(s1.isalnum())
print(s2.isalnum())'''



'''s1="val"
s2="val$"
s3="if"
print(s1.isidentifier())
print(s2.isidentifier())
print(s3.isidentifier())'''



'''s1="ajay reddy"
print(s1,s1.isprintable())
s2="ajay\nreddy"
print(s2,s2.isprintable())'''



'''s1="My name is {frame},I'm {age}".format(frame="ajay reddy",age=22)
print(s1)
s2="My name is {0},I'm {1}".format("ajay reddy",22)
print(s2)
s3="My name is {},I'm {}".format("ajay reddy",22)
print(s3)'''



'''s1="12345"
s2="12@34"
s3="ajay"
print(s1.isnumeric())
print(s2.isnumeric())
print(s3.isnumeric())'''



'''s1="12345"
s2="12@34"
s3="ajay"
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())'''



'''s1="\u0030"
s2="\u0047"
print(s1.isdecimal())
print(s2.isdecimal())'''



'''d1={"name":"ajay","age":22}
s="happy birthday {name} you are now on leve {age}"
print(s.format_map(d1))'''



'''s1="ajay reddy bhumana"
res=s1.replace("reddy","kumar")
print(res)'''



'''s1="ajay reddy"
s2="bhumana"
print(s1.startswith("i"))
print(s2.startswith(("a","b","c")))'''



'''s1="ajay reddy"
s2="bhumana"
print(s1.endswith("i"))
print(s2.endswith(("a","b","c")))'''



'''s1="...ajay reddy..."
print(s1,len(s1))
s2=s1.removeprefix("..")
print(s2,len(s2))'''



'''s1="...ajay reddy..."
print(s1,len(s1))
s2=s1.removesuffix("..")
print(s2,len(s2))'''



'''s1="we\tare\tgood\tstudents"
s2=s1.expandtabs()
print(s2)'''



'''s1="123"
print(s1.zfill(5))
print(s1.zfill(4))'''



'''l1=['my','name','is','ajay','reddy']
res=" ".join(l1)
print(res)'''


'''d1={'a':'@','n':'$','i':'!'," ":"%%"}
table1=" ".maketrans(d1)
print(table1)'''



'''d1 = {'a': '@', 'n': '$', 'i': '!', ' ': '%%'}
text = "ani is an animal"
table1 = str.maketrans(d1)
res = text.translate(table1)
print(res)'''



'''txt="My name is ajay"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))'''



'''def greet():
    print("hi good morning")
greet()
greet()'''
    


'''l=[1,4,7,9,3]
print(min(l),max(l),sum(l))'''


'''print(bin(10))
print(hex(34))
print(oct(120))'''



'''n=int(input("enter:"))
res=[n%2==0,n%3==0,n%4==0]
print(res)
if all(res):
    print("yes")
else:
    print("no")'''


'''n=int(input("enter:"))
res=[n%2==0,n%3==0,n%4==0]
print(res)
if any(res):
    print("yes")
else:
    print("no")'''



'''def add_two_nums():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    print(c)
add_two_nums()'''



'''def even_odd(n):
    if n%2==0:
        print("even number")
    else:
        print("odd number")
even_odd(int(input("enter:")))
even_odd(90)'''



'''def add_two_nums():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    return c
res=add_two_nums()
print(res)'''



'''def even_odd(n):
    if n%2==0:
        return "even number"
    else:
        return "odd number"
print(even_odd(int(input("enter:"))))'''



'''def greet():
    print("welcome")
res=greet
print(greet)
print(res)
res()'''



'''sq=lambda x:x**2
print(sq(int(input("enter:"))))'''

'''add=lambda a,b,c:a+b+c
print(add(2,5,6))'''

'''div=lambda n:n%3==0 and n%4==0
print(div((int(input("enter:")))))'''


'''def add_two_nums(a,b):
    c=a+b
    print(c)
add_two_nums(3,4)'''



'''def fun(a,b=9):
    print(a,b)
fun(10)
fun(12,89)'''


'''def bio(name,age,place):
    print(name,age,place)
bio(name="ajay",age=22,place="nellore")'''


'''def fun(*a):
    print(a,type(a))
fun(12,2.5,2+3j,True)'''


'''def fun(**a):
    print(a,type(a))
fun()
fun(a=56,b="ajay")'''


'''def fun(a,b=9,*c,d,**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
fun(10,45,89,d="py",a1=100,b1=200,c1=300)'''



'''def outer_fun():
    def nested_fun():
        print("i am a nested function")
    nested_fun()
outer_fun()'''



'''def fun():
    a=100
    print("inside the function=>",a)
fun()'''
# print("outside the function=>",a)



'''def fun():
    global a
    a=100
    print("inside the function=>",a)
fun()
print("outside the function=>",a)'''



'''def outer():
    a="enclosed"
    def inner():
        b=900
        print(a)
    inner()
outer()'''


'''def outer():
    a=100
    def inner():
        a=200
        print("inside the nested function:",a)
    inner()
    print("outeside the nested function:",a)
outer()'''



'''def outer():
    a=100
    def inner():
        nonlocal a
        a=200
        print("inside the nested function:",a)
    inner()
    print("outside the nested function:",a)
outer()'''



'''a=100
def fun():
    print("inside the function:",a)
fun()
print("outside the function:",a)'''



'''s="hello"
print(len(s))'''



'''l1=[]
for i in range(1,101):
    l1.append(i)
print(l1)'''


'''l1=[i for i in range(1,11)]
print(l1)'''


'''l1=[i for i in range(1,11) if i%2==0]
print(l1)'''


'''n=int(input("n:"))
l1=[i for i in range(1,n+1)]
print(l1)'''



'''n=int(input("n:"))
l1=[i**2 for i in range(1,n+1)]
print(l1)'''


'''n=int(input("n:"))
l1=[100 for i in range(1,n+1)]
print(l1)'''


'''n=int(input("n:"))
r=int(input("r:"))
l1=[[x for x in range(1,r+1)] for i in range(1,n+1)]
print(l1)'''



'''n=int(input("n:"))
l1=[int(input(f"value {i}:")) for i in range (1,n+1)]
print(l1)'''


'''l1=[1 for i in range(1,6) for j in range(1,5)]
print(l1)'''



'''l1=["ajay","kumar","reddy","bhumana"]
res=[i.upper() for i in l1]
print(res)'''



'''t1=(x for x in range(1,11))
print(t1)'''


'''s1={x for x in range(1,11)}
print(s1)'''


'''s1={int(input("value:")) for i in range (1,5)}
print(s1)'''


'''d1={x:x**2 for x in range(1,6)}
print(d1)'''


'''l1=[1,2,3,4]
l2=[10,20,30,40,50]
res=zip(l1,l2)
print(list(res))'''


'''l1=[1,2,3,4]
l2=[10,20,30,40,50]
s1="ajay"
res=zip(l1,l2,s1)
print(list(res))'''


'''l1=[1,2,3,4,50]
l2=[10,20,30,40,50]
d1={x:y for x,y in zip(l1,l2)}
print(d1)'''


'''l1=[1,2,3,4,50]
l2=[10,20,30,40,50]
d1=dict(zip(l1,l2))
print(d1)'''


'''l1=[1,2,3,4,5,6,7]
a,*b,c=l1
print(a,b,c)'''


'''l1=[1,2,3,4,5]
print(l1)
print(*l1,sep="__")
print(*l1)'''


'''def ironman(n):
    if n<4:
        print(n,end=" ")
        ironman(n+1)
    print(n,end=" ")
print("start")
ironman(0)
print("end")'''


'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))'''


'''def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''


'''def sum_of_n(n):
    if n==0:
        return 0
    else:
        return n+sum_of_n(n-1)
print(sum_of_n(10))'''


'''def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:] + s[0])
print(reverse_string("hello"))'''



'''def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))'''



'''s1={10,20,30,40}
print(type(s1))
s2=frozenset(s1)
print(type(s2))'''
































































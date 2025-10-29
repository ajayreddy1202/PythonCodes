# [::::::::::::::::::::::::::::::::::::::BASICS::::::::::::::::::::::::::::::::::::::::::]

'''a=int(input("a:"))
b=int(input("b:"))
print(f"Before swap\n a:{a}\t b:{b}")
# c=a
# a=b
# b=c
a,b=b,a
print(f"After swap\n a:{a}\t b:{b}")'''



'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(f"Before swap \n a:{a}\tb:{b}\tc:{c}")
# d=a
# a=c
# c=b
# b=a
a,b,c=c,a,b
print(f"After swap \n a:{a}\tb:{b}\tc:{c}")'''



'''n=int(input("enter integer:"))
if n%2==0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")'''



# [:::::::::::::::::::::::::::::::::::PATTERN PART-1:::::::::::::::::::::::::::::::::::::::::::]

'''row=int(input("Enter row:"))
for i in range(row):
    print("*")'''


'''row=int(input("Enter row:"))
for i in range(row):
    print("* *")'''


'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()'''


'''row=int(input("row:"))
col=int(input("col:"))
val=1
l=len(str(row*col))
for i in range(row):
    for j in range(col):
        print(str(val).zfill(l),end=" ")
        val+=1
    print()'''


'''row=int(input("row:"))
col=int(input("col:"))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
    print()
    val+=1
    if val>9:
        val=1'''


'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=1
    for j in range(col):
        print(val,end=" ")
        val+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
        val+=1
    print()'''


'''row=int(input("row:"))
col=int(input("col:"))
val=row
for i in range(row):
    for j in range(col):
        print(val,end=" ")
    print()
    val-=1'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=col
    for j in range(col):
        print(val,end=" ")
        val-=1
    print()'''


'''row=int(input("row:"))
col=int(input("col:"))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    print()
    val+=1'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=ord('A')
    for j in range(col):
        print(chr(val),end=" ")
        val+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=ord('A')+row-1
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    print()
    val-=1'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=ord('A')+col-1
    for j in range(col):
        print(chr(val),end=" ")
        val-=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
        val+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
        val+=1
        if val>ord('Z'):
            val=ord('A')
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=ord('Z')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
        val-=1
        if val<ord('A'):
            val=ord('Z')
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=ord('Z')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    print()
    val-=1'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=ord('Z')
    for j in range(col):
        print(chr(val),end=" ")
        val-=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    for j in range(col):
        if i%2==0:
            print(i//2+1,end=" ")
        else:
            print(chr(64+(i//2+1)),end=" ")
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
num=1
char=ord('A')
for i in range(row):
    for j in range(col):
        if j%2==0:
            print(num,end=" ")
            num+=1
        else:
            print(chr(char),end=" ")
            char+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
num=1
char=ord('A')
l=len(str(row*col))
for i in range(row):
    for j in range(col):
        if j%2==0:
            print(str(num).zfill(l),end=" ")
            num+=1
        else:
            print(chr(char),end=" ")
            char+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    for j in range(col):
        if j%2==0:
            print(j//2+1,end=" ")
        else:
            print(chr(65+j//2),end=" ")
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
alpha=ord('A')
val=1
for i in range(row):
    for j in range(col):
        if i%2==0:
            print(val,end=" ")
        else:
            print(chr(alpha),end=" ")
    print()
    if i%2==0:
        val+=1
    else:
        alpha+=1'''



'''row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    val=1
    alpha=ord('A')
    for j in range(col):
        if j%2==0:
            print(val,end=" ")
            val+=1
        else:
            print(chr(alpha),end=" ")
            alpha+=1
    print()'''



'''row=int(input("row:"))
col=int(input("col:"))
val=1
alpha=ord('A')
p=True
for i in range(row):
    for j in range(col):
        if p:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
            p=False
        else:
            print(chr(alpha),end=" ")
            alpha+=1
            p=True
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


'''n=int(input("n:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
        if num>9:
            num=1
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(i+64),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(i+j+63),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==j:
            print(i+1,end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    count=n
    for j in range(n+1):
        if i==j:
            print(count+1,end=" ")
        else:
            print(" ",end=" ")
        count-=1
    print()'''


'''n=int(input("n:"))
k=n
for i in range(n):
    for j in range(n+1):
        if i==j:
            print(k,end=" ")
        else:
            print(" ",end=" ")
    k-=1
    print()'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print((str(i)+' ')*(n-i+1))
print()'''


'''n=int(input("n:"))
for i  in range(n):
    for j in range(n-i):
        print(n-j,end=" ")
    print()
print()'''


'''n=int(input("n:"))
ch=90
for i in range(n):
    print((chr(ch-i)+' ')*(i+1))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print((chr(64+i)+" ")*(n-i+1))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(64+j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print((chr(64+i)+" ")*(n-i+1))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print((str(i)+" ")*(n-i+1))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(chr(64+n-j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(chr(90-i-j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print((" ")*(i-1)+str(i))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print((" ")*(n-i)+str(i))
print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print(" "*(i-1)+chr(64+i))
print()'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print(" "*(n-i)+chr(64+i))
print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*i+chr(90-i))
print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    if i%2!=0:
        print(" "*(i-1)+str((i+1)//2))
    else:
        print(" "*(i-1)+"*")
print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print("*"*i)'''


'''n=int(input("n:"))
val=1
for i in range(1,n+1):
    print((str(val)+" ")*i)
    val+=1'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print("*"*i)'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*i+"*")'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print(" "*(i-1)*2+str(i))'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(i*2)+chr(65+i))'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    print(" "*((n-i)*2)+str(i))'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(i*2)+chr(87+i))'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(i*2)+chr(65+(n-i-1)))'''


'''n=int(input("n:"))
for i in range(n):
    print((chr(65+(n-i-1))+" ")*(i+1))'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(chr(65+j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(chr(65+i),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(chr(90-i),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(chr(68-i),end=" ")
    print()'''


'''n=int(input("n:"))
count=1
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(count,end=" ")
            count+=1
    print()'''


'''n=int(input("n:"))
count=1
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(count,end=" ")
            count+=1
        else:
            print("*",end=" ")
    print()'''


'''n=int(input("n:"))
ch=65
rows=n+1
for i in range(rows):
    for j in range(n):
        if i+j<rows:
            print(chr(ch),end=" ")
            ch+=1
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(chr(68-j),end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(chr(90-j),end=" ")
    print()'''


'''n=int(input("n:"))
count=1
for i in range(n):
    for j in range(i+1):
        print(count,end=" ")
    count+=1
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(n-i,end=" ")
    print()'''


'''n=int(input("n"))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(i,n):
        print(i+1,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(chr(ord('D')-j),end=" ")
    print()'''



'''n = 4  # Number of rows
for i in range(n):
    # Print leading spaces
    print("  " * (n - i - 1), end="")
    # Print letters
    for j in range(n-1, n-i-2, -1):
        print(chr(65 + j), end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(chr(ord('Z')-j),end=" ")
    print()'''


'''n = 4
start = 90  # 'Z'
for i in range(n):
    print("   " * (n - i - 1), end="")
    for j in range(start, start - i - 1, -1):
        print(chr(j), end=" ")
    print()'''


'''n = 4  # Number of rows
start = 90  # ASCII of 'Z'
for i in range(n):
    # Print leading spaces
    print("   " * (n - i - 1), end="")
    # Print the same letter (decreasing each row)
    for j in range(i + 1):
        print(chr(start - i), end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(i+1,end=" ")
    print()'''


'''n = 4  # number of rows
for i in range(1, n + 1):
    # Print leading spaces (3 spaces per missing row)
    print("   " * (n - i), end="")
    # Print the number i, i times
    for j in range(i):
        print(i, end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()'''


'''n = 4  # Number of rows
for i in range(1, n + 1):
    # Print leading spaces
    print("   " * (n - i), end="")
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(i+1):
        print(n-i,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(i+1):
        print(n-j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()'''


'''n=int(input("n:"))
str=1
spc=n-1
for i in range(n):
    for j in range(spc):
        print(" ",end=" ")
    for k in range(str):
        print("*",end=" ")
    print()
    spc-=1
    str+=2'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))'''


'''n=int(input("n:"))
str=2*n-1
spc=0
for i in range(n):
    for j in range(spc):
        print(" ",end=" ")
    for k in range(str):
        print("*",end=" ")
    print()
    str-=2
    spc+=1'''


'''n=int(input("n:"))
for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    print((str(i)+" ")*(2*i-1))'''


'''n=int(input("n:"))
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    for j in range(1,2*i):
        print(j,end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n,0,-1):
    print("  "*(n-i),end=" ")
    print((str(i)+" ")*(2*i-1))'''


'''n=int(input("n:"))
ch=65
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    print((chr(ch)+" ")*(2*i-1))
    ch+=1'''


'''n=int(input("n:"))
for i in range(n):
    print("  "*i,end=" ")
    for j in range(1,2*(n-i)):
        print(j,end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    print("  "*i+(chr(68-i)+" ")*(2*(n-i)-1))'''


'''n=int(input("n:"))
ch=90
for i in range(n):
    print("  "*i,end=" ")
    for j in range(2*(n-i)-1):
        print(chr(ch),end=" ")
        ch-=1
    print()'''


'''n=int(input("n:"))
for i in range(n,0,-1):
    start_char_code=ord('A')
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(start_char_code+k),end=" ")
    print()'''


'''n=int(input("n:"))
start_char_code=ord('A')
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(start_char_code),end=" ")
    start_char_code+=1
    print()'''


'''n = int(input("n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")   # spaces before pattern

    if i % 2 != 0:  # odd row → numbers
        print((str(i) + " ") * (2 * i - 1))
    else:            # even row → stars
        print(("* ") * (2 * i - 1))'''


'''n=int(input("n:"))
count=1
for i in range(1,n+1):
    print(" "*(n-i)*2,end=" ")
    for j in range(1,2*i):
        if j%2==0:
            print("*",end=" ")
        else:
            print(count,end=" ")
            count+=1
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==3 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==j or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(2*n-1):
        if i==n-1 or i+j==n-1 or j-i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(2*n-1):
        if i==0 or i==j or i+j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(1,n-i+1):
        print("*",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
for i in range(1,n):
    for space in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,2*n-2*i):
        print("*",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for space in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,n-i+1):
        print("*",end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n-1,-n,-1):
    for j in range(n,abs(i),-1):
        print("*",end=" ")
    print()'''

# [:::::::::::::::::::::::::::::::::::PATTERN PART-2:::::::::::::::::::::::::::::::::::]

# An Armstrong number (also called a narcissistic number)
# is a number that is equal to the sum of the powers of its
# digits, where the power is the number of digits in that number.
'''num=9474
res=0
temp=num
while num!=0:
    rem=num%10
    res=res+rem**4
    num=num//10
if temp==res:
    print("Amstrong number")
else:
    print("Not an Amstrong number")'''



# The factorial of a number (n!) is the product of all positive integers from 1 up to that number n.
# It is written using an exclamation mark:
# 👉 n! = n × (n−1) × (n−2) × ... × 3 × 2 × 1
'''n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("factorial of",n,"is",fact)'''



# A Strong number is a number where the sum of factorials of its digits equals the number itself.
# Example:
# 145 → (1! + 4! + 5!) = 145 ✅
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



# The sum of digits of a number means adding all the individual
#  digits of that number together.
#  For 99 → 9 + 9 = 18
'''n=99
res=0
while n!=0:
    num=n%10
    res+=num
    n=n//10
    print(res)'''



# A Perfect Number is a positive integer that is equal
#  to the sum of its proper divisors
# (excluding the number itself).
'''n=int(input("Enter number:"))
res=0
for i in range(1,n):
    if n%i==0:
        res+=i
if n==res:
    print("perfect")
else:
    print("not perfect")'''


# Palindrome number or Not:
# A Palindrome number is a number that reads the same forward and backward.
'''n=int(input("enter number:"))
n=str(n)
if n==n[::-1]:
    print("Palindrom Number")
else:
    print("Not a Palindrom Number")'''


'''n=int(input("Enter Number:"))
temp=n
res=0
while n!=0:
    rem=n%10
    res=res*10+rem
    n=n//10
print("Reverse the Number",res)
if temp==res:
    print("Palindrom number")
else:
    print("Not a palindrom number")'''


'''n=int(input("Enter Number:"))
d={}
while n!=0:
    rem=n%10
    if rem not in d:
        d[rem]=1
    else:
        d[rem]+=1
    n=n//10
for i,j in d.items():
    print(i,":",j)'''      



# A Disarium number is a number in which the sum of its digits
#  powered with their respective positions equals the number itself.
'''n=int(input("Enter Number:"))
val=n
temp=n
cnt=0
res=0
while temp!=0:
    cnt+=1
    temp=temp//10
print("count:",cnt)
while val!=0:
    rem=val%10
    res=res+rem**cnt
    val=val//10
    cnt=cnt-1
if res==n:
    print("Disarium number")
else:
    print("Not Disarium Number")'''



'''n = int(input("Enter Number: "))
while n > 9:          # repeat until n is a single digit
    x = n
    res = 0
    while x != 0:
        rem = x % 10      # get last digit
        res = res + rem   # sum of digits
        x = x // 10       # remove last digit
    n = res              # assign sum to n
print("Super digit of the given number:", n)'''



'''n=int(input("Enter Number:"))
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
    print("Automorphic Number")
else:
    print("Not Automorphic Number")'''



'''n=int(input("Enter Number:"))
cnt=0
temp=n
while n!=0:
    cnt+=1
    n=n//10
print("Total digit",cnt)
if cnt%2==0:
    first_half=temp//(10**(cnt//2))
    second_half=temp%(10**(cnt//2))
else:
    first_half=temp//(10**(cnt//2))
    second_half=temp%(10**(cnt//2))
rev=0
sec=second_half
while sec!=0:
    rev=rev*10+sec%10
    sec//=10
if first_half==rev:
    print(temp,"is a Mirror number")
else:
    print(temp,"is Not a Mirror Number")'''


'''n=int(input("Enter Number:"))
max_ele=0
while n!=0:
    rem=n%10
    if rem>max_ele:
        max_ele=rem
    n=n//10
print("Max element is",max_ele)'''


'''num=int(input("Enter Number:"))
max1=0
max2=0
while num>0:
    rem=num%10
    if rem>max1:
        max2=max1
        max1=rem
    elif rem>max2:
        max2=rem
    num=num//10
print("first maximum digit:",max1)
print("second maximum digit:",max2)
print("difference:",max1-max2)'''


'''n = int(input("Enter a number: "))
# Step 1: Multiply by 1, 2, 3 and concatenate as string
concat = str(n*1) + str(n*2) + str(n*3)
# Step 2: Check if length is 9 and contains digits 1-9 exactly once
if len(concat) == 9 and set(concat) == set('123456789'):
    print(n, "is a Fascinating Number")
else:
    print(n, "is Not a Fascinating Number")'''


'''n=int(input("Enter Number:"))
if n>0:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Enter valid Number")'''


'''n=int(input("Enter Number:"))
temp=1
bi=0
while n!=0:
    rem=n%2
    bi=bi+temp*rem
    temp=temp*10
    n=n//2
print("Binary Value is:",bi)'''


'''n=int(input("Enter Number:"))
cnt=0
while n!=0:
    rem=n%2
    if rem==1:
        cnt+=1
    n=n//2
if cnt%2==0:
    print("Evel Number")
else:
    print("Not Evel Number")'''


'''binary=input("Enter a Binary Number:")
decimal=0
power=len(binary)-1
for digit in binary:
    if digit=='1':
        decimal+=2**power
    power-=1
print("Decimal value:",decimal)'''


# [:::::::::::::::::::::::::::::::::::NUMBER SERIES:::::::::::::::::::::::::::::::::::]
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


'''n=int(input("Enter:"))
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


'''num=int(input("Enter:"))
n1=0
n2=1
if num<=0:
    print("enter above zero")
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


'''num=int(input("Enter:"))
n=1
str="*"
char=97
for i in range(num):
    print(n,end=" ")
    n+=1
    print(str,end=" ")
    # if char<=122:
    #     print(chr(char),end=" ")
    #     char+=1
    # else:
    #     char=97
    print(chr(char),end=" ")
    char+=1'''


'''n=int(input("Enter:"))
count=0
num=2
print("First",n,"Prime numbers are:")
while count<n:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=" ")
        count+=1
    num+=1'''


'''n=int(input("Enter n:"))
for i in range(1,n+1):
    pos=(i-1)%15+1
    if pos<=5:
        print(pos,end=" ")
    elif pos<=10:
        print("*",end=" ")
    else:
        print(chr(65+(pos-11)),end=" ")'''


'''s="ajayreddybhumana"
num=int(input("Enter:"))
length=len(s)
for i in range(num):
    ch=s[i%length]
    if (i+1)%2==0:
        print(ch.upper(),end=" ")
    else:
        print(ch.lower(),end=" ")'''


# [::::::::::::::::::::::::::::::::::: LIST :::::::::::::::::::::::::::::::::::]





































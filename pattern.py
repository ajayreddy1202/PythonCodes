#pattern programming 07/08/25
'''row=int(input("row:"))
col=int(input("col:"))
val=1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
        val+=1
    print()'''



'''row=int(input("row :"))
for i in range(row):
    print("*")'''



'''row=int(input("row:"))
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



#pattern programming 08/08/25
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
for i in range(row):
    for j in range(col):
        if j%2==0:
            print(j//2+1,end=" ")
        else:
            print(chr(65+j//2),end=" ")
    print()'''
        


#pattern programming 11/08/25
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
    alpha=ord('A')
    val=1
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
alpha=ord('A')
val=1
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



#pattern programming 11/08/25
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
    k=k-1
    print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print((str(i) + ' ') * (n-i+1))
print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(n-j, end=' ')
    print()
print()'''



'''n=int(input("n:"))
ch=90  
for i in range(n):
    print((chr(ch - i) + ' ') * (i+1))'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print((chr(64 + i) + " ") * (n - i + 1))'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(chr(64 + j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print((chr(64 + i) + " ") * (n - i + 1))'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print((str(i) + " ") * (n - i + 1))'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i, n):
        print(chr(64 + n - j), end=" ")
    print()
print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i, n):
        print(chr(90 - i - j), end=" ")
    print()
print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print(" " * (i - 1) + str(i))
print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print(" " * (n - i) + str(i))
print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print(" " * (i - 1) + chr(64 + i))
print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print(" " * (n - i) + chr(64 + i))
print()'''



'''n=int(input("n:"))
for i in range(n):
    print(" " * i + chr(90 - i))
print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(" " * (i - 1) + str((i + 1) // 2))
    else:
        print(" " * (i - 1) + "*")'''



#pattern programming 12/08/25
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
    print("* "*i)'''



'''n=int(input("n:"))
val=1
for i in range(1,n+1):
    print((str(val)+" ")*i)
    val+=1'''



'''n=int(input("n:"))
for i in range(n,0,-1):
    print("* "*i)'''



'''n=int(input("n:"))
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)'''



'''n=int(input("n:"))
for i in range(n):
    print("  "*i+"*")'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print(" " * (i - 1) * 2 + str(i))
print()'''



'''n=int(input("n:"))
for i in range(n):
    print(" " * (i * 2) + chr(65 + i))
print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print(" " * ((n - i) * 2) + str(i))
print()'''



'''n=int(input("n:"))
for i in range(n):
    print(" " * (i * 2) + chr(87 + i))  # 87 -> 'W'
print()'''



'''n=int(input("n:"))
for i in range(n):
    print(" " * (i * 2) + chr(65 + (n - i - 1)))
print()'''



'''n=int(input("n:"))
for i in range(n):
    print((chr(65 + (n - i - 1)) + " ") * (i + 1))'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n, i, -1):
        print(j, end=" ")
    print()
print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i, n):
        print(chr(65 + j), end=" ")
    print()
print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(chr(65 + i), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(chr(90 - i), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(chr(90 - j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(chr(68 - i), end=" ")
    print()'''


'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(chr(68 - j), end=" ")
    print()'''



'''n=int(input("n:"))
count = 1
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(count, end=" ")
            count += 1
        else:
            print("*", end=" ")
    print()'''



'''n=int(input("n:"))
ch = 65
rows = n + 1
for i in range(rows):
    for j in range(n):
        if i + j < rows:
            print(chr(ch), end=" ")
            ch += 1
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(chr(68 - j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(chr(90 - j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(chr(90 - i), end=" ")
    print()
print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(n - i, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i+1):
        print(n - j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(i, n):
        print(i+1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(j+1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end=" ") 
    for j in range(i + 1):
        print(chr(ord('D') - j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end=" ")
    for j in range(i + 1):
        print(chr(ord('Z') - j), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end=" ")
    for j in range(i + 1):
        print(chr(ord('Z') - i), end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end="")
    for j in range(i + 1):
        print(i + 1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end=" ")
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end=" ")
    for j in range(i + 1):
        print(n - i, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * (n - i - 1), end="")
    for j in range(i + 1):
        print(n - j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    for j in range(n - i):
        print(j + 1, end=" ")
    print()'''



# pattern programming 13/08/25
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
    print("  "*(n-i-1)+"* "*(2*i+1))'''



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
   print("  "*i+"* "*(2*(n-i)-1))'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    print((str(i) + " ") * (2 * i - 1))'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    print("  " * (n - i), end=" ")
    print((str(i) + " ") * (2 * i - 1))'''



'''n=int(input("n:"))
ch = 65  # ASCII for 'A'
for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    print((chr(ch) + " ") * (2 * i - 1))
    ch += 1'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * i, end=" ")
    for j in range(1, 2*(n-i)):
        print(j, end=" ")
    print()'''



'''n=int(input("n:"))
for i in range(n):
    print("  " * i + (chr(68 - i) + " ") * (2*(n-i)-1))'''



'''n=int(input("n:"))
ch = 90
for i in range(n):
    print("  " * i, end=" ")
    for j in range(2*(n-i)-1):
        print(chr(ch), end=" ")
        ch -= 1
    print()'''



'''n=int(input("n:"))
for i in range(n, 0, -1):
    start_char_code = ord('A')
    for j in range(n - i):
        print("  ", end=" ")
    for k in range(2 * i - 1):
        print(chr(start_char_code + k), end=" ")
    print()'''



'''n=int(input("n:"))
start_char_code = ord('A')
for i in range(n, 0, -1):
    for j in range(n - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print(chr(start_char_code), end=" ")
    start_char_code += 1
    print()'''



'''n=int(input("n:"))
for i in range(1, n + 1):
    if i % 2 != 0:  
        print(" " * (n - i) * 2, end=" ")
        for j in range(2 * i - 1):
            print(i, end=" ")
    else:  
        print(" " * (n - i) * 2, end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
    print()'''



'''n=int(input("n:"))
count = 1
for i in range(1, n + 1):
    print(" " * (n - i) * 2, end="")
    for j in range(1, 2 * i):
        if j % 2 == 0:  
            print("*", end=" ")
        else:  
            print(count, end=" ")
            count += 1
    print()'''



#Pattern programming 14/08/25
'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
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
        if j==0 or j==n-1 or i==j:
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



#pattern programming 15/08/25
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



'''for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()'''



'''for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()'''



'''for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()'''



'''for i in range(1,6):
    for j in range(1,6):
        print(j%2,end=" ")
    print()'''



'''for i in range(ord('a'),ord('e')+1):
    for j in range(ord('a'),ord('e')+1):
        print(chr(j),end=" ")
    print()'''



'''for i in range(ord('a'),ord('e')+1):
    for j in range(ord('a'),ord('e')+1):
        print(chr(i),end=" ")
    print()'''



'''for i in range(ord('e'),ord('a')-1,-1):
    for j in range(ord('e'),ord('a')-1,-1):
        print(chr(j),end=" ")
    print()'''



'''for i in range(ord('e'),ord('a')-1,-1):
    for j in range(ord('e'),ord('a')-1,-1):
        print(chr(i),end=" ")
    print()'''



'''for i in range(1,6):
    for j in range(1,6):
        print(i%2,end=" ")
    print()'''



'''for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()'''



'''for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end=" ")
    print()'''



'''for i in range(5,0,-1):
    for j in range(5,0,-1):
        print("*",end=" ")
    print()'''



#PATTERN1:
'''rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    print(' '*(rows-i)+'*'*(2*i-1))



#PATTERN2:
'''rows=int(input("Enter rows:"))
for i in range(rows,0,-1):
    print(' '*(rows-i)+'*'*(2*i-1))



#PATTERN3:
'''rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    print(' '*(rows-i)+'*'*(2*i-1))
for i in range(rows,0,-1):
    print(' '*(rows-i)+'*'*(2*i-1))'''



#PATTERN4:
'''#upper part
rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    print('*'*i+' '*(2*(rows-i))+'*'*i)
#lower part
for i in range(rows,0,-1):
    print('*'*i+' '*(2*(rows-i))+'*'*i)'''



#PATTERN5:
'''rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    print('*'*i)'''



#PATTERN6:
'''rows=int(input("Enter rows:"))
for i in range(rows):
    if i==0 or i==rows-1:
        print('*'*rows)
    else:
        print('*'+' '*(rows-2)+'*')'''



#PATTERN7:
'''rows=int(input("Enter rows:"))
for i in range(rows):
    print('*'*rows)'''



#PATTERN8:
'''rows=int(input("Enter rows:"))
for i in range(rows,0,-1):
    print('*'*i)'''



#PATTERN9:
'''rows=int(input("Enter rows:"))
#upper part
for i in range(1,rows+1):
    print(' '*(rows-i)+'*'+' '*(2*i-3)+('*' if i>1 else ' '))
#lower part
for i in range(rows-1,0,-1):
    print(' '*(rows-i)+'*'+' '*(2*i-3)+('*' if i>1 else ' '))
'''



#PATTERN10:
'''rows=int(input("Enter rows:"))
for i in range(1,rows-1):
    if i==rows:
        print('*'*(2*i-1))
    else:
        print(' '*(rows-i)+'*'+' '*(2*i-3)+('*'if i>1 else' '))'''



#PATTERN11:
'''rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    print(' '*(rows-i)+'*'*i)'''



#PATTERN12:
'''rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==j or i+j==rows+1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()'''




























































































































































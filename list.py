#Find the max element of the list 29/08/25
'''l1=[11,9,2,14,16,33,4,1]
max1=l1[0]
for i in range(1,len(l1)):
    if l1[i]>max1:
        max1=l1[i]
print("max element in the list:",max1)'''



'''l1=[11,9,2,14,16,33,4,1]
min1=l1[0]
for i in range(1,len(l1)):
    if l1[i]<min1:
        min1=l1[i]
print("min element in the list:",min1)'''



#write a program to print missing elements in the given list and excluding in the given list
'''l1=[2,8,15,20,28,37,48,55]
for i in range(len(l1)-1):
    fe=l1[i]+1
    le=l1[i+1]
    for j in range(fe,le):
        print(j,end=" ")'''



#wite a program Bubble sort/Sinking sort [*important*]
'''l1=[3,1,8,7,2]
print("Before sorting:",l1)

for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print("After sorting:",l1)'''


    
'''l1=[6,2,7,1,8,5,3,4]
print(l1)
if len(l1)%2==0:
    for i in range(0,len(l1),2):
        l1[i],l1[i+1]=l1[i+1],l1[i]
    else:
        print("it will work only for even number of elements")
print(l1)'''



'''l1=[1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1]
print(l1)
cnt=0
for i in l1:
    if i==1:
        cnt+=1
for i in range(len(l1)):
    if i<cnt:
        l1[i]=1
    else:
        l1[i]=0
print(l1)'''



#write a program to check the given list is palindrome or not 30/08/25
'''l1=[1,11,8,5,8,11,1]
j=len(l1)-1
for i in range(len(l1)):
    if l1[i]!=l1[j]:
        print("List is not a palindrom")
        break
    j-=1
else:
    print("List is a palindrom")'''


    
#write a program to rotate the list to the left side based on the no.of rotation given in the user input    
'''l1=[1,2,3,4,5]
print("Before rotating",l1)
n=(int(input("Enter the number of rotations:")))

for i in range(n):
    temp=l1[0]
    for i in range(len(l1)-1):
        l1[i]=l1[i+1]
    l1[len(l1)-1]=temp
    print(l1)'''



#Right rotation
'''l1=[1,2,3,4,5]
print("Before rotating",l1)
n=(int(input("Enter the number of rotations:")))

for i in range(n):
    temp=l1[len(l1)-1]
    for i in range(len(l1)-1,0,-1):
        l1[i]=l1[i-1]
    l1[0]=temp
    print(l1)'''



#swap the list characters and numbers not special characters 01/09/25
# step1:count the total no.of lower,upper and numeric chars only
# step2:based on the count create on list with total count and all the value must be 'None' [None,None,....None]
# step3:iterate through the list and assign all lower,upper and numeric char to new list
# step4:return the new list
# step5:iterate till the end of original list and if the value is upper,lower and numeric assign the value from new list to original list,if it is special characters no need to modify the value
'''l1=['1','@','l','2','3','$','u','9','h','#','a','4','r']
print("l1:",l1)
cnt=0
for i in l1:
    if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=48 and ord(i)<=57):
        cnt+=1
# print("cnt:",cnt)
n_list=[None]*cnt
# print(n_list)
j=0
for i in range(len(l1)):
    if (ord(l1[i])>=97 and ord(l1[i])<=122) or (ord(l1[i])>=65 and ord(l1[i])<=90) or (ord(l1[i])>=48 and ord(l1[i])<=57):
        n_list[j]=l1[i]
        j+=1
# print(n_list)
n_list=n_list[::-1]
# print(n_list)
j=0
for i in range(len(l1)):
    if (ord(l1[i])>=97 and ord(l1[i])<=122) or (ord(l1[i])>=65 and ord(l1[i])<=90) or (ord(l1[i])>=48 and ord(l1[i])<=57):
        l1[i]=n_list[j]
        j+=1
print("l1:",l1)'''


    
'''# swap the list characters and numbers not special characters 01/09/25
l1 = ['1','@','l','2','3','$','u','9','h','#','a','4','r']
print("Original l1:", l1)
# step1: check if a character is alphanumeric (digit or letter)
def int_or_char(i):
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
        return True
    else:
        return False
# step2: collect all alphanumeric chars
temp = [ch for ch in l1 if int_or_char(ch)]
# step3: reverse them
temp = temp[::-1]
# step4: assign back into original list, skipping special chars
j = 0
for i in range(len(l1)):
    if int_or_char(l1[i]):
        l1[i] = temp[j]
        j += 1
print("Modified l1:", l1)
'''



#Write a program to have N number of non negative integers in a list
'''n = int(input("enter:"))     
numbers = []
for i in range(n):
    num = int(input())
    if num < 0:
        exit()
    numbers.append(num)
print(numbers)'''



#display the sum of only prime numbers present in a given list 02/09/25
'''l1 = [1, 11, 12, 33, 10, 8, 9,2]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):   # only check up to sqrt(num)
        if num % i == 0:
            return False
    return True
res = 0
for i in l1:
    if is_prime(i):
        res += i
print("sum of all prime numbers in a list:", res)'''



#write a program to minimize and maximize the height of a given values based on the user input and display the maximum and minimum values
# 1 :if the values is < the user input need to add user input to that value
# 2 :if the value is > user input need to decrement the user input value from the selected value
# 3 :if the value is = user input increment the value with the user input
'''l1=[2,3,6,15,10,8]
print(l1)
n=int(input("enter:"))
l2=[]
for i in range(len(l1)):
    if l1[i]<=n:
        l2+=[l1[i]+n]
    elif l1[i]>n:
        l2+=[l1[i]-n]
print(l2)
max1=l2[0]
min1=l2[0]

for i in range(1,len(l2)):
    if l2[i]>max1:
        max1=l2[i]
    if l2[i]<min1:
        min1=l2[i]
print(max1-min1)'''



#write a program to product all the values present in a list excluding the number its self during each iteration
'''l1=[1,2,3,4,5]
print(l1)
prod=1
l2=[]
for i in l1:
    prod=prod*i
print(prod)

for i in range(len(l1)):
    l2+=[prod//l1[i]]
print(l2)'''



#write a program to display yes or no from the list of non negative integer values
# 1:the start index must be 0 and the based on the value present in the valu and need to jump to the respect the index
# 2:need to do this process till end of the list if we cannot reach the end display message no      
# write a program to display yes or no from the list of non negative integer values

'''def can_reach_end(arr):
    n = len(arr)
    i = 0   # start index

    while i < n:
        if i == n - 1:   # reached the last index
            return "Yes"
        if arr[i] == 0:  # stuck, cannot move further
            return "No"
        i = i + arr[i]   # jump to next index

    return "No"

# Example test cases
l1 = [2, 3, 1, 1, 4]   # can reach last index
l2 = [3, 2, 1, 0, 4]   # cannot reach last index

print("List:", l1, "=>", can_reach_end(l1))
print("List:", l2, "=>", can_reach_end(l2))'''



'''l1=[3,2,1,1,4]
def new(l1):
    i=0
    while i<len(l1):
        if i==len(l1)-1:
            return "yes"
        i+=l1[i]
    return "no"
print(new(l1))'''



#write a program  to display all the pairs of target value from the given list 03/09/25
'''l1=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter:"))
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]+l1[j]==target:
            print(l1[i],l1[j])'''



'''l1=[1,2,3,4,5,6,7,8,9]
target=int(input("Enter:"))
for i in l1:
    for j in l1:
        if i+j==target:
            print(i,",",j)'''



#write a program to display boolean values true if each element in the list ends with the value 5 or return false
'''l1=[]
a=False
b=len(l1)
for i in l1:
    if i%10==0 or i%10==5:
        a=True
    else:
        a=False
        break
print(a)
if b==0:
    print(-1)'''



'''def last_five(nums):
    if len(nums)==0:
        return -1
    else:
        for i in nums:
            last_digit=i%10
            if last_digit!=5:
                return False
        else:
            return True
l1=[5,25,337,465,725,1025]
print(last_five(l1))'''



#Ajay wants to buy a stock with minimum price and he need to sell the stock to get a maximum profit and help 
#with when to buy a stock and when to sell to get a msximum profit based on the values given in the list
'''def max_profit(prices):
    n = 0
    for _ in prices:
        n += 1
    min_price = prices[0]   
    max_profit = 0
    i = 1
    while i < n:
        if prices[i] < min_price:
            min_price = prices[i]
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        i += 1
    return max_profit
prices1 = [10, 8, 1, 3, 4, 9, 2]   
prices2 = [1, 3, 6, 8, 10, 12]
prices3 = [7, 5, 3, 2, 1]

print("Max Profit (prices1):", max_profit(prices1))  
print("Max Profit (prices2):", max_profit(prices2)) 
print("Max Profit (prices3):", max_profit(prices3)) '''



'''def stocks(prices):
    if len(prices)==0:
        return 0
    else:
        maxprofit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                current_profit=prices[j]-prices[i]
                if current_profit>maxprofit:
                    maxprofit=current_profit
        return maxprofit
prices=[10, 8, 1, 3, 4, 9, 2] 
# prices=[]
# prices=[1, 3, 6, 8, 10, 12]
# prices=[12,12]
print(stocks(prices))'''



#write a program to display only unique elements present in a list without type conversion 04/09/25
'''l1=[1,2,2,3,1,4,3,2,2,5,6]
dict={}
for i in l1:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
    while dict[i]>1:
        dict[i]-=1
for i in dict:
    print(i,end=" ")'''



'''l1=[1,2,2,3,1,4,3,2,2,5,6]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            l1[j]-=l1[i]
    if l1[i]!=0:
        print(l1[i],end=" ")'''



#write a program to flatten the give list
'''l1=[1,2,[3,'$','@'],7,['6'],4,3,[8,9,'#']]
l2=[]
for i in range(len(l1)):
    a=type(l1[i])
    if a==list:
        l2.extend(l1[i])
    else:
        l2.append(l1[i])
print(l2)'''



'''l1=[1,2,[3,'$','@'],7,['6'],4,3,[8,9,'#']]
print(l1)
new_l=[]
for i in l1:
    if isinstance(i,list):
        for j in i:
            new_l+=[j]
    else:
        new_l+=[i]
print(new_l)'''



'''l1=[1,2,3,'$','@',7,'6',4,3,8,9,'#']
print(l1)
new_1=[]
even=[]
odd=[]
char=[]
for i in l1:
    if isinstance(i,str):
        char.append(i)
    elif i%2==0:
        even.append(i)
    else:
        odd.append(i)
new_1.clear()
new_1.append(even)
new_1.append(odd)
new_1.append(char)
print(new_1)'''



#write a program all the unique elements in the first place and duplicate elements in the last place
#INPUT l1=[1,2,2,3,1,4,3]
#OUTPUT l1=[1,2,3,4]
'''l1 = [1, 2, 2, 3, 1, 4, 3]
result = []
for i in l1:
    if i not in result:
        result.append(i)
print(result)'''



#write a program to count present inside a list and find the sum of integer values 05/09/25
'''l1=['A',33.6,74,[7],4,'a',[3,'$',4],[3,'a',11],17,[12,4]]
sum=0
count=0
for i in l1:
    if isinstance(i,list):
        count+=1
        for j in range(len(i)):
           if isinstance(i[j],int):
               sum+=i[j]
    else:
        if isinstance(i,int):
            sum+=i
print(count,sum)'''



#write a program to print matrix program
'''row=int(input("enter rows:"))
col=int(input("enter columns:"))
list=[]
for i in range(row):
    rowi=[]
    for j in range(col):
        rowi+=[(i,j)]
    list+=[rowi]
print(list)'''



#write a program to fetch the values of a specific column number if it exists in the given nested list based on the use input
'''l1=[[2,'$',4,'a'],[7,6,'py',75.5],['@','R',1,'king'],[84,7,'#',89.9]]
col=int(input("enter columns:"))
if col>=4:
    print("out")
else:
    for i in range(len(l1)):
        for j in range(col):
            print(l1[i][col])
            break'''


        
#write a program for matrix addition    08/09/25
'''row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# Input Matrix 1
print("\nEnter the values for Matrix 1:")
matrix1 = [[int(input(f"matrix1[{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)]

# Display Matrix 1
print("\nMatrix 1:")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=" ")
    print()

# Input Matrix 2
print("\nEnter the values for Matrix 2:")
matrix2 = [[int(input(f"matrix2[{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)]

# Display Matrix 2
print("\nMatrix 2:")
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end=" ")
    print()

# Initialize result matrix with zeros
result = [[0 for j in range(col)] for i in range(row)]
# Perform Matrix Addition
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Display Result Matrix
print("\nMatrix Addition Result:")
for i in range(row):
    for j in range(col):
        print(result[i][j], end=" ")
    print()'''



#write a program for matrix multiplication
'''row=int(input("Enter the row:"))
col=int(input("Enter the col:"))

print("Enter the values for the matrix1:")
matrix1=[[int(input()) for j in range(col)] for i in range(row)]

print("matrix1")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()
    
print("Enter the values for the matrix2:")
matrix2=[[int(input()) for j in range(col)] for i in range(row)]

print("matrix2")
for i in range(row):
    for j in range(col):
        print(matrix2[i][j],end=" ")
    print()

result=[[0 for j in range(col)] for i in range(row)]
#matrix multiplication
print("matrix multiplication")
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        for k in range(len(matrix2)):
            result[i][j]+=matrix1[i][k]*matrix2[k][j]
        
print("result")
for i in range(row):
    for j in range(col):
        print(result[i][j],end=" ")
    print()
'''



#write a program to except the values to the matrix using user input and find the sum of each diagonals and print the its difference of the diagonals
# Input matrix size
'''row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# Check if matrix is square
if row != col:
    print("Diagonal operations require a square matrix.")
else:
    print("Enter the values for the matrix:")
    matrix = [[int(input(f"matrix[{i+1}][{j+1}]: ")) for j in range(col)] for i in range(row)]

    # Display the matrix
    print("The Matrix:")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

    # Calculate sums of diagonals
    pd_sum = 0
    sd_sum = 0

    for i in range(row):
        pd_sum += matrix[i][i]
        sd_sum += matrix[i][row - i - 1]

    # Compute absolute difference
    difference = abs(pd_sum - sd_sum)

    # Print results
    print(f"Sum of Primary Diagonal: {pd_sum}")
    print(f"Sum of Secondary Diagonal: {sd_sum}")
    print(f"Absolute Difference of Diagonals: {difference}")'''



#write a program to transpose the given matrix   09/09/25
'''row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

print("Enter the values for the matrix:")
matrix=[[int(input()) for j in range(col)] for i in range(row)]

print(" original matrix")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

print("Transposed matrix")
for i in range(col):
    for j in range(row):
        print(matrix[j][i],end=" ")
    print()'''



#write a program to rotate the given matrix 90degree to right side and display the output and makeshore that no.of rows and no.of columns should be same
'''row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

print("Enter the values for the matrix:")
matrix=[[int(input()) for j in range(col)] for i in range(row)]

print(" original matrix")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

print("transposed matrix")
for i in range(row):
    for j in range(col):
        print(matrix[j][i],end=" ")
    print()

print("rotated matrix")
for i in range(row):
    for j in range(col-1,-1,-1):
        print(matrix[j][i],end=" ")
    print()''' 



'''numbers = [1,2,3,4,5,6,7,8,9,10]
output = []

for number in numbers:
    if number % 2 == 0:
        if number % 4 == 0:
            output.append(f"{number} is divisible by 4")
        else:
            output.append(f"{number} is even")
print(output)'''










































#write a program to print count of vowels and consonents present in the given string 09/09/25
'''s='hey you beautiful'
vow=0
con=0
for i in s:
    if i==" ":
        continue
    elif i in "aeiouAEIOU":
                vow+=1
    else:
                con+=1
print(vow)
print(con)'''



#convert each character in the  given string to upper case if it is a lower case and vice versa
'''s='AjaY reDdY'
print(s)
res=""
for i in s:
    if i==" ":
        res+=i
    else:
        if 96<ord(i)<123:
                i=chr(ord(i)-32)
                res+=i
        else:
                i=chr(ord(i)+32)
                res+=i
print(res)'''
                  


#write a program to find the occurence or frequency of given character      10/09/25
'''s1="my name is ajay reddy bhumana,from nellore in andhra pradesh"
ch=input("Enter the character:")
cnt=0
for i in s1:
    if i==ch:
        cnt+=1
print(cnt)'''
         


'''s1="ABCD"
s2="wxyz"
s3=""
n=len(s1)
for i in range(n):
    s3+=s1[i]+s2[n-1-i]
print(s3)'''


   
'''s1="ABCD"
s2="wxyz"
s3=""
for i in range(len(s1)):
    s3+=s1[i]+s2[len(s2)-i-1]
print(s3)''' 



#write a program to convert given string from camel case to snake case
'''s1="This Is Ajay Kumar Bhumana!"
s2=""
for i in s1:
    if i>="A" and i<"Z":
        a=ord(i)+32
        s2+=chr(a)
    elif i>="a" and i<"z":
        s2+=i
    elif i==" ":
        s2+="_"
print(s2)'''



'''s1="This Is Mohan Kumar Tamilian!"
s2=""
for i in s1:
    if i==" ":
        s2+="_"
    elif i>='A' and i<='Z':
        s2+=chr(ord(i)+32)
    else:
        s2+=i
print(s2)'''



'''s1="this_is_hemanth_kumar!"
s2=""
s2+=chr(ord(s1[0])-32)
for i in range(1,len(s1)):
    if s1[i]=="_":
        s2+=" " 
    elif s1[i-1]=="_":
        s2+=chr(ord(s1[i])-32)
    else:
        s2+=s1[i]
print(s2)'''



#write a program to count total no.of special character in each word of special string  11/09/25
'''s1="If@@## you$$% Good@@## at$%"
print(s1)
s1=s1.split()
s2=""
for i in s1:
    cnt=0
    for j in i:
        if j>='A' and j<='Z' or j>='a' and j<='z':
            continue
        else:
            cnt+=1
    if cnt%2==0:
        s2+=i[::-1]+" "
    else:
        s2+=i+" "
print()
print(s2)'''



#write a program to check the given strings is anagram strings or not
'''s1="silent"
s2="listen"
dic1={}
dic2={}
if len(s1)==len(s2):
    for i in s1:
        if i not in dic1:
            dic1[i]=1
        else:
            dic1[i]+=1
    for i in s2:
        if i not in dic2:
            dic2[i]=1
        else:
            dic2[i]+=1
    if dic1==dic2:
        print("Anagram")
    else:
        print("not anagram")
else:
    print("Not Anagram")'''



#another method
'''def string_sorting(s):
    s=list(s)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]:
                s[i],s[j]=s[j],s[i]
    return"".join(s)
s1="school master"
s2="the classroom"
if string_sorting(s1)==string_sorting(s2):
    print("strings are anagram")
else:
    print("strings are not anagram")'''


         
#write a program the given string is panagram string or not
'''s1="Pack my Box with five dozen liquor jugs"
unique_char=set()
for i in s1:
    if i==" ":
        continue
    else:
        unique_char.add(i.lower())
if len(unique_char)==26:
    print("panagram string")
else:
    print("Not a panagram string")'''



#write a program to given string is palindrom or not
'''s1="madam"
if s1==s1[::-1]:
    print("palindrom")
else:
    print("Not a palindrom")'''



'''s1="madam"
j=len(s1)-1
for i in range(len(s1)):
    if s1[i]!=s1[j]:
        print("it is not a palindrome")
        break
    j-=1
else:
    print("string is a palindrome")'''



#write a program to check the given string can become a password or not   12/09/25
#1.check length must be >6 and <30
#2.it should contain atlest one upper case , one lower case , one numeric and one special case character
#3.if it is not satisfing the rules display string cannot be a password
'''s1=input("Enter the password:")
u=0
l=0
n=0
s=0
if len(s1)>6 and len(s1)<30:
    for i in s1:
        if i>='A' and i<='Z':
            u+=1
        elif i>='a' and i<='z':
            l+=1
        elif i>='0' and i<='9':
            n+=1
        else:
            s+=1
    if u==0:
        print("it should contain atlest one upper case")
    if l==0:
        print("it should contain atlest one lower case")
    if n==0:
        print("it should contain atlest one numeric character")
    if s==0:
        print("it should contain atlest one special character")
    elif u>=1 and l>=1 and n>=1 and s>=1:
        print("string can be a password")
else:
    print("Password should contain atlest 7 characters")'''



#program to insert the given second string in the middle of first string by converting first and last character of second string to the upper case
'''s1="ajay"
s2="madam"
mid=len(s1)//2
s3=""
print(mid)
for i in range(len(s1)):
    if i<mid:
        s3+=s1[i]
    elif i==mid:
        for j in range(len(s2)):
            if j==0 or j==len(s2)-1:
                s3+=chr(ord(s2[j])-32)
            else:
                s3+=s2[j]
        s3+=s1[i]
    else:
        s3+=s1[i]
print(s3)'''



#write a program to divid the given string into specied no.of chracters based on the given input 
#we need to ignore the space character in the given string
'''s1="iam ajay studying in pyspiders taken couse is python full stack with devops "
s2=""
n=8
a=0
for i in range(len(s1)):
    if s1[i]!=" ":
        a+=1
    if s1[i]!=" ":
        s2+=s1[i]
    if a==n:
        print(s2)
        s2=""
        a=0'''



#wap to divide given string into specified no of charcter and divide the given string   13/09/25
#you need to ignore the space character in the given string
'''s='mynameisbhumanaajaykumarreddy'
n=int(input("number:"))
res=""
cnt=0
for i in s:

    if cnt==n:
        res+='\n'
        cnt=0
    res+=i
    cnt+=1
print(res)'''



#mirror image or not
#AHIMOTUVWXY
'''def mirror(s):
    mir={'A','H','I','M','O','T','U','V','W','X','Y','0','8'}
    for i in s:
        if i not in mir:
            return  False
    return s
s=input("enter string:").upper()
if mirror(s):
    print(s,"mirror image")
else:
    print(s,"mirror image")'''



#string pattern
'''s=input("enter string:")
n=len(s)
mid=n//2
if n%2!=0:
    for i in range(n):
        for j in range(n):
            if i==mid:
                print(s[j],end=" ")
            elif j==mid:
                print(s[i],end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("not possible")'''



#write a program to upset the string and display the frequency of each character along with
#   its specified character    15/09/25
'''s1="aaaabbbbbccccccddeeeeeefff"
dic={}
s2=""
for i in s1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for a,b in dic.items():
        print(f"{a}{b}",end=" ")'''



#write a program
'''names = ["iron man", "spider man", "super man", "bat man"]
res = []
for name in names:
    acronym = ""
    for word in name.split():
        acronym += word[0].upper()
    res.append(acronym)
print(res)'''



#write a program to sort the words given in a list based on the count of Kth character
'''f=["apple","pineapple","mango","papaya","chikko","pomogranate"]
c1=[]
k=input("Enter the character:")
for i in range(len(f)):
    c=0
    for j in range(len(f[i])):
        if f[i][j]==k:
            c+=1
        c1+[c]
for i in range(len(c1)):
    for j in range(len(c1)-1):
        if c1[j]>c1[j+1]:
            c1[j],c1[j+1]=c1[j+1],c1[j]
            f[j],f[j+1]=f[j+1],f[j]
print(f)''' 



#write a program to check the second string is a sub-string of first string or not  16/09/25
'''s1="aaabbcccddabcdeefgg"
s2="abcd"
if s2 in s1:
    print("s2 is a sub string of s1")
else:
    print("s2 is not a sub string of s1")'''



'''def sub_string(s1,s2):
    for i in range(len(s1)):
        if s1[i:len(s2)+i]==s2:
            return True
    return False

s1="aaabbcccddabcdeefgg"
s2="abcd"
if sub_string(s1,s2):
    print("s2 is a sub string of s1")
else:
    print("s2 is not a sub string of s1")'''
   


'''def sub_string(s1,s2):
    cnt=0
    for i in range(len(s1) ):
        if s1[i:len(s2)+i]==s2:
            cnt+=1
    return cnt

s1="aaabbcccddabcdeefggabcdjjj"
s2="abcd"
cnt=sub_string(s1,s2)
if cnt:
    print("s2 occurs for",cnt,"times in s1")
else:
    print("s2 is not a sub string of s1")'''



#write a program to display all the posible ways of creating new string with the help of given string
'''s1="I YOU"
s2="LOVE PLAY"
s3="CRICKET FOOTBALL"
s1=s1.split()
s2=s2.split()
s3=s3.split()
for i in s1:
    for j in s2:
        for k in s3:
            print(i+" "+j+" "+k)'''



'''s1="I YOU"
s2="LOVE PLAY"
s3="CRICKET FOOTBALL"
s4=""
for i in s1.split():
    for j in s2.split():
        for k in s3.split():
            s4+=i+" "+j+" "+k+" "+"\n"
print(s4)'''        



#write a program to accept the string as a input and list as a output
'''s1="programs programs programs i dont like it i avoid but programs like me i cant avoid"
n= input('enter input:')
l=[]
s1=s1.split()
for i in range(len(s1)):
    if s1[i]==n:
        l+=[i]
print(l)'''



'''s1="programs programs programs i dont like it i avoid but programs like me i cant avoid"
n= input('enter input:')
res=[]
for i in range(len(s1.split())):
    if s1.split()[i]==n:
        res+=[i]
print(res)'''



'''s1="programs programs programs i dont like it i avoid but programs like me i cant avoid"
dic={}
s1=s1.split()
for i in range(len(s1)):
    if s1[i] not in dic:
        dic[s1[i]]=[i] 
    else:
        dic[s1[i]]+=[i]
for i,j in dic.items():
    print(i,":",j)'''



#write a program to accept string and integer as a input ,iterate through each character of given string and encript the given string using below critirea 
#check if the character is lower case find its ascii value and ascii value is even number add the value +4 ascii value and again convert to ascii character and store new string 
#if it is a odd number add +3 to it and again convert to ascii converter
#if character is upper then check its ascii value,if it is even add +2 or if it is odd add +5
#if character is numeric check it's ascii value and add the integer which accepts during user input and again convert into it's ascii character
#17/09/25
'''s1="abcD1"
n=6
s2=""
for i in s1:
    if i>="A" and i<="Z":
        if ord(i)%2==0:
            s2+=chr(ord(i)+2)
        else:
            s2+=chr(ord(i)+5)
    elif i>="a" and i<="z":
        if ord(i)%2==0:
            s2+=chr(ord(i)+4)
        else:
            s2+=chr(ord(i)+3)
    elif i>="0" and i<="9":
        s2+=chr(ord(i)+n)
    else:
        s2+=i
print(s2)'''
        


#create a class with the name my dictionery, and it should contains a mehods like add items,update items,delete items and display items
#when the object is created empty dictinery should create automatically
#add items method accept 2 perameters key and value, if the key and vale is not present add into dictionery,if it is already present no need to add
#when update item is called need to pass 2 parameters key and value,if key is already present modify the value,if it is not present no need do any change
#delete items to present accept only one parameter  key if the key is present key and value ,if key is not present no need to delete
#displlay items method need to display all the items in dictionery
'''class MyDictionary:
    def __init__(self):
        self.d1={}
    
    def addItems(self,k,v):
        if k not in self.d1:
            self.d1[k]=v
    
    def updateItems(self,k,v):
        if k in self.d1:
            self.d1[k]=v

    def deleteItems(self,k):
        if k in self.d1:
            del self.d1[k]

    def displayItems(self):
        print(self.d1)

md=MyDictionary()
md.addItems(1,"one")
md.addItems(2,"two")
md.addItems(3,"three")
md.displayItems() '''



#program using classes and object to create and working functionality of a wending machine
#it should contain attributes like items and cart
#methods like display items,display cart,add to cart and update cart,total price
#when the object is created it should create an empt cart and it should accept all the items alonge with its price
#18/09/25
'''class VendingMachine:
    def __init__(self, products):
        self.products = products
        self.cart = {}
    
    def display_products(self):
        for k, v in self.products.items():
            print(k, " : ", v)

    def display_cart(self):
        print("Items in cart:")
        if len(self.cart) == 0:
            print("No items in cart")
        else:
            for k, v in self.cart.items():   
                print(k, " : ", v)

    def add_to_cart(self, item, qty):
        if item in self.products:
            if item not in self.cart:
                self.cart[item] = qty
            else:
                self.cart[item] += qty

    def total_price(self):
        res = 0
        for k, v in self.cart.items():
            total = v * self.products[k]
            res += total
            print(k, " : ", v, "*", self.products[k], "=", total)
        print("-" * 30)
        print("Total price :", res)

products = {
    'kitkat': 25,
    'oreo': 30,
    'jimjam': 35,
    'bingo': 10,
    'chiki': 15,
    'cupcake': 5,
    'snikers': 15
}

vm = VendingMachine(products)
a=True
while a:
    print("List of all the products")
    vm.display_products()   # corrected
    print()
    print("1.Add to cart\n2.Display cart\n3.Total price")
    opt = int(input("Enter your option: "))
    match opt:
        case 1:
            item = input("Enter the item: ")
            qty = int(input("Enter the quantity: "))
            vm.add_to_cart(item, qty)
        case 2:
            vm.display_cart()
        case 3:
            a=False
            vm.total_price()
        case _:
            print("invalid option")'''



#write a program using classes and object
#take the train details,having the details like train number,train name,starting from,end,days of run and price of sleeper,general and ac
#each train details should be in the form of dictionary and all the train details should be in the form of list as follows
#create a method like get_train_name())[we should take train number and get train name],get_trains_in_a_day()[it should except day name as a parameter and it should display all the train names on that day ],
# get_total_fair()[it should except two parameters train number,dictionary of total seats eg:-{'general':120,'sleeper':20,'ac':30}]

'''class Train:
    def __init__(self, train_number, train_name, start, end, days, price):
        self.train_number = train_number
        self.train_name = train_name
        self.start = start
        self.end = end
        self.days = days  # list of days
        self.price = price  # dictionary {'general':50, 'sleeper':100, 'ac':200}

class Railway:
    def __init__(self):
        self.trains = []  # list to hold all train objects

    def add_train(self, train):
        self.trains.append(train)

    def get_train_name(self, train_number):
        for train in self.trains:
            if train.train_number == train_number:
                return train.train_name
        return "Train not found"

    def get_trains_in_a_day(self, day):
        result = []
        for train in self.trains:
            if day in train.days:
                result.append(train.train_name)
        return result

    def get_total_fare(self, train_number, seat_dict):
        for train in self.trains:
            if train.train_number == train_number:
                total = 0
                for seat_type, count in seat_dict.items():
                    if seat_type in train.price:
                        total += train.price[seat_type] * count
                return total
        return "Train not found"
# ---------------- Testing ----------------
# Creating Railway System
railway = Railway()

# Adding Trains
train1 = Train(101, "Express", "Hyderabad", "Chennai",
               ["Mon", "Wed", "Fri"], {"general": 100, "sleeper": 200, "ac": 500})
train2 = Train(102, "Superfast", "Delhi", "Mumbai",
               ["Tue", "Thu", "Sat"], {"general": 120, "sleeper": 250, "ac": 600})

railway.add_train(train1)
railway.add_train(train2)

# Get train name by number
print("Train name for 101:", railway.get_train_name(101))

# Get trains on Wednesday
print("Trains on Wednesday:", railway.get_trains_in_a_day("Wed"))

# Get total fare for train 101
seats = {'general': 2, 'sleeper': 1, 'ac': 1}
print("Total fare for train 101:", railway.get_total_fare(101, seats))'''



#write a program to build game of cards using classes and objects
#accept a list of cards during object creation time as follows
#cards=['2','3','4','5','6','7','8','9','10','A','K','Q','J']
#there are 4 types of cards like daimond,heart,spare,clube so the total cards we need to take total length into 4 types
#it should contain a method called card value,it accept card name and it should return its value, the card values need to takes as follows
# card_values={
#     '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'j':11,'q':12,'k':13,'a':14
# }
#the game need to play between two players,user and computer
#computer need to give random cards automatically and then user need to enter user card,this should happen continuously for total no of cards(13 rounds)
#in each round calculate the individual score of computer and user,atlast compare the values and display the winner,if the scores are equal then display draw match
# 20/09/25
'''import random
class GAME_OF_CARDS:
    def __init__(self):
        self.cards=['2','3','4','5','6','7','8','9','10','A','K','Q','J']*4
        random.shuffle(self.cards)
    
    def card_value(self,card_name):
        card_values={'2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9,'10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return card_values[card_name]
    
    def start_game(self,name):
        computer_score=0
        user_score=0
        for i in range(13):
            computer_card=random.choice(self.cards)
            print("Enter the cards like:",self.cards)
            user_card=input("Enter your card:")

            computer_card_value=self.card_value(computer_card)
            user_card_value=self.card_value(user_card)

            computer_score+=computer_card_value
            user_score+= user_card_value

        print("computer score:",computer_score)
        print("user score:",user_score)
        if computer_score>user_score:
            print("computer won the game!...")
        elif computer_score<user_score:
            print(name,"won the game!...")
        elif computer_score==user_score:
            print("Tie match")

game=GAME_OF_CARDS()
game.start_game("rahul")'''
            


'''import random
# Flight details dictionary
flights_details = {
    "flight_id": 83142,
    "flight_name": "Indigo",
    "start": "Bangalore",
    "destination": "Delhi",
    "price": 6800,
    "type": "domestic"
}

# Function to generate unique ticket number
def generate_ticket_number(flight_id):
    ticket_no = ""
    if flights_details["flight_id"] == flight_id:
        ticket_no += (
            flights_details["flight_name"][:3].upper() +
            flights_details["destination"][:3].upper() +
            str(random.randint(1111, 9999)) +
            flights_details["start"][:3].upper()
        )
    return ticket_no

# Function to book ticket
def book_ticket(flight_id, total_tickets):
    if flights_details["flight_id"] == flight_id:
        print("\n--- Flight Details ---")
        for key, value in flights_details.items():
            print(f"{key}: {value}")
        
        print("\nTicket is booked successfully!")
        total_cost = total_tickets * flights_details["price"]
        
        print(f"Number of Tickets: {total_tickets}")
        print(f"Total Cost: {total_cost}")
        
        # Generate ticket numbers
        print("\nGenerated Ticket Numbers:")
        for i in range(total_tickets):
            print(f"Ticket {i+1}: {generate_ticket_number(flight_id)}")
        print("\n--- Booking Confirmed ---")
    else:
        print("Flight ID not found!")

# Example usage
book_ticket(83142, 3)'''



#write a program to display the city name and the total population from the given details of each city, display the output for comparing all the citys and display maximum population with name and population       
# Step 1: Create the dictionary "States" as shown in the image
'''States = {
    "Karnataka": {
        "CM": "Siddaramaiah",
        "DCM": "D. K. Shivakumar",
        "population": 68000000,     # Population of Karnataka
        "total_gdp": 250000,        # Example GDP value
        "literacy": 75              # Literacy percentage
    },
    "Andhra": {
        "CM": "Y. S. Jagan Mohan Reddy",
        "DCM": "Pushpa Srivani",
        "population": 54000000,     # Population of Andhra
        "total_gdp": 150000,        # Example GDP value
        "literacy": 67              # Literacy percentage
    }
}

# Step 2: Display each state name and its population
print("State-wise Population:")
for state, details in States.items():
    print(f"{state} -> Population: {details['population']}")

# Step 3: Find the state with the maximum population
max_state = max(States.items(), key=lambda x: x[1]["population"])

print("\n State with Maximum Population:")
print(f"{max_state[0]} -> Population: {max_state[1]['population']}")'''


    
    


    



















































































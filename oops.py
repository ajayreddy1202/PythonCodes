# [::::::::::::::::::::::::::::::CLASS and OBJECT::::::::::::::::::::::::::::::]
# Syntax of a Class
'''class ClassName:
    # class variables
    # methods (functions)'''


# Syntax of Object Creation
'''class ClassName:
    # constructor
    def __init__(self,...):
        # initialize variables
        ...
    #methods
    def method_name(self):
        ...
# create object
obj=ClassName(arguments)'''


# Example 1: Simple Class and Object
'''class Employee:
    # constructor to initialize data
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    # Method
    def show_details(self):
        print("Employee Name:",self.name)
        print("Employee ID:",self.emp_id)
        print("Salary:",self.salary)
# creating objects
e1=Employee("ajay",101,50000)
e2=Employee("Ravi",102,60000)

# calling method
e1.show_details()
e2.show_details()'''


# Example 2: Company-Related Example (Real Scenario)
'''class Developer:
    def __init__(self,name,language,project):
        self.name=name
        self.language=language
        self.project=project
    def work(self):
        print(f"{self.name} is developing {self.project} using {self.language}")
d1=Developer("ajay","python","chatbot")
d2=Developer("sneha","java","banking app")
d1.work()
d2.work()'''


# Example 3: Class Variable vs Instance Variable
'''class Company:
    company_name="TechNova Pvt Ltd"  #class variable (shared by all)
    def __init__(self,emp_name,emp_id):
        self.emp_name=emp_name    #Instance variable (unique to object)
        self.emp_id=emp_id
    def show(self):
        print("Company:",Company.company_name)
        print("Employee:",self.emp_name,"|ID:",self.emp_id)
e1=Company("Ajay",101)
e2=Company("Uma",102) 
e1.show()
e2.show() '''  


# Example 4: Real-world Company Use Case
'''class Account:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"{self.name} deposite {amount}. New balance: {self.balance}")
acc1=Account(1001,"Ajay",20000)
acc2=Account(1002,"Vijay",30000)
acc1.deposite(5000)
acc2.deposite(2000)'''



# [::::::::::::::::::::::::::::::ENCAPSULATION::::::::::::::::::::::::::::::]

# 4. Company-Related Example: HDFC Bank – Account Encapsulation
'''class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no    #public
        self.name=name        #public
        self.__balance=balance  #private variable
    #method to deposit money (allowed way)
    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} deposited. New balance: {self.__balance}")
    # method to withdraw money
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance!")
    # method to check balance
    def get_balance(self):
        return self.__balance
# creating object
cust1=BankAccount(1001,"Ajay",10000)
cust1.deposit(5000)
cust1.withdraw(2000)
# trying to access private data directly
print(cust1.__balance)    # ❌ This will cause error'''




# [::::::::::::::::::::::::::::::INHERITANCE::::::::::::::::::::::::::::::]

# TYPE 1: Single Level Inheritance{Parent → Child}
# Base class
'''class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def show_details(self):
        print("Employee Name:",self.name)
        print("Employee ID:",self.emp_id)

# Derived class
class Developer(Employee):
    def __init__(self,name,emp_id,language):
        super().__init__(name,emp_id)
        self.language=language
    def show_language(self):
        print(f"{self.name} works on {self.language}")
dev=Developer("Ajay",101,"Python")
dev.show_details()
dev.show_language()'''



# TYPE 2: Multilevel Inheritance{Grandparent → Parent → Child}
'''class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name} is working")

class Developer(Employee):
    def develop(self):
        print(f"{self.name} write code")

class TeamLead(Developer):
    def manage_team(self):
        print(f"{self.name} manages the developer team")
lead=TeamLead("Ajay")
lead.work()
lead.develop()
lead.manage_team()'''


# TYPE 3: Multiple Inheritance{Parent1 + Parent2 → Child}
'''class Tester:
    def test(self):
        print("Testing the softer")

class Developer:
    def develop(self):
        print("Developing the software")

class DevTester(Developer,Tester):
    def role(self):
        print("Handles both development and Testing")
emp=DevTester()
emp.develop()
emp.test()
emp.role()'''



# TYPE 4: Hierarchical Inheritance
# {
    #    Employee
    #    /     \
 #  Developer   Manager
# }
'''class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name} works in the company")

class Developer(Employee):
    def develop(self):
        print(f"{self.name} develops applications")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} manages the team")
dev=Developer("Ajay")
mgr=Manager("Ravi")

dev.work()
dev.develop()

mgr.work()
mgr.manage()'''



# TYPE 5: Hybrid Inheritance
# {
    #       Employee
        #  /        \
#      Developer   Tester
        #  \        /
        #   TechLead
# }
'''class Employee:
    def show(self):
        print("I am an Employee")

class Developer(Employee):
    def develop(self):
        print("I develop code")

class Tester(Employee):
    def test(self):
        print("I test application")

class TechLead(Developer,Tester):
    def lead(self):
        print("I lead Dev & Test team")
lead=TechLead()
lead.show()
lead.develop()
lead.test()
lead.lead()'''


# [::::::::::::::::::::::::::::::POLYMORPHISM::::::::::::::::::::::::::::::]

# 1. Duck Typing (Dynamic Typing)
# Example: Company Communication System
'''class Developer:
    def work(self):
        print("Developer is writing code.")

class Tester:
    def work(self):
        print("Tester is testing the product.")

def company_work(employee):
    employee.work()
dev=Developer()
test=Tester()

company_work(dev)
company_work(test)'''


# 2. Method Overriding (Run-time Polymorphism)
# Example: IT Company Employee Roles
'''class Employee:
    def role(self):
        print("Employee works in company.")

class Developer(Employee):
    def role(self):       # overriding parent method
        print("Developer writes code.")

class Manager(Employee):
    def role(self):       # overriding parent method
        print("Manager manages the team.")

e1=Employee()
e2=Developer()
e3=Manager()

for emp in (e1,e2,e3):
    emp.role()'''


# 3. Method Overloading (Not directly supported)
# {you can simulate it using default arguments or variable arguments (*args)}
# Example: Salary Calculation in HR System
'''class HR:
    def calculate_salary(self,base,bonus=0):
        print("Total Salary:",base+bonus)
hr=HR()
hr.calculate_salary(50000)      #without bonus
hr.calculate_salary(50000,5000) #with bonus'''



# 4. Operator Overloading
# Example: Company Project Team Combining
'''class Team:
    def __init__(self,members):
        self.members=members
    def __add__(self,other):
        return Team(self.members + other.members)
    def display(self):
        print("Team Members:",self.members)
team1=Team(["Ajay","Arjun"])
team2=Team(["Uma","rao"])
team3=team1+team2     # '+' overloaded
team3.display()'''



# [::::::::::::::::::::::::::::::ABSTRACTION::::::::::::::::::::::::::::::]

# 1. Abstract Classes and Methods (Using abc module)
# Example: Company Payment System (Real Company Example)
'''from abc import ABC, abstractmethod
# Abstract Class
class Payment(ABC):
    @abstractmethod
    def payment_process(self,amount):
        pass

    @abstractmethod
    def payment_status(self):
        pass

# Child class1 
class CreditCardPayment(Payment):
    def payment_process(self, amount):
        print(f"Processing credit card payment of {amount}")

    def payment_status(self):
        print("Credit card Payment Successful")

# Child class2
class UpiPayment(Payment):
    def payment_process(self,amount):
        print(f"Processing UPI payment of {amount}")

    def payment_status(self):
        print("UPI Payment Successful")

cc=CreditCardPayment()
cc.payment_process(5000)
cc.payment_status()

upi=UpiPayment()
upi.payment_process(1500)
upi.payment_status()'''
       


# 2. Abstraction via Encapsulation
# Example: Company Employee Salary System
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary #private attribute
    
    def show_details(self):
        print("Name:",self.name)
        print("Salary Details Hidden for Security")

    def get_salary(self):
        return self.__salary  #controlled access

emp=Employee("Ajay",50000)
emp.show_details()
print("Access Salary:",emp.get_salary())'''








































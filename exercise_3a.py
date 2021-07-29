#Enter customer details
#For Review
print ("Kindly enter the details requested below:")
name = input("Enter your full name: ")

#Calculation of respondents age
import datetime
year_of_birth = int(input ("Enter year of birth: "))
age = datetime.datetime.now().year - year_of_birth

#The loop below verifys the pension fund based on age
if age <= 42:
         pension_fund = "ITP1"
elif age >= 43:
    pension_fund = "ITP2"
 #Pending details entered below
sex = input("Enter your sex: ")
salary = float (input("Enter your salary: "))
print ("Address options: malmo, lund, helsinborg")
address = input("Enter your address: ")

#The loop below verifys the tax deducted based on location
#Lund and Malmo share a similar tax percentage
if address == "malmo":
    tax = float ((27 * salary) / 100 )
    net_salary = float (salary - tax)
elif  address == "lund":
     tax = float((30 * salary) / 100)
     net_salary = float(salary - tax)
elif address == "helsinborg":
     tax = float((25 * salary) / 100)
     net_salary = float(salary - tax)
print("You details are as follows")
print("Name:", name)
print("Age:", age)
print("Sex:",sex)
print("Salary:", salary)
print("Address:", address)
print("You belong to", pension_fund)
print("Tax deducted:", tax)
print("Salary after Tax:", net_salary)

    








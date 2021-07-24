#Enter customer details
print ("Kindly enter the details requested below:")
name = input("Enter your full name: ")
age = int(input("Enter your age: "))

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
if address == "malmo" or address == "lund":
    tax = float ((32.42 * salary) / 100 )
    net_salary = float (salary - tax)
elif address == "helsinborg":
     tax = float((31.39 * salary) / 100)
     net_salary = float(salary - tax)
print("You details are as follows")
print(name)
print(age)
print(sex)
print(salary)
print(address)
print("You belong to", pension_fund)
print("Tax deducted", tax)
print("Salary after Tax", net_salary)

    






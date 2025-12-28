

#get the environment from user 

import platform

for i in range(5):
        
env = input("Enter the environment = ")

print("The user input enc is",env)


#simple arithmetic operations
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
print("Multiplication:",a*b)

# conditional statements
if env == "prod":
    print("Don't deploy on friday")
elif env == "dev":
    print("Safe to deploy any day")
else:
    print("Take backup & Test well")


choice = input("Enter the choice (press q to quit):")

while choice != 'q':
    num = int(input("Enter a number you want the table for: "))

# formatted string  
name  = input("Enter your friends name: ")
print(f"Hello friend,{name}")

for i in range(1,12):
    print(f"{num} x {i} = {num*i}")


# while loop
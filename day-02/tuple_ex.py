info = ('Surya', '1.0', '2024-06-10', 'A tuple to store information about various topics')
print(type(info))
print("Author is:", info[0])
print("Version is:", info[1])
print("Date is:", info[2])
print("Description is:", info[3])
# info[1] = '2.0'  # This will raise a TypeError since tuples are immutable
for item in info:
    print(item)
print(dir(info))
print(info.count.__doc__)
print(info.index.__doc__)

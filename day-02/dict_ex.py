
info = {
    'author': 'Surya',
    'version': '1.0',
    'date': '2024-06-10',
    'description': 'A dictionary to store information about various topics',
    'dict': 'True'
}

print("Who is author",info['author'])
print("Version is",info['version'])


info.update({'license':'MIT'})

print(info.get.__doc__)

# for i in info:
#     print(f"{i} : {info[i]}")

for key, value in info.items():
    print(f"{key} : {value}")
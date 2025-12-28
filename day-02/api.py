import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

for key, value in response.json().items():

    # if key == 'userId':
    #     if value in [100, 200, 300]:
    #         print('The user is valid in the system')

    if key == 'completed':
        if value == False:
            print('The data is not yet completed in Server') 

    # print(f"{key} : {value}")

# print(dir(response.json))
a= [100,200,True,3.45,"Sathya"]

print(type(a))
print(a)

clouds = list()
print(type(clouds))

clouds.append("Utho")
clouds.append("AWS")
clouds.append("Azure")
clouds.append("GCP")
print(clouds)

print("Length of the list is:", len(clouds))
print("Largest cloud provider is:", clouds[0])
print("Indian cloud provider is:", clouds[-1])

print(dir(clouds)) 
print(clouds.count.__doc__)

for cloud in clouds:
    if cloud == "GCP":
        print("GCP is the 3rd largest cloud provider")
    elif cloud == "Utho":
        print("Utho is an Indian cloud provider")
    elif cloud == "AWS":
        print("AWS is the largest cloud provider")
    elif cloud == "Azure" or cloud == "gcp":
        print(f"{cloud} is the 2nd largest cloud provider")
    else:
        print("No match found")



a = [100,200,300, True, 4.6] # 1st way to make a list
print(type(a))
a.append(500)
print(a)

clouds = list() # 2nd way to make a list
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
print(clouds)
print("Length of list is:", len(clouds))
print("World Leader for Cloud Service Provider is:",clouds[0])
print("Indian Cloud Service Provider is:",clouds[-1])

print(dir(clouds))
print(clouds.extend.__doc__)


# ['aws', 'azure', 'gcp', 'ibm', 'alibaba', 'utho']
# range(5) -> 0,1,2,3,4

# iterate a list
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Market Leader")
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} DevOps - Zero To Hero")
    else:
        print(f"{cloud} not found")
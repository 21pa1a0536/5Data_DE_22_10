#Using popitem()

dict1 = {1:"Rahul", 2:"Vijay", 3:"Sunil",4:"Hema", 5:"Vidya" }
while(dict1):
    key, value = dict1.popitem()
    print(key, value)

print("-------- Method 2 --------")

#Using Changing dictonary to list

dict1 = {1:"Rahul", 2:"Vijay", 3:"Sunil",4:"Hema", 5:"Vidya" }
lst = list(dict1.items())
start = 0
while(start<len(lst)):
    key, value = lst[start]
    print(key, value)
    start+=1



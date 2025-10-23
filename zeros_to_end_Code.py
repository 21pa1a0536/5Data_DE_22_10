# Input: [1,2,3,4,0,0,1,2,3,4,0,0,0,6]
# Output: [1,2,3,4,1,2,3,4,6,0,0,0,0,0]

#Using Count
a = [1,2,3,4,0,0,1,2,3,4,0,0,0,6]
b = []
count = 0
for i in a:
    if(i!=0):
        b.append(i)
    else:
        count+=1
print(b+[0]*count)
    


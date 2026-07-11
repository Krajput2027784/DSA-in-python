#find minimum number in list
arr = [2 , 30 , 47 , 60 , 100]
minvalue = arr[0]

for i in arr:
    if i < minvalue:
        i = minvalue
print("Lowest value:",minvalue)


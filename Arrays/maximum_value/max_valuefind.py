#find maximum value in list
my_array = [90 , 100 , 102 , 78 , 67]
max_value = my_array[0]

for i in my_array:
    if i > max_value:
        i = max_value
print("grater value:",max_value)

"""
Lists are a collection of data
"""
my_list = [25, 69, 47, 36, 87]
print(my_list)
print(my_list[2:6])

my_list.append(1000) #add an item at the end 
print(my_list)

my_list.insert(2, 1000) # insert an item in the given index 
print(my_list)

my_list.remove(87) #removes the value passed as a param
print(my_list)

my_list.pop(0) #removes the item of the index passed as a param
print(my_list)

my_list.sort() # order the list from the lowest to highest 
print(my_list)

#ASSIGNEMENT

# zoo = ["elephant", "monkey", "giraffe", "hippo", "lion"]
# zoo.pop(3)
# zoo.append("snake")
# zoo.pop(0)
# print(zoo)
# print(zoo[0:3])
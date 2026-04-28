"""
Dictionaries
"""
# user_dictionary = {
#     'username': 'user2',
#     'name' : 'Alice',
#     'age': 21
# }

# user_dictionary["married"] = False
# user_dictionary["type"] = "user"

# print(user_dictionary.get("username"))
# print(user_dictionary.get("name"))
# print(user_dictionary.get("age"))

# user_dictionary.pop("married")

# print(user_dictionary)

# #we can print the whole dictionary using a for loop
# for key, value in user_dictionary.items():
#     print(key, value)

# # or only the keyes
# for key in user_dictionary:
#     print(key)

# #copying a dictionary

# user_dictionary2 = user_dictionary.copy()
# user_dictionary2.pop("age")
# print(user_dictionary)

# user_dictionary.clear()
# print(user_dictionary)

# ASSIGNMENT

def create_dic(firstname, lastname, age):
    user = {
        "firstname" : firstname,
        "lastname" : lastname,
        "age": age
    }

    return user

solution = create_dic("natalia", "miatelli", 32)
print(solution)
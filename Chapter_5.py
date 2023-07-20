# number = 8
# if number <= 8:
#     print('Number is greater than 8')
# else:
#     print('Number is less than 8')

# name = "Destiny's Child"
# if name == "Destiny's Child":
#     print("Say my name, say my name", end=" ")
# print("If no one is around you", end=" ")
# if name:
#     print("Say baby I love you", end=" ")
# else:
#     print("If you ain't runnin' game", end=" ")



# x = 5
# y = 10
# i = "5"
# j = "10"
# if x == i and x != y:
#     print("Blackbird", end=" " )
# else:
#     print("singing", end=" ")
# print("in the", end=" ")
# if x < int(j) or i ==j : 
#     print("dead", end=" ")
# else:
#     print("of night", end=" " )

# x = 5
# print("A spoon", end=" ")
# if x == 4 or x==5:
#     print("full of", end=" ")
# elif x>=4:
#     print("sugar", end= " ")
# else:
#     print("helps the medicine", end=" ")
# print("go down", end=" ")


# my_dict = {
#     "name":"troy Aikman",
#     "position": "qb",
#     "team":"Dallas Cowboys",
#     "age": 54,
#     "weight": 220.,
#     "superbowls":["XXVII", "XXVIII", "XXX"],
#     "awards": {
#         "super_bowl_mvp":"XXVII",
#         "probowl":[1991,1992,1993,1994,1995,1996],
#         "man_of_the_year": 1997
#     }
#     }
# for key in my_dict:
#     if key> "position":
#         print(key, end=" ")

# my_dict = {
#     "name":"troy Aikman",
#     "position": "qb",
#     "team":"Dallas Cowboys",
#     "age": 54,
#     "weight": 220.,
#     "superbowls":["XXVII", "XXVIII", "XXX"],
#     "awards": {
#         "super_bowl_mvp":"XXVII",
#         "probowl":[1991,1992,1993,1994,1995,1996],
#         "man_of_the_year": 1997
#     }
#     }
# # my_dict["awards"]["probowl"].reverse()
# # print(my_dict["awards"]["probowl"].pop(2))

# # print(my_dict["awards"]["probowl"].pop(2))

# # 
# a_list=[]
# for k, v in my_dict["awards"].items():
#     if k == "superbowl_mvp" or k =="man_of_the_year":
#         a_list.append(v)
# print(a_list)



# pets = []

# pet = {
#     'type':'dog',
#     'name':'tod',
#     'owner':'sara',
# }

# pets.append(pet)

# pet = {
#     'type':'cat',
#     'name':'george',
#     'owner':'Larry',
# }

# pets.append(pet)

# for pet in pets:
#     print(f"\nHere's What I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")
        

# car = input("What kind of car would you like to rent? ")
# print("Hello, we are grabbing that " + car.title() + " for you!")    
# 


number = input("How many people are in the dinner group? ")
number = int(number)

if number >= 8:
    print("\n You will have to wait")
else:
    print("\nYour table is ready!")
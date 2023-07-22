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


# number = input("How many people are in the dinner group? ")
# number = int(number)

# if number >= 8:
#     print("\n You will have to wait")
# else:
#     print("\nYour table is ready!")

# number="syd"to 

# number = input("Enter a number and I will tell you if it is a multiple of 10: ")
# number = int(number)

# if number % 10 == 0:
#     print("\nThe number " + str(number) + " is a multiple of 10.")
# else:
#     print ("\n"+ str(number) + " is not a multiple of 10")


# dict_1 = {'name':'reece','height':'short', 'hair':'blonde'}
# dict_2 = {'name':'Bobby', 'height':'tall', 'hair':'brown'}

# my_list = (dict_1, dict_2)
 
# print(f"this is my list ${my_list}")

# for pet in my_list:
#     print(f"\nHere's What I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")

# number = 3
# while number < 5:
#     print(number)
#     number += 1

# age = int(input("What is your age?"))
# while age > 10:
#     age-=1
#     print(age, end=" ")

# while False:
#     print("My" , end= " ")
#     print("Name", end= " ")
#     continue
#     print("is", end=" ")
#     break
#     print("chika-chika", end= " ")

# print("done")

# age = 13
# while age > 10:
#     print("You are too old!", end= " ")
#     if age == 13:
#         break
#     age+=1

# print(1%2)
    
# age = 1
# while age < 10:
#     if age % 2 == 1:
#         if age == 3:
#             print("ding", end= " ")
#         elif age == 4:
#             print("dong", end= " ")
#         elif age == 5:
#             print("the", end=" ")
#         print("which", end=" ")
#     age += 1
# print("is dead", end=" ")

# num = 1
# new_num = 0
# while num < 10:
#     for i in range(3):
#         new_num += 1
#     num +=2
# print(new_num)

# i = 6
# while i <= 10:
#     for j in range (3):
#         i*=j+2
#         print(j,end=" ")
#         break

# def make_shirt(size,moto):
#     if size in 'small':
#         print("This is your option:" + moto.title())
#     else:
#         print("Sorry, we don't have that option in your size")

# make_shirt(size='small',moto='You suck')


# x = 5
# def some_func(x):
#     print(x, end=" ")
# print(x, end=" ")
# some_func(1)
# x = x - 1
# print(x, end=" ")
# some_func(1)

# def do_something(a_list):
#     my_string=""
#     for element in a_list:
#         my_string += element[0]
#     return my_string
# aladdin_characters = ['Jasmine', 'Aladdine', 'Aboo', 'Razul']
# print(do_something(aladdin_characters))

def make_shirt(size,moto):
    sizes=['small', 'medium']
    if size in sizes:
        print("This is your option:" + moto.title())
    else:
        print("Sorry, we don't have that option in your size")

make_shirt(size='small',moto='You suck')
# x = 17

# if x > 10:
#     print('x is big')
#     # print('look at his kid')
# elif x == 10:
#     print('x is small')
# else:
#     print('x is tiny')
# del
# clear
# my_list = ["chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
# for index in my_list:
#     print(index, end=' ')
# my_list = ["it's", "peanut btter", "jelly", "time"]
# new_word=''
# for word in my_list:
#     new_word += word + " "
# print (new_word)    

# my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "Macaroni"]
# my_string = ""
# for index, object in enumerate(my_list):
#     my_string += object + " "
#     if index == 3 or index == 4:
#         my_string += "and "
# print(my_string)

# my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "Macaroni"]
# for index in range(3):
#     print(my_list[index], end=" ")

# my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "Macaroni"]
# my_string = ""
# for index in range(len(my_list)):
#     if index ==6:
#         my_string += "chillin' with my homie"
#     my_string[index] = "chicken wing"
# print(my_string)

# my_list = [1, 3.0,["a","b",["A","B", "C"], "d"], "john"]
# for member in my_list:
#     if isinstance(member, list):
#         for m in member:
#             if isinstance(m, list):
#                 print(m,end=" ")

# my_list = [1, 3.0,["a","b",["A","B", "C"], "d"], "john"]
# print(my_list[2][2][0])

# my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "Macaroni"]
# for food in my_list:
#    
#         continue
#     print(food, end=" ")

my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "Macaroni"]
for food in my_list:
    if food == "chicken wing":
        break
    print(food, end= " ")

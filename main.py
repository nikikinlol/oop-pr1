# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# myString = "hello"
# myFloat = 10.0
# myInt = 20
#
# if myString == "hello":
#     print("string %s" % myString)
# if isinstance(myFloat, float) and myString == 10.0:
#     print("FLoat: %f" % myFloat)
# if isinstance(myInt, int) and myInt == 20:
#     print("Integer: %d" % myInt)

#       lists
# myList = [1,2,3]
# myList.append("hello")
# print(myList[0])
#       Basic Opetators
# hellworld = "hello" + " " + "fck"
# print(hellworld)
# even_numbers = [2,3,4,5]
# odd_numvers = [1,2,4,5,6]
# all_numbers = odd_numvers + even_numbers
# print(all_numbers)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

name = "John"
print("Hello, %s!" % name)
gg = "alex"
age = 23
print("%s is %d years old." % (gg, age))

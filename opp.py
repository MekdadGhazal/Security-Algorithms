

class Point:
    def __int__(self, x=0, y=0):  # constructor with parameters [self is object like 'this']
        self.xCoord = x
        self.yCoord = y

    def shift(self, xInc=1, yInc=2):
        self.xCoord += xInc
        self.yCoord += yInc

    def result(self):
        print(self.xCoord , self.yCoord)


# to make letter upper : ctrl + shift + u (toggle)
# to make a mark : ctrl + shift + number(1..9) (toggle)
# to comments all : ctrl + / (toggle)

# STRING METHODE:
# TO INPUT:

# fName = input("What's  Your first name? ")
# mName = input("What's  Your middle name? ")
# lName = input("What's  Your last name? ")

# TO MAKE IT WITHOUT SPACES(strip)
# AND MAKE IT FORMAT (capitalize)

# fName = fName.strip().capitalize()
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()

# TO PRINT IT IN ONE LINE
# 'mName:.1s'  MEANS THE FIRST LETTER JUST

# print(f"Hello {fName} {mName:.1s} {lName} ,Nice To meet YOU :)")


# # Dictionaries In Python :
# my_info = {
#     "name": "ali",
#     "age": '18',
#     "id": '8888',
# }
# print(my_info)
# print(my_info['name'] + ", " + my_info['age'])
# print('#################')
# for i in my_info:
#     print(i + " : " + my_info[i])
# print('#################')
# for i, j in my_info.items():
#     print("{} : {}".format(i, j))
# print('#################')
# for i, j in my_info.items():
#     print(f"hello Your {i} is {j} ")

def shape(w = 1, h = 1):
    return "the width =>", w ,"the height => ", h ,"the round => ", (w+h)*2 ,"the area => ", w*h

# print(type(2))
#
# x = 10
# print(type(range(x)))
#
# if (type(x) == "int"):
#     print('YES!')
# else: print("NO!")
# # print(shape(10 , 3))

point_x = Point()
# point_x.xCoord =10
# point_x.yCoord = 5
point_x.__int__(2 ,10)
point_x.shift(15 ,14)
print(point_x.xCoord)
point_x.result()


class Person:
    def __str__(self, fname="", lname =""):
        self.name = fname + " " + lname
        self.id =5

    def sayHello (self):
        print("HI " +self.name+ ", Nice to meet YOU :) ")
        print(self.id)

n = Person
n.__str__(n,"ali","ali")
n.sayHello(n)

def login(name, password, id='0', phone='0', zip='0', loc="#"):
    print (name +":"+ password+":"+id+":"+phone+":"+zip+":"+loc)


login("ali","147852","5","0938354715","5204","Syria")
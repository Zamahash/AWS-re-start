print("Python has 3 numeric types:int, float, complex")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=3.14
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
mystring="This is a string"
print(mystring)
print(type(mystring))
string1="fire"
string2="water"
string3=string1+string2
print(string3)
#name = input("what is your name?")
#print(name)
##color = input("what is your favorite color? ")
#print(name)
#animal = input("what is your favorite animal? ")
#print(color)
#print("{}, you like a {} {}!".format(name,color,animal))
#print("{}, you like a {} {}!".format(name,color,animal))
myFruitlist = ["apple", "banana", "orange"]
print(myFruitlist)
print(type(myFruitlist))
print(myFruitlist[0])
print(myFruitlist[1])
myFruitlist[2] = "orange"
print(myFruitlist[2])
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

fruitDict = {
    "Akua" : "Apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(fruitDict)
print(type(fruitDict))
print(fruitDict["Akua"])
myMixedList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedList:
    print("{} is of the data type {}".format(item,type(item)))
    
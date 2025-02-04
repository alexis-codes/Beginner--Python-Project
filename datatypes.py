number = 50 #int (integer)
num = 56.98 #float (decimals)
greeting = "hello there" #str (string)
hasFeathers = True # booLean

#data structures
cars=["Mercedes", "Toyota", "Volvo"] #Lists;   In a Programme use te special brackets and commas in between string
#to access specific string use index followed by the vale e.g cars index 0 which is mercedes
fruits = ("banana", "Orange", "Apple" ) #turple
countries = {"England","France", "Germany"} #Set   ;does not follow an order,values are unchangeable
student = {
    "Firstname" : "Ann",
    "course" : "MIT",
    "age" : 19 ,
    "nationality" : "Kenyan"


}




print(number)
print(num)
print(greeting)
print(hasFeathers)


print(cars)
print(fruits)
print(countries)

print(student["nationality"]) #to access specific string using its assigned key


# Typecasting  ; a form of convrting one datatype to another
print (float(number))
print(int(num))
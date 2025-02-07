# Built in functions/Standard library functions

y = max(45,89,75,56,31)
print("The maximum value is",y)

x = min(85, 56,40,2,23)
print("The minimum value is", x)


#User-defined Functions
# To create a function use the key def (define)

def school():
    print("eMobilis")

#Call the created function in order to see the output
school()

def add():
    num1 = 5
    num2 = 3
    print(num1 + num2)
add()



#Parameters and arguements

#Parameter is a variable
#arguement is the value stored in the parameter when calling the function

def multiply(a , b):
    print( a * b)
multiply(5,6)
multiply(7,10)



#Creating employee data

def employee(name, age, gender, salary, position):
    print(name,age,gender,salary,position)

employee("Alexis",18,"Female",560000,"CEO")
employee("John",56,"Male",360000,"Managing Director")
employee("Mark",30,"Male",310000,"Programmes developer")
employee("Debbie",25,"Female",300000,"Personal assistant")
employee("Culrt",18,"Male",200000,"Security")
employee("Pinky",27,"Female",1000000,"Secretary")



#A program to display details of 5 patients
#Using a user-defined function implement parameter and arguement
#fullname, gender, age, disease


def patients(fullname, gender, age, disease):
    print(fullname, gender, age, disease)

patients("Siri Khalim", "Male", 56, "Cancer")
patients("Maria Antoinette", "Female", 73, "Diabetes")
patients("John Mark", "Male", 66, "Hypertension")
patients("Fiona Flora", "Female", 44, "Liver Cirrhosis")
patients("Rose Silvester", "Female", 88, "Dymensia")

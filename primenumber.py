#program to check whether a number is prime

number = (int(input("Enter number: ")))

if number <= 1 :
    print("Not prime")
elif number :
    print ("Prime")
else :
    print("Prime")

for x in range (2,number):
    if number / x == 0 :
        print("Not prime")

# A pythonn programme that checks for room temperature


temperature = 23
if temperature > 25 :
    print ("it is too hot")
else :
    print("it is too cold")


# A program that returns the largest number
first = 3
second = 1
third = 2


if first > second and first > third :
    print(first, "is the largest number")
elif second > first and second > third :
    print(second, "us the largest number")
else :
    print(third, "is the largest number")


#program to check a number and return whether even or odd

num=int (input(print("enter number__ ")))
if num == 0 :
    print("neutral number")
elif (num % 2) == 0:
    print("Even Number")
else:
    print("Odd Number")
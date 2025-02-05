#A simple python project to
#check whether a year is a leap year on not
year = int(input("Enter Year "))
if year % 4 == 0 or year % 100 == 0 or year % 400 == 0 :
    print (year,"is a leap year")
else :
    print(year,"is not leap")




#A letter is a vowel or a consonant
x = str(input("Type letter "))
if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
    print("Vowel")
else:
    print("Consonant")

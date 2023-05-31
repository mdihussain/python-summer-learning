#MD Hussain
#Day 5
#Control Structures
#Learned extra stuff along the way and decided to incorporate

while True:
    try:
        number = int(input("Enter your number: "))
        print("Thank you!")
        if number > 0:
            print("Your number is positive :)")
        elif number < 0:
            print("Your number is negative :(")
        elif number == 0:
            print("Your number is neither positive nor negative :|")
        break

    except ValueError:
        print("Your entry is not a number :\ ")
   
print("  ")
print("The numbers from 1 to 9 are the following:")
for i in range(9):
    print(i+1)

number = 1
print("  ")
print("The numbers from 1 to 10 are the following:  ")

while number < 11:
    print(number)
    number += 1
    

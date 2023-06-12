#Md Hussain
#Day6
while True:
    try:
        Number1 = int(input("Please enter your first number: "))
        Number2 = int(input("Please enter your second number: "))
        Guess = int(input("Please enter what you think your two numbers add up to: "))
        Answer = Number1 + Number2
        if Answer == Guess:
            print("You've answered it correctly")

        else:
            print("You've answered it incorrectly")
        break
    except ValueError:
        print("Your entry might not be a number")

def add_two_numbers(x ,y):
    d = x+y
    return d

    

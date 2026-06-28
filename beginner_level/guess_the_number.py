import random

# welcome message
print("Hello User! Welcome to the number guessing game!\n")

# prompt the user to enter the lowest number in the set
low = int(input("Enter the lowest number: "))
# prompt the user to enter the highest number in the set
high = int(input("Enter the highest number in the set: "))

# giving the instructions to the user
print(f"\nYou have 10 chances. The number lies between {low} and {high}\n")

# prompt the user to answer if they are ready
while True:
    answer = input("Are you ready? Yes or No: ").strip().lower()
    
    # defining the different input cases
    if answer.startswith("y"):
        ready = True
        break
    elif answer.startswith("n"):
        print("No problem, rerun the program when you want!")
        ready = False
        break
    else:
        print("Please type 'Yes' or 'No'!")
        
# defining the guessing number together with the counter and number of guesses
num = random.randint(low, high)
chances = 10
counter = 0

# defining the first hint
if num % 2 == 0:
    print("Hint: The number is EvEn :)\n")
else:
    print("Hint: The number is OdD :)\n")
    
# while loop to control the number of chances
while counter < chances:
    # second hint
    if counter == 1:
        want = input("Do you want a hint? Yes or No: ").strip().lower()
        if want.startswith("y"):
            if num % 10 == 0: 
                print("Hint: yes, the number is divisible by TEN\n")
            else:
                print("Hint: the number is NOT divisible by ten\n")
                
    # third hint
    elif counter == 2:
        want = input("Do you want a hint? Yes or No: ").strip().lower()
        if want.startswith("y"):
             if num % 2 != 0:
                # odd number -> check divisibility by 3
                if num % 3 == 0:
                    print("Hint: yes, the odd number IS divisible by 3.\n")
                else:
                    print("Hint: no, the odd number is NOT divisible by 3.\n")
        else:
            # even number -> check divisibility by 4
            if num % 4 == 0:
                print("Hint: yes, the even number IS divisible by 4.\n")
            else:
                print("Hint: no, the even number is NOT divisible by 4.\n")
                
    counter += 1
    guess = int(input("Enter your guess: "))
    
    # case 1: the user has found the answer
    if guess == num:
        print(f"Bravo! You have found the answer which is {num}! You found it after {counter} guesses.")
        break
    elif guess > num:
        print("Your guess was too high, try again later...")
    else:
        print("Your guess was too low, try again later...")
        
# loop ended with no correct guess and counter exhausted
if guess != num:
    print(f"The number was {num}. You have exhausted the amount of trials, try again later...")
    
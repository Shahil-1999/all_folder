print("Welcome to number guessing game")
n = 30
number_of_guesses = 0
print("Number of guesses is limited to only 9 times")
while (number_of_guesses <= 9):
    a = int(input("Choose number between 1 to 50: "))
    if a > n:
        print("Youre guess is high")
    elif a < n:
        print ("Your guess is low")
    elif a == n:
        print("you guess right number")
        print(number_of_guesses,"no. of guesses you took to finish.")
        break
    number_of_guesses += 1
    print(9 - number_of_guesses, "no. of guesses left")
    

if(number_of_guesses > 9):
    print("Game Over")

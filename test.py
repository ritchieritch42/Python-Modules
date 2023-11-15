from check_guess import check_guess

guess = input("Guess: ")

answer = "Austin Ekeler"

if check_guess(guess, answer) == True:
    print("Correct")
else:
    print("Incorrect")
def check_guess(guess, answer):
    #Clean guess & answer string
    guess = guess.replace(" ", "").lower()
    answer = answer.replace(" ","").lower()

    #Ensure all characters are letters of the alphabet
    testguess = guess.isalpha()
    testanswer = answer.isalpha()

    if not testguess or not testanswer:
        return "Enter a word with solely letters of the alphabet"

    #Assign variables for the length of guess & answer
    sizeofguess = len(guess)
    sizeofanswer = len(answer)

    #Adjust the length of the variables as necessary
    if sizeofguess < sizeofanswer:
        guess+= " " * (sizeofanswer - sizeofguess)
        sizeofguess = sizeofanswer
    elif sizeofguess > sizeofanswer:
        guess = guess[:sizeofanswer]
        sizeofguess = sizeofanswer


    #Check if guess is exactly answer
    if guess == answer:
        return True

    #Else compare guess to answer & if guess is 80% correct, return true, otherwise false
    else:
        count = 0

        for character in range(sizeofguess):
            if answer[character] == guess[character]:
                count+= 1

        if count >= (sizeofanswer * 0.8):
            return True
        else:
            return False
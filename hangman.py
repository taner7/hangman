import random

def hangman():
    wordlist = ["python", "java", "kotlin", "javascript"]
    word = random.choice(wordlist)
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main += "_ "
                
        if main == word:
            print(main)
            print("Congratulations! You guessed the word.")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in valid_letters:
            guessmade += guess
        else:
            print("Enter a valid character.")
            guess = input()
        
        if guess not in word:
            turns -= 1
            
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            elif turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            else:
                print("You lose!")
                print("The word was", word)
                break

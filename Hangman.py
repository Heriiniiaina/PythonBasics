from random import choice 

def run_game():
    word:str = choice(["Banana","Apple","Computer","Keyboard"])

    guessed:str =""
    life:int = 3
    while life > 0:
        blanks:int = 0
        print("word: ", end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print(" _ ",end="")
                blanks+=1
        print()
        if blanks==0:
            print("You got it")
            break
        guess:str = input("Enter a character: ")
        if len(guess) > 1:
            print("Enter only one character")
        else:
            if guess in guessed:
                print(f"You have already use {guess} character! try with another letter")
                continue
            guessed +=guess

            if guess not in word:
                life -=1
                print(f"Sorry, that was wrong ... ({life}) tries remaining")

                if life ==0:
                    print("Sorry, you lose!")
                    break

if __name__ == '__main__':
    run_game()
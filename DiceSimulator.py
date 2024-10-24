import random

def rolls_dice(amount: int = 2) -> list[int]:
    if amount <=0:
        raise ValueError
    rolls: list[int] = []
    for i in range (amount):
        random_rolls = random.randint(1, 6)
        rolls.append(random_rolls)
    return rolls
def main():
    while True:
        try:
            user_input:str = input("How many dice would you like to roll ?: ")
            if user_input.lower()=="exit":
                print("Thanks for playing")
                break
            print(rolls_dice(int(user_input)))
        except ValueError:
            print("Enter a valid number")
if __name__ == '__main__':
    main()
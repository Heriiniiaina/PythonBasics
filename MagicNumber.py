from random import randint
lower_number:int = 1
higher_number:int = 10
random_number:int =  randint(lower_number,higher_number)
life = 5
def get_Number(lower_number: int,higher_number:int):
    number:int = int(input(f"Enter a number in range from {lower_number} to {higher_number}: "))
    return number

while True:
    print(f"Life: {life}")
    try:
        number:int = get_Number(lower_number, higher_number)
    except ValueError as e:
        print("Please enter a valid number")
        continue2
    if number > random_number:
        print("The number is lower")
    elif number < random_number:
        print("The number is higher")
    else:
        print("You guessed it")
        break
    
    life = life -1
    if life ==0:
        print(f"You lose ! the number was {random_number}")
        break
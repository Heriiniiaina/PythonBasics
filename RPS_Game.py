import random
import sys

class RPS:
    def __init__(self):
        self.moves :dict = {"rock":'🪨',"paper":'📄', "scissors":'✂️'}
        self.validmoves :list[str] = list(self.moves.keys())
    def play_game(self):
        user_move:str = input("rock, paper or scissors ! (or exit to quit) > ").lower()
        if(user_move=="exit"):
            print("Thanks for playing!")
            sys.exit()
        if(user_move not in self.validmoves):
            print("Invalid move")
            return self.play_game()
        ai_move:str = random.choice(self.validmoves)

        self.display_moves(user_move,ai_move)
    def display_moves(self,user_move: str,ai_move:str):
        print("---")
        print(f"You: {self.moves[user_move]}")
        print(f"Ai: {self.moves[ai_move]}")
        print("---")
        
        self.check_moves(user_move, ai_move)
    def check_moves(self,user_move:str,ai_move:str):
        if user_move==ai_move:
            print("It's a tie")
        elif user_move=="rock" and ai_move=="scissors":
            print("You win!")
        elif user_move=="paper" and ai_move=="rock":
            print("You win!")
        elif user_move=="scissors" and ai_move=="paper":
            print("You win!")
        else:
            print("Ai win")

if __name__ =="__main__":
    rps = RPS()
    while True:
        rps.play_game()
        
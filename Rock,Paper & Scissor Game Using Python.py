import random

def play():
    user=input("What's your choice  (r) for rock, (s) for scissor and (p) for paper?: ")
    computer=random.choice(["r","s","p"])

    if user==computer:
        return "It\'s a tie"
    
    if is_win(user,computer):
        return "You have win..Congrats!"

    return "You have lost"

def is_win(player,opponent):
    #if wins it returns true
    # r>s and p>s and p>s  it wins

    if (player=="r" and opponent=="s") or (player=="p" and opponent=="s") or (player=="p" and opponent=="s"):
        return True

print(play())
  

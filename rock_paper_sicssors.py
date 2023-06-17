import random
def play():
    user=input("what's your choice: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer=random.choice(['r','s','p'])
    
    if(user==computer):
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You won!'
    
    return 'You Lost!'

def is_win(player,opponent):
    if(player=='r' and opponent=='s') or (player=='p' and opponent=='r')\
        or (player=='s' and opponent=='p'):
            return True
        
        
print(play())
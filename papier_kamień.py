import random


emoji = {'r': '🪨', 's': '✂️', 'p': '🧻'}
choices = ('r', 'p', 's')

def get_user_choice():
    while True:
        pick = input('Rock, paper, scisors (r/p/s): ').lower()
        if pick in choices:
            return pick
        else:
            print('invalid choice')
            
def show_pick(pick, ai_pick):
    print(f'you chose {emoji[pick]}')
    print(f'computer chose {emoji[ai_pick]}')

def win_conditions(pick, ai_pick):
    if pick == ai_pick:
        print('Tie')
    elif (
        (pick == 'r' and ai_pick == 's') or 
        (pick == 's' and ai_pick == 'p') or 
        (pick == 'p' and ai_pick == 'r')):
        print('you win')
    else:
        print('you lose')

def play_game():
    while True:
        pick = get_user_choice()
        
        ai_pick = random.choice(choices)

        show_pick(pick, ai_pick)

        win_conditions(pick, ai_pick)

        next = input('Continue? y/n: ').lower()
        if next == 'n':
            break

play_game()
import random


emoji = {'r': '🪨', 's': '✂️', 'p': '🧻'}
choices = ('r', 'p', 's')

while True:
    pick = input('Rock, paper, scisors (r/p/s): ').lower()

    if pick not in choices:
        print('Invalid choice')
        continue

    ai_pick = random.choice(choices)


    print(f'you chose {emoji[pick]}')
    print(f'computer chose {emoji[ai_pick]}')

    if pick == ai_pick:
        print('Draw')
    elif (
        (pick == 'r' and ai_pick == 's') or 
        (pick == 's' and ai_pick == 'p') or 
        (pick == 'p' and ai_pick == 'r')):
        print('you win')
    else:
        print('you lose')

    next = input('Continue? y/n: ').lower()
    if next == 'n':
        break
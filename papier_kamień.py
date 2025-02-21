import random


emoji = {'r': '🪨', 's': '✂️', 'p': '🧻'}
choices = ('r', 'p', 's')
pick = input('Rock, paper, scisors (r/p/s): ').lower()

if pick not in choices:
    print('Invalid choice')

ai_pick = random.choice(choices)


print(f'you chose {emoji[pick]}')
print(f'computer chose {emoji[ai_pick]}')


import random
c=['rock','paper','scisors']
cg=random.choice(c)
p=input('Enter input :')
if cg==p:
    print('Its a TIE')
elif p=='paper' and cg=='rock':
    print('Yay! you win')
elif p=='scisors'and cg=='paper':
    print('Yay! you win')
elif p=='rock' and cg=='scisors':
    print('Yay! you win')
else:
    print('Game over! You lost...')
print(cg)
import random
c=['Rock','Paper','Scisors']
cg=random.choice(c)
p=input('Enter input :')
if cg==p:
    print('Its a TIE')
elif p =='paper' or p == 'PAPER' or p == 'Paper' and cg=='Rock':
    print('Yay! you win')
elif p =='Scisors' or p == 'scisors' or p == 'SCISORS' and cg=='paper':
    print('Yay! you win')
elif p == 'rock' or p == 'ROCK' or p == 'Rock' and cg=='Scisors':
    print('Yay! you win')
else:
    print('Game over! You lost...')
print(cg)
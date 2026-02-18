import random
c=['Rock','Paper','Scisors','rock','paper','scissor','ROCK','PAPER','SCISSOR']
cg=random.choice(c)
p=input('Start :')
if cg==p:
    print(cg)
    print('Its a TIE')
elif p =='paper' or p == 'PAPER' or p == 'Paper' and cg=='Rock':
    print(cg)
    print('Yay! you win')
elif p =='Scisors' or p == 'scisors' or p == 'SCISORS' and cg=='paper':
    print(cg)
    print('Yay! you win')
elif p == 'rock' or p == 'ROCK' or p == 'Rock' and cg=='Scisors':
    print(cg)
    print('Yay! you win')
else:
    print('Game over! You lost...')
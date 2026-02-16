import random

while True:
    print('Roll your dice')
    
    print('You Rolled ',random.randint(1,6))
    ag=input('Roll again (y/n) ?').lower()
    if ag == 'n':
        print('Thanks for playing!')
        break

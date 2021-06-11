import random

r = random.randint(1, 100)
count = 0

while True:
    count = count + 1

    num = input('please enter a number between 1 to 100: ')
    num = int(num)
    if num == r:
        print('you got it right!')
        break
    elif num > r: 
        print('your number is greater than the answer')
    else:
        print('your number is smaller than the answer')
    print('this is ', count, 'times')
import random
r = random.randint(1,100)
while True:
    guess = input('請猜數字: ')
    guess = int(guess)
    if guess == r:
        print('恭喜你猜對了!!!')
        break
    elif guess > r:
        print('比答案大 請再試試看')
    elif guess < r:
        print('比答案小 請再試試看')
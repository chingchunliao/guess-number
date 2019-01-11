import random
r = random.randint(1,100)
count = 0
while True:
    guess = input('請猜數字: ')
    guess = int(guess)
    count += 1 #count = count + 1
    if guess == r:
        print('恭喜你猜對了!!!')
        print('你已經猜了', count, '次') 
        break
    elif guess > r:
        print('比答案大 請再試試看')
    elif guess < r:
        print('比答案小 請再試試看')
    print('你已經猜了', count, '次') 
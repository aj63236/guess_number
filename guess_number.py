import random
r = random.randint(1 , 100)
print(r)

while True:
    guess = input("請猜一個數字:")
    guess = int(guess)
    if guess == r:
        print("恭喜你猜對了!")
        break
    elif guess > r:
        print("要猜得比答案小")
    else:
        print("要猜得比答案大")
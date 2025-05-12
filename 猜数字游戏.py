import random

def guess_number():
    number = random.randint(1, 100)
    guessed = False
    attempts = 0

    print("欢迎来到猜数字游戏！我想了一个1到100之间的整数。")

    while not guessed:
        try:
            guess = int(input("请输入你的猜测："))
            attempts += 1

            if guess == number:
                print(f"恭喜！你在{attempts}次尝试中猜对了数字。")
                guessed = True
            elif guess < number:
                print("你猜的数字小了，请再试一次。")
            else:
                print("你猜的数字大了，请再试一次。")
        except ValueError:
            print("请输入一个有效的整数。")


if __name__ == "__main__":
    guess_number()


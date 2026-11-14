import random
import sys


def main():
    n = get_level()
    score = 0
    print(f"Level: {n}")
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        ans = x + y
        for g in range(3):
            try:
                user = int(input(f"{x} + {y} = "))
                if ans == user:
                    score += 1
                    break
                else:
                    print("EEE")
                    if g == 2:
                        print(f"{x} + {y} = {ans}")

            except:
                print("EEE")
                if g == 2:
                    print(f"{x} + {y} = {ans}")

    print(f"score: {score}")


def get_level():
    while True:
        try:
            num = int(input("What level would you like to play? "))
            if num == 1 or num == 2 or num == 3:
                return num
        except:
            print("That is not a valid input! ")


def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        if level == 2:
            return random.randint(10, 99)
        if level == 3:
            return random.randint(100, 999)

    except ValueError:
        sys.exit("There was a value error, shut down program")


if __name__ == "__main__":
    main()

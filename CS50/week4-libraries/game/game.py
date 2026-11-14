import random
def main():
    n = get_level()
    find = random.randint(1,n)
    while True:
        guess = get_guess()
        if guess < find:
            print("Too small!")
        if guess > find:
            print("Too large!")
        if guess == find:
            print("Just right!")
            break


def get_level():
    while True:
        try:
            num = int(input("What level would you like to play? "))
            if num>0:
                return num
        except:
            print("Invalid number")
def get_guess():
    while True:
        try:
            g = int(input("What is your guess? "))
            if g>0:
                return g
        except:
            print("not valid guess")

main()


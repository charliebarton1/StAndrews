def main():
    x = input("What time is it?")
    realx = convert(x)
    if realx >= 7 and realx <= 8:
        print("breakfast time")
    elif realx >= 12 and realx <= 13:
        print("lunch time")
    elif realx >= 18 and realx <= 19:
        print("dinner time")



def convert(time):
    x, y = time.split(":")
    x = int(x)
    y = int(y)/60
    real = x + y
    return real


if __name__ == "__main__":
    main()

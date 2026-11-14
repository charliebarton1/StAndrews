
def main():
    fract = convert(input("how much fuel do you have? (X/Y) "))
    tank = gauge(fract)
    print(tank,end = "%")


def convert(fraction):
    try:
        div = fraction.split("/")
        a = int(div[0])
        b = int(div[1])
        if b < 0 or a < 0 or "-" in div:
            raise ValueError
        div = a/b
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    if div > 1:
        raise ValueError
    return int(round(div*100))


def gauge(percentage):
    if percentage <= 1 :
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()





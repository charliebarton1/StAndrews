
def main():
    x,y = get_int(input("how much fuel do you have? (X/Y) "))
    form(x,y)
    print(tank(x,y),end = "")


def get_int(inp):
    try:
        div = inp.split("/")
        a = int(div[0])
        b = int(div[1])
        return a,b
    except ValueError:
        main()

def form(a,b):
    if not a >= 0 or not b >= 0:
        main()
    if a > b:
        main()

def tank(a,b):
    if 0.01 < a/b < 0.99:
        return f"{int(round(a/b*100))}%"
    elif a/b >= 0.99:
        return "F"
    else:
        return "E"
main()





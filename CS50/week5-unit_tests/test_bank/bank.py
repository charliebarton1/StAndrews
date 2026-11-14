def main():
    val = value(input("How woudl you like to greet me?"))
    print(f"${val}")


def value(greeting):
    if not isinstance(greeting, str):
        raise TypeError
    greeting = greeting.lower().strip()
    if greeting.split(",")[0].strip() == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

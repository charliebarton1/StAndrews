import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"((?<![a-zA-Z])um([^a-zA-Z]|$))"
    if num := re.findall(pattern, s, re.IGNORECASE):
        return len(num)
    else:
       return 0





if __name__ == "__main__":
    main()

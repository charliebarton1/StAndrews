import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^\<iframe.+src=\"(?:(?:http|https):\/\/(?:www\.)?(?:youtube\.com\/embed\/)([A-Za-z0-9_:\/\.]+))\".+$"
    if matches := re.search(pattern,s):
        val =  "https://youtu.be/"+matches.group(1)
        return val

    else:
        return None

if __name__ == "__main__":
    main()

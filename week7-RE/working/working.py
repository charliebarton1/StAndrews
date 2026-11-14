import re
import sys


def main():
    use = convert(input("Hours: "))
    print(use, end="")


def convert(s):
    pattern = r"^(1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM)$"
    if matches := re.search(pattern, s):
        if matches.group(3) == "AM":
            if int(matches.group(1)) <= 9:
                hour = "0" + str(matches.group(1))
            else:
                hour = matches.group(1)
            if int(hour) == 12:
                hour = "00"
            if matches.group(2) != None:
                start = hour + ":" + matches.group(2)
            else:
                start = hour + ":00"
        if matches.group(3) == "PM":
            hour = int(matches.group(1)) + 12
            if hour == 24:
                hour = "12"
            if matches.group(2) != None:
                start = str(hour) + ":" + matches.group(2)
            else:
                start = str(hour) + ":00"
        if matches.group(6) == "AM":
            if int(matches.group(4)) <= 9:
                hour = "0" + str(matches.group(4))
            else:
                hour = matches.group(4)
            if int(hour) == 12:
                hour = "00"
            if matches.group(5) != None:
                end = hour + ":" + matches.group(5)
            else:
                end = hour + ":00"
        if matches.group(6) == "PM":
            hour = int(matches.group(4)) + 12
            if hour == 24:
                hour = "12"
            if matches.group(5) != None:
                end = str(hour) + ":" + matches.group(5)
            else:
                end = str(hour) + ":00"
    else:
        raise ValueError
    times = start + " to " + end
    return times


if __name__ == "__main__":
    main()

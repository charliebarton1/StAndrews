from datetime import date
import re
import sys
from num2words import num2words

class Date:

    today = date.today()

    def __init__(self, birthday):
        self.birthday = birthday
    def __str__(self):
        return f"{self.birthday}"
    @property
    def birthday(self):
        return self._birthday
    @birthday.setter
    def birthday(self,birthday):
        pattern = r"^(19[7-9]\d|20[0-1]\d|202[0-6])-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[0-1])$"
        if not re.match(pattern, birthday):
            sys.exit("invalid input")
        self._birthday = date.fromisoformat(birthday)

    def days(self):
        time_to_birth = abs(Date.today - self.birthday)
        return time_to_birth.days*24*60




def main():
    birthday = Date(input("What's your birthday? (yyyy-dd-mm)"))
    minutes = Date.days(birthday)
    print(f"{num2words(minutes)} minutes")





if __name__ == "__main__":
    main()

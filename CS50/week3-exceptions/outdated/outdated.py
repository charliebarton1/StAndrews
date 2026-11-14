def main():
    real = date(input("Please input a date: " ).strip())
    print(real, end = "")
def date(user):
        while True:
            try:

                if user.replace("/","").isnumeric():
                    new = user.split("/")
                    year= int(new[2])
                    month = int(new[0])
                    if month <= 9:
                        monthstr = f"0{month}"
                    else:
                        monthstr = month
                    day = int(new[1])
                    if day <= 9:
                        daystr = f"0{day}"
                    else:
                        daystr= day
                    if day <= 31 and month <= 12:
                        day = daystr
                        month = monthstr
                        return f"{year}-{month}-{day}"
                elif user[0].isalpha():
                    long = user.split(" ")
                    year =long[2]
                    month = month_dig[long[0]]
                    if "," in long[1]:
                        day = long[1].replace(",","")
                        day = day.strip()
                        if int(day) < 10:
                            day = "0"+day
                        if int(day) <= 31:
                            return f"{year}-{month}-{day}"
            except :
                main()
month_dig = {
    "January":  "01" ,
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}

main()

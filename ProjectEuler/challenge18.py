day = 2
count = 0 
for i in range(1901, 2001):
    day = day%7
    if day == 0: ##JAN 
        count += 1
    day += 3
    day = day%7
    if day == 0: ##FEB 
        count += 1
    leap = (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)
    day += 1 if leap else 0
    day = day%7
    if day == 0: ##March 
        count += 1
    day += 3
    day = day%7
    if day == 0: ##April 
        count += 1
    day += 2
    day = day%7
    if day == 0: ##May 
        count += 1
    day += 3
    day = day%7
    if day == 0: ##June
        count += 1
    day += 2
    day = day%7
    if day == 0: ##July 
        count += 1
    day += 3
    day = day%7
    if day == 0: ##August 
        count += 1
    day += 3
    day = day%7
    if day == 0: ##September 
        count += 1
    day += 2
    day = day%7
    if day == 0: ##October
        count += 1
    day += 3
    day = day%7
    if day == 0: ##November 
        count += 1
    day += 2
    day = day%7
    if day == 0: ##December  
        count += 1
    day += 3
    day = day%7
print(count)

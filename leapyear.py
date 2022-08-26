def is_leap(year):
    if year <= 1917:
        if (year % 4) == 0:
            return True
        else: 
            return False
    elif year >= 1919:
        if (year % 400)==0 and (year % 4)==0 and (year % 100)!=0:
            return True
        else:
            return False
    else: 
        return False

year = int(input())
(a) = is_leap(year)
print(a)
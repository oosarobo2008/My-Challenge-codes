 #Question: Given a year, determine whether it is a leap year. If it is a leap year, 
 # return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    if (year % 400) == 0:
        return True
    elif (year % 100) ==0:       
        return False
    elif (year % 4)==0 :
        return True
    else:
        return False

year = int(input('Enter the Year:'))
print(is_leap(year))


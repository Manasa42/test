year = int(input("enter the year"))

def leap(year):
    if (year%4==0):
        return ("it is a leap year")
    else:
        return ("it is not a leap year")

result = leap(year)
print (result)

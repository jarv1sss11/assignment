#determine if a year inputted is a leap year
Year=int(input("Enter a Year in the format YYYY\n"))

def isLeapYear(Year):
    if(Year%4==0 and (Year%100!=0 or Year%400==0)):
        print("Is a leap year")
    else:
        print("It's not a leap year")

isLeapYear(Year)
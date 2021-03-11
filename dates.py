import sys

#Author: Jordan Kettles 2147684
# Date: 10/03/21

#Read a date and determine whether it is a valid date
# between the years 1753 and 3000.

#Either state why the date is invalid.
# or outptu a valid date in the format
# <dd> <first three char of month> <yyyy>
# e.g. 02 Apr 1997
#month input could be the first three letters of the month
#name all in the same case, all with the first letter upper-case.
#seperators could be space, / or -

#calcutate whether the date is valid (29th of Feb)
#How do i calculate leap years?
#if the year is two numbers, it lies between 1950 and 2049.
#if >49 +1900 else +2000

#check if the first letter is uppercase:
#all follwing letters have to be the same case.

#if the first letter is lowercase:
#all following letters have to be lowercase.

#days lie between 01 and 31.

# If day is > 0 then it is a real day, but it might not be valid of that month.
def day(d):
    # 1-2
    if (3 > len(d) > 0):
        try:
            d_int = int(d)
        except:
            return 0
        if (32 > d_int > 0):
            return d_int
    return 0

#
def month(m):
    # 1-2
    if (3 > len(d) > 0):
        try:
            m_int = int(m)
        except:
            return None
        # 1-12
        if (13 > m_int > 0):
            return month_list[m_int - 1]
    # Is it a valid 3-letter month?
    if len(m) == 3:

        if m[0].isupper():
            if m[1:].isupper():
                m = m[0] + m[1:].lower()

        elif m.islower():
            m = m[0].upper() + m[1:]

        if m in month_list:
                return m

    return None

def day_and_month(d, m):
    #as int.
    day = day(d)
    #as 3-letter month.
    month = month(m)
    #Check if the day is valid for that month.
    return 0

if __name__ == "__main__":

    month_dict = {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May",
        6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov",
        12 : "Dec"}

    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for line in sys.stdin:
        line = line.strip()
        dash = line.split("-")
        slash = line.split("/")
        space = line.split(" ")

        #the seperators format is correct.
        if len(dash) == 3 and len(slash) == 1 and len(space) == 1:
            day = dash[0]
            month = dash[1]
            year = dash[2]

        elif len(slash) == 3 and len(dash) == 1 and len(space) == 1:
            day = slash[0]
            month = slash[1]
            year = slash[2]

        elif len(space) == 3 and len(dash) == 1 and len(slash) == 1:
            day = space[0]
            month = space[1]
            year = space[2]

        else:
            reason = "Separator Type"
            print("INVALID: " + reason)

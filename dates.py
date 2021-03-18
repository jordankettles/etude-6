import sys

#Author: Jordan Kettles 2147684
# Date: 10/03/21

def print_invalid(input, reason):
    print(input + " - INVALID: " + reason)

# Returns true if the year is a leap year, else false.
def leap_year_check(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True

            return False

        return True

    return False

# If day is > 0 then it is a real day, but it might not be valid of that month.
def validate_day(input, d):
    # 1-2
    if (3 > len(d) > 0):
        try:
            d_int = int(d)

        except:
            print_invalid(input, "Day is not a number.")
            return 0

        if (32 > d_int > 0):
            return d_int

        elif d_int > 31:
            print_invalid(input, "Day is too large.")
            return 0

        else:
            print_invalid(input, "Day is too small.")
            return 0

    elif len(d) > 2:
        print_invalid(input, "Day has too many characters.")
        return 0

    print_invalid(input, "Day does not have any characters.")
    return 0


def validate_month(input, m):
    # 1-2
    if (3 > len(m) > 0):
        try:
            m_int = int(m)
        except:
            print_invalid(input, "Month has less than 3 characters but is not a number.")
            return 0
        # 1-12
        if (13 > m_int > 0):
            return m_int

        elif m_int > 12:
            print_invalid(input, "Month is too large.")
            return 0

        print_invalid(input, "Month is too small.")
        return 0
    # Is it a valid 3-letter month?
    if len(m) == 3:

        if m[0].isupper():
            if m[1:].isupper():
                m = m[0] + m[1:].lower()

        elif m.islower():
            m = m[0].upper() + m[1:]

        # For each month
        for i in range(12):
            if month_list[i] == m:
                return i+1

        else:
            print_invalid(input, "Month is not a valid month.")
            return 0

    elif len(m) > 3:
        print_invalid(input, "Month has too many characters.")
        return 0

    print_invalid(input, "Month does not have any characters.")
    return 0

def validate_year(input, y):

    if len(y) == 4:
        try:
            y = int(y)
        except:
            print_invalid(input, "Year is not a valid number.")
            return 0
        # 1753 - 3000
        if (1752 < y < 3000):
            return y

        elif y > 2999:
            print_invalid(input, "Year is too large.")
            return 0

        else:
            print_invalid(input, "Year is too small.")
            return 0

    elif len(y) == 3:
        print_invalid(input, "Year cannot have 3 characters.")
        return 0

    elif len(y) == 2:
        try:
            y = int(y)
        except:
            print_invalid(input, "Year is not a valid number.")
            return 0
        # 1950 - 1999
        if y > 49:
            return 1900 + y
        # 2000 - 2049
        elif y >= 0:
            return 2000 + y

        print_invalid(input, "Year is too small.")
        return 0


    elif len(y) > 4:
        print_invalid(input, "Year has too many characters.")
        return 0

    elif len(y) == 1:
        print_invalid(input, "Year has only 1 character.")
        return 0

    print_invalid(input, "Year does not have any characters")
    return 0

def validate_dm(input, d, m):
    #int.
    day = validate_day(input, d)
    # If it was invalid.
    if day == 0:
        return None
    #3-letter string.
    month = validate_month(input, m)
    # If it was invalid
    if month == 0:
        return None
        #do some checks.
    #Check if the day is valid for that month.
    if day > 30 and month in [2, 4, 6, 9, 11]:
        print_invalid(input, month_list[month-1] + " has less than 31 days.")
        return None
    # Check if Feb and not greater than 29. Whether or not the year is a leap
    # year is not checked yet.
    if month == 2 and day > 29:
        print_invalid(input, "Feb has less than 30 days.")
    # 28 Feb except on a leap year 29.
    return day, month

def validate_dmy(input, d, m, y):
    dm = validate_dm(input, d, m)

    if dm != None:
        day = dm[0]
        month = dm[1]
        year = validate_year(input, y)
        if year == 0:
            return

        #Check for leap years.
        if (month == 2 and day == 29):
            if not leap_year_check(year):
                print_invalid(input, str(year) + " is not a leap year.")
                return
        #The Date is a valid date.
        day_str = str(day)
        # Add 0 to the start of the day string if the day has one digit.
        if len(day_str) == 1:
            day_str = "0" + day_str

        month_str = month_list[month-1]
        year_str = str(year)
        print(day_str + " " + month_str + " " + year_str)


if __name__ == "__main__":

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
            validate_dmy(line, day, month, year)

        elif len(slash) == 3 and len(dash) == 1 and len(space) == 1:
            day = slash[0]
            month = slash[1]
            year = slash[2]
            validate_dmy(line, day, month, year)

        elif len(space) == 3 and len(dash) == 1 and len(slash) == 1:
            day = space[0]
            month = space[1]
            year = space[2]
            validate_dmy(line, day, month, year)

        else:
            # PLACEHOLDER.
            print_invalid(line, "Does not follow the correct format.")

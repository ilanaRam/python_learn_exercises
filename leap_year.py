
def is_leap_year(year):
    is_leap = False

    print(f"input is: {year}")

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        is_leap = True
        print("the year is leap")
    else:
        print("the year isnt leap")



if __name__ == '__main__':
    year = int(input(" please enter year: "))
    is_leap_year(year)

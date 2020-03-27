# Written: 07-Dec-2019
# https://edabit.com/challenge/co4nwXSvnCjGEu8vp

def format_date(date):
    date = date.split("/")
    date.reverse()
    return "".join(date)
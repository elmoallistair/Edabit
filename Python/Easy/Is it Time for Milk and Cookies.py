# Written: 27-Mar-2020
# https://edabit.com/challenge/6nSckbgCx9hjTwmcw

import datetime
def time_for_milk_and_cookies(date):
    date = ''.join(str(date).split('-'))
    return date[4::] == '1224'
    # return '12-24' in str(date)
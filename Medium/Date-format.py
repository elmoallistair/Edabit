# Written: 07-Dec-2019
'''
* Instructions:
*   Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
*
*   Examples
*     format_date("11/12/2019") ->➞ "20191211"
*     format_date("12/31/2019") ->➞ "20193112"
*     format_date("01/15/2019") ->➞ "20191501"
*
*   Notes
*     Return value should be a string.
*
* Resources:
*   - https://stackabuse.com/how-to-format-dates-in-python/
*   - https://docs.python.org/3/library/datetime.html
*   - https://www.w3schools.com/python/ref_string_split.asp
'''

# =======================================================================================

def format_date(date):
    date = date.split("/")
    date.reverse()
    return "".join(date)

print(format_date("11/12/2019"))    # Output: 20191211
print(format_date("12/31/2019"))    # Output: 20193112
print(format_date("01/15/2019"))    # Output: 20191501


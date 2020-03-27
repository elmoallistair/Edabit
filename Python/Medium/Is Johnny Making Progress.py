# Written: 08-Dec-2019
# Link: https://edabit.com/challenge/2yHQwkecEHZBfHcmN

def progress_days(runs):
    progress = 0
    for days in range(len(runs)-1):
        if runs[days] < runs[days+1]:
            progress += 1
    return progress
    # return len([days for days in range(len(runs)-1) if runs[days] < runs[days+1]])
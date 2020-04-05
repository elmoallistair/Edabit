# Written: 26-Dec-2019
# https://edabit.com/challenge/pnd7xPYuvogkNfHg6

def get_best_student(grades):
  # Calculate the average
  check_ave = ([sum(i)/len(i) for i in grades.values()])

  # Find the biggest average
  highest = max(check_ave)

  # list out keys and values separately
  key_list = list(grades.keys())
  val_list = list(check_ave)

  # Get key(name) by its value(highest average)
  result = key_list[val_list.index(highest)]
  return result
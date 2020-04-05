## Combined Consecutive Sequence
Write a function that returns `True` if two lists, when combined, form a 
consecutive sequence.

### Examples
```
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
```

### Notes
* The input lists will have unique values.
* The input lists can be in any order.
* A consecutive sequence is a sequence without any gaps in the integers, e.g. `1, 2, 3, 4, 5` is a consecutive sequence, but `1, 2, 4, 5` is not.
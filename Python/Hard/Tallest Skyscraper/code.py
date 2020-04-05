# Written: 05-Apr-2020
# https://edabit.com/challenge/76ibd8jZxvhAwDskb

def tallest_skyscraper(lst):
    temp = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            temp.append(0)
            if lst[i][j] == 1:
                temp[j]+=1
    return max(temp)
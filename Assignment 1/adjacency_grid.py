# To print the grid with no adjacent number +/- 1

from itertools import permutations


# Check_cell function will check if the current list of number
# satisfy the condition (no adjacent number)
def check_cell(current_list):
    for _ in range(8):
        for i in range(8):
            if _ == 0 and (i == 1 or i == 2 or i == 3):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 1 and (i == 0 or i == 2 or i == 4 or i == 5):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 2 and (i == 0 or i == 1 or i == 3 or i == 4 or i == 5 or i == 6):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 3 and (i == 0 or i == 2 or i == 5 or i == 6):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 4 and (i == 1 or i == 2 or i == 5 or i == 7):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 5 and (i == 1 or i == 2 or i == 3 or i == 4 or i == 6 or i == 7):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 6 and (i == 2 or i == 3 or i == 5 or i == 7):
                if current_list[_] + 1 == current_list[i]:
                    return 1
            if _ == 7 and (i == 4 or i == 5 or i == 7):
                if current_list[_] + 1 == current_list[i]:
                    return 1
    return 0

## Start from the initial set and get all possible solution
List = [1, 2, 3, 4, 5, 6, 7, 8]
ALL_List = list(permutations(List, r=None))
for i in range(len(ALL_List)):
    error = 0
    error += check_cell(ALL_List[i])
    # use the function to check for error
    # if no error then print the list as below:
    if error == 0:
        first_row = ALL_List[i][0]
        second_row = [ALL_List[i][1], ALL_List[i][2], ALL_List[i][3]]
        third_row = [ALL_List[i][4], ALL_List[i][5], ALL_List[i][6]]
        forth_row = ALL_List[i][7]
        print('  {}'.format(first_row))
        print('{} {} {}'.format(*second_row))
        print('{} {} {}'.format(*third_row))
        print('  {}\n'.format(forth_row))

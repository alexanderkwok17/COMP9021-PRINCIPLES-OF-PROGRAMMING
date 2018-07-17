# initial die position [right, back , top , front,left, bottom ]
# TO estimate the front top right of the die in each position
from copy import copy

# map the change if the die move right
def move_right(old_dice_swap, new_dice_swap):
    new_dice_swap[0] = old_dice_swap[2]
    new_dice_swap[1] = old_dice_swap[1]
    new_dice_swap[2] = old_dice_swap[4]
    new_dice_swap[3] = old_dice_swap[3]
    new_dice_swap[4] = old_dice_swap[5]
    new_dice_swap[5] = old_dice_swap[0]

# map the change if the die move Left
def move_left(old_dice_swap, new_dice_swap):
    new_dice_swap[0] = old_dice_swap[5]
    new_dice_swap[1] = old_dice_swap[1]
    new_dice_swap[2] = old_dice_swap[0]
    new_dice_swap[3] = old_dice_swap[3]
    new_dice_swap[4] = old_dice_swap[2]
    new_dice_swap[5] = old_dice_swap[4]

# map the change if the die move forward
def move_forward(old_dice_swap, new_dice_swap):
    new_dice_swap[0] = old_dice_swap[0]
    new_dice_swap[1] = old_dice_swap[5]
    new_dice_swap[2] = old_dice_swap[1]
    new_dice_swap[3] = old_dice_swap[2]
    new_dice_swap[4] = old_dice_swap[4]
    new_dice_swap[5] = old_dice_swap[3]

# map the change if the die move backward
def move_backward(old_dice_swap, new_dice_swap):
    new_dice_swap[0] = old_dice_swap[0]
    new_dice_swap[1] = old_dice_swap[2]
    new_dice_swap[2] = old_dice_swap[3]
    new_dice_swap[3] = old_dice_swap[5]
    new_dice_swap[4] = old_dice_swap[4]
    new_dice_swap[5] = old_dice_swap[1]
# let old die be position one
old_dice = [1, 5, 3, 2, 6, 4]
new_dice = [1, 5, 3, 2, 6, 4]
# new die will be used to store the new position
# only accept integer input
while True:
    try:
        steps = int(input('Enter the desired goal cell number: '))
        if steps <= 0:
            print('Incorrect value, try again')
            continue
        break
    except:
        print('Incorrect value, try again')
print('On cell {}'.format(steps), end='')

last_move = 0 # last move count cells location
last_direction = 'R' # This shows what is the direction it should move next ( the last given direction)
count_move_per_direction = 0 # count how many times it has be moved in the same direction
remain_direction = 0 # remaining number of time to move in the same direction
# using the pattern Right -> Forward -> Left -> Backward -> right ->....
# and the fact that the length of the path is 1,1,2,2,3,3,4,4,....
# Then the moving pattern is 1 RIGHT -> 1 Forward -> 2 Left -> 2 Backward -> etc....
for _ in range(1, steps, 1):
    if last_direction == 'R':
        # if the die moved Right last time,
        # it will either keep moving right or Switch direction
        if remain_direction == 0: # if there is no remaining move in the same direction switch to Forward
            move_right(old_dice, new_dice)   # perform the final move of right
            old_dice = copy(new_dice)        # change the face of the die
            # print('Moved Right. {}'.format(new_dice))
            last_move += 1                  # count the move
            last_direction = 'F'            # next move will be forward
            remain_direction = count_move_per_direction # Reset the remaining times to follow the same direction
            continue
        elif remain_direction > 0: # if there is still remaining direction keep moving right
            move_right(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved Right {}'.format(new_dice))
            last_move += 1
            last_direction = 'R' # keep moving Right
            remain_direction -= 1 # reduce the remaining times to follow the same direction
            continue
    if last_direction == 'F': # so if the next move is Forward, use the similar logic  as right perform the following
        if remain_direction == 0:
            move_forward(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved forward {}'.format(new_dice))
            last_move += 1
            last_direction = 'L' # Left is followed after Forward
            count_move_per_direction += 1
            remain_direction = count_move_per_direction
            continue
        elif remain_direction > 0:
            move_forward(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved foward {}'.format(new_dice))
            last_move += 1
            last_direction = 'F'
            remain_direction -= 1
            continue
    if last_direction == 'L': # if next move is Left, then apply the same logic move the die to left
        if remain_direction == 0:
            move_left(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved left {}'.format(new_dice))
            last_move += 1
            last_direction = 'B' # Backward is always follow after Left
            remain_direction = count_move_per_direction
            continue
        elif remain_direction > 0:
            move_left(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved left {}'.format(new_dice))
            last_move += 1
            last_direction = 'L'
            remain_direction -= 1
            continue
    if last_direction == 'B': # next move is backward
        if remain_direction == 0:
            move_backward(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved back {}'.format(new_dice))
            last_move += 1
            last_direction = 'R' # Right is always following Backward
            count_move_per_direction += 1
            remain_direction = count_move_per_direction
            continue
        elif remain_direction > 0:
            move_backward(old_dice, new_dice)
            old_dice = copy(new_dice)
            # print('Moved back {}'.format(new_dice))
            last_move += 1
            last_direction = 'B'
            remain_direction -= 1
            continue

Solution = [new_dice[2], new_dice[3], new_dice[0]]
print(', {} is at the top, {} at the front, and {} on the right.'.format(*Solution))

import random

def try_next_move():
    if random.random() < 0.25:
        print("Try to go right.")
    
    elif random.random() < 0.5:
        print("Try to go left.")
    
    elif random.random() < 0.75:
        print("Try to go down.")
    elif random.random() < 0.1:
        print("Try to go up.")

map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 24]
]
map3 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [24, 0, 0, 0],
]
map = map3

start_pos_x = 0
start_pos_y = 0

def move(step, current_pos_x,current_pos_y):
    print("Current step is: ", step)
    print("Current current_position_y = ", current_pos_y)
    print("Current current_position_x = ", current_pos_x)

    can_move_right = current_pos_x <= 2 and map[current_pos_y][current_pos_x+1] == 0
    can_move_down = current_pos_y <= 2 and map[current_pos_y+1][current_pos_x] == 0
    
    right_is_finish = current_pos_x <= 2 and map[current_pos_y][current_pos_x+1] == 24
    down_is_finish = current_pos_x <= 2 and map[current_pos_y+1][current_pos_x] == 24

    if right_is_finish:
        print("Found finish on right")
        return False
    if down_is_finish:
        print("Found finish below")
        return False
    if can_move_right:
        print("Should move right")
        return [current_pos_x + 1, current_pos_y]  
    if can_move_down:
        print("Should move down")
        return [current_pos_x, current_pos_y + 1]
    
current_move_number = 1
new_position = move(current_move_number, start_pos_x, start_pos_y)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1])

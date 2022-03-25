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

map = map2

start_pos_x = 0
start_pos_y = 0

def move(step, current_pos_x,current_pos_y):
    print("Current step is: ", step)
    print("Current current_position_y = ", current_pos_y)
    print("Current current_position_x = ", current_pos_x)
    can_move_right = current_pos_x <= 2 and map[current_pos_y][current_pos_x+1] == 0
    can_move_down =current_pos_y <= 2 and map[current_pos_y+1][current_pos_x] == 0
   
    if can_move_right:
        print("Should move right")
        current_pos_x = current_pos_x + 1
    if can_move_down:
        print("Should move down")
        current_pos_y = current_pos_y + 1

    return [current_pos_x, current_pos_y]

new_position = move(1, start_pos_x, start_pos_y)
new_position = move(2, new_position[0], new_position[1])
new_position = move(3, new_position[0], new_position[1])


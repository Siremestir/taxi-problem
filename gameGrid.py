import json

# TAXI deterministic MDP model:

# set of states S
# The grid is 5x5, and each position is doubled depending on whether or not the taxi has a passenger
# width = 5
# height = 5
# depth = 2

# P_ORIGIN = "s23"
# DESTINATION = "s25"

# walls = {
#     1 : "right",
#     6 : "right",
#     15 : "right",
#     17: "right",
#     20 : "right",
#     22 : "right"
# }

with open("config.json", 'r') as file:
    config = json.loads(file.read())

width = config["width"]
height = config["height"]
depth = 2

P_ORIGIN = "s" + str(config["passenger"]["origin"])
DESTINATION = "s" + str(config["passenger"]["destination"] + (width * height))

walls = config["walls"]

states= ["s"+str(i) for i in range(width*height*depth) ]
states.append("s%i" % (width*height*depth)) # final state

cube = []
i = 0
for plane in range(depth):
    grid = []
    for line in range(width):
        row = []
        for cell in range(height):
            row.append("s%i" % i)
            i += 1

        grid.append(row)

    cube.append(grid)

for grid in cube:
    for line in grid:
        print(line)
    print("------")
print(states[-1])

# set of actions
actions= ["right", "down", "left", "up", "pickup", "dropoff"]


#utils
def get_state_number(state:str) -> int:
    return int(state.removeprefix('s'))


def can_move(state:str, direction:str) -> bool:
    #TODO integrate walls
    state_nb = get_state_number(state)
    grid_number = state_nb % (width*height) #Relative to the grid
    if state == states[-1]:
        return False

    if str(grid_number) in walls and direction == walls[str(grid_number)]:
        return False

    if str(grid_number-1) in walls and walls[str(grid_number-1)] == "right" and direction == "left":
        return False
    
    if str(grid_number-5) in walls and walls[str(grid_number-5)] == "down" and direction == "up":
        return False

    if direction == "up":
        return grid_number >= width
    
    if direction == "down":
        return grid_number < (width * (height -1))
    
    row_number = state_nb % width #Relative to the row

    if direction == "right":
        return row_number < width - 1
    
    if direction == "left":
        return row_number > 0


# transition function T
def transitions(state, action):
    # Calculate next state (according to simple grid with wall)
    # Default: remain in a state if action tries to leave grid
    next_state = state
    state_nb = get_state_number(state)

    if state_nb < height*width and action == "pickup" and state == P_ORIGIN:
        next_state = "s%i" % (state_nb + height*width)

    elif action == "dropoff" and state == DESTINATION:
        next_state = states[-1]

    elif action == "right" and can_move(state, action):
        next_state = "s%i" % (state_nb + 1)

    elif action == "left" and can_move(state, action):
        next_state = "s%i" % (state_nb - 1)

    elif action == "down" and can_move(state, action):
        next_state = "s%i" % (state_nb + width)

    elif action == "up" and can_move(state, action):
        next_state = "s%i" % (state_nb - width)


    return {next_state : 1.0}


# Reward function R
def rewards(state, action):
    # Calculate reward
    if (state == DESTINATION and action == "dropoff"):
        return 20
    elif (state != P_ORIGIN and action == "pickup") or action == "dropoff":
        return -10
    else:
        return -1


# final state 
def isEnd(state):
    return (state == states[-1])


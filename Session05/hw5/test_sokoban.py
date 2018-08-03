map ={
    'size_x': 6,
    'size_y': 6
}

player ={'y': 1,'x':1}

boxes = [
    {'y': 2,'x':0},
    {'y': 2,'x':1},
    {'y': 2,'x':2},
    {'y': 2,'x':3}
]

destinations = [
    {'y': 3, 'x':0},
    {'y': 4, 'x':1},
    {'y': 5, 'x':0},
    {'y': 5, 'x':3}
]

obstacle_course =[
    {'y':3,'x':1},
    {'y':5,'x':4}
]

playing = True

while playing:
    #map
    for y in range(map['size_y']):
        for x in range(map['size_x']):

            dest_is_here = False
            for dest in destinations:
                if y == dest['y'] and x == dest['x']:
                    dest_is_here = True

            play_is_here = False
            if y == player['y'] and x == player['x']:
                play_is_here = True

            box_is_here = False
            for box in boxes:
                if y == box['y'] and x == box['x']:
                    box_is_here = True
            
            obs_is_here = False
            for obs in obstacle_course:
                if y == obs['y'] and x == obs['x']:
                    obs_is_here = True
            
            if play_is_here:
                print("P ",end="")
            elif box_is_here:
                print("B ",end="")
            elif dest_is_here:
                print("D ",end="")
            elif obs_is_here:
                print("O ",end="")
            else:
                print("- ",end="")
        print()
    #endmap

    #check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win:
        print("You win!")
        break
    ####

    move = input("Your move: ").upper()

    dx = 0 
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    # elif move =="Z":
    #     
    else:
        playing = False

    if 0 <= player['x'] + dx <= map['size_x'] - 1 and 0 <= player['y'] + dy <= map['size_y']-1:
        for obs in obstacle_course:
            if player['x'] + dx == obs['x'] and player['y'] + dy == obs['y']:
                #
            else:
                player['x'] += dx
                player['y'] += dy

    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player ['y']:
            box['x'] += dx
            box['y'] += dy
    
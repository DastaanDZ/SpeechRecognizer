from PIL import Image
import random

end = 100
def show_board():
    img = Image.open('board.png')
    img.show()

def check_ladder(points):
    if points == 8:
        print("Ladder")
        return 26
    elif points == 21:
        print("Ladder")
        return 82
    elif points == 43:
        print("Ladder")
        return 77
    elif points == 50:
        print("Ladder")
        return 91
    elif points == 54:
        print("Ladder")
        return 93
    elif points == 62:
        print("Ladder")
        return 96
    elif points == 66:
        print("Ladder")
        return 87
    elif points == 80:
        print("Ladder")
        return 100
    else:
        return points
    
def check_snake(points):
    if points == 44:
        print("Snake")
        return 22
    elif points == 46:
        print("Snake")
        return 5
    elif points == 48:
        print("Snake")
        return 9
    elif points == 52:
        print("Snake")
        return 11
    elif points == 55:
        print("Snake")
        return 7
    elif points == 59:
        print("Snake")
        return 17
    elif points == 64:
        print("Snake")
        return 36
    elif points == 69:
        print("Snake")
        return 33
    elif points == 73:
        print("Snake")
        return 1
    elif points == 83:
        print("Snake")
        return 19
    elif points == 92:
        print("Snake")
        return 51
    elif points == 95:
        print("Snake")
        return 24
    elif points == 98:
        print("Snake")
        return 28
    else:
        return points
    
def reached_end(points):
    if points == end:
        return True
    else:
        return False
    
def play():
    p1_name = input("Enter player 1 name: ")
    p2_name = input("Enter player 2 name: ")
    p1_pos = 0
    p2_pos = 0

    turn = 0

    while True:
        if turn%2 == 0:
            print(p1_name, "turn")
            c = input("Press 1 to continue, 0 to quit: ")
            if c == '0':
                print(p1_name, "scored", p1_pos)
                print(p2_name, "scored", p2_pos)
                break
            dice = random.randint(1,6)
            print("Dice showed", dice)
            p1_pos += dice
            p1_pos = check_ladder(p1_pos)
            p1_pos = check_snake(p1_pos)

            if p1_pos>end:
                p1_pos = end
            print(p1_name, "scored", p1_pos)

            if reached_end(p1_pos):
                print(p1_name, "won")
                break
        else:
            print(p2_name, "turn")
            c = input("Press 1 to continue, 0 to quit: ")
            if c == '0':
                print(p1_name, "scored", p1_pos)
                print(p2_name, "scored", p2_pos)
                break
            dice = random.randint(1,6)
            print("Dice showed", dice)
            p2_pos += dice
            p2_pos = check_ladder(p2_pos)
            p2_pos = check_snake(p2_pos)

            if p2_pos>end:
                p2_pos = end
            print(p2_name, "scored", p2_pos)

            if reached_end(p2_pos):
                print(p2_name, "won")
                break



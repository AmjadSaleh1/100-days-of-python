print("Welcome to Treasure Island\nYour mission is to find the treasure.")
path = input('youre at a cross road, where you want to go ? type "left" or "right" \n').lower()

if path == "right":
    print("Fall into a hole.Game Over.")
    exit()
else:
    print("you've come to a lake , this is island in the middle of the lake ")
    path2 = input('type "wait" to wait for a boar or "swim" to swim a cross \n').lower()
    if path2 == "swim":
        print("Game over.")
        exit()
    else:
        path3 = input('you have three doors pick color of each door "red or "blue "yellow" ').lower()
        if path3 == "red" or path3 == "blue":
            print("game over")
            exit()
        elif path3 == "yellow":
            print("you win!")
        else:
            print("door doesnt exist")

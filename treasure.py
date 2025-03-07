print(r'''         _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
name = input("Enter your name to continue the game: ")
print(f"Hello {name},Your mission is to find the treasure.")
choose = input("Type continue or end: ").lower()

# choosing option to continue or end
if choose == "continue":

    # choose direction
    direction = input(r"You're at a turning point in life. choose 'left' or 'right': ").lower()
    if direction == "left":
        # choose action
        action = input(r"choose 'swim' or 'wait' for boat to reach the Island... ").lower()
        if action == "wait":
            # game Continues
            door = input("You reached to Island,Which door do you want to open to win treasure? choose door: red, blue, yellow: ").lower()
            if door == "red":
                print("Burned by fire! Game Over!")
            elif door == "blue":
                print("Eaten by beasts! Game Over!")
            elif door == "yellow":
                print(f"Hey {name}, Congratulations! You win the game!")
            else:
                print("You entered the wrong door, Game Over!")
        # game end
        elif action == "swim":
            print("attacked by trout, Game Over!")
        # wrong action - game over
        else:
            print("Wrong option, Game Over.")
    elif direction == "right":
        print("Fall into a hole, Game over.")
    else:
        print("Wrong Direction, Game Over.")
#end
else:
    print("You end the Game!!")
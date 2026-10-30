life = 3
leftcounter = 0
import random
num = random.randint(1, 5)
print("Life Counter:", life)
if leftcounter == num:
    print("You found the treasure. YOU WIN!")
    print("Life Counter:", life)
while life > 0:
    choice = input(str("left or right"))
    if choice == "left":
        print("You have entered the cave! You are safe")
        leftcounter = leftcounter + 1
        print("Life Counter:", life)
    if choice == "right":
        life = life - 1
        print ("Haha loser")
        print("Life Counter:", life)
    if leftcounter == num:
        print("You found the treasure. YOU WIN!")
        print("Life Counter:", life)
        break
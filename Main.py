print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Find The Treasure!")
print("Your mission is to find the treasure.")

input1 = input("To your left you see a river and to your right you see a forest.\nWhich way would you like to go?  Type 'left' or 'right'\n\n")

if input1 == "left":
  input2 = input("\nYou make it to the river.\nWill you try to swim across or will you wait for a boat? Type 'wait' or 'swim'\n\n")
  if input2 == "swim":
    input3 = input("\nWell that was pretty easy since the rivver was so shallow.\nYou come across three houses colored red, yellow, and blue.\nWhich house should you go in?  Type 'red', 'yellow', or 'blue'\n\n")
    if input3 == "yellow":
      print("\nYou did it!  You found the treasure!")
    elif input3 == "blue":
      print("\nYou enter the blue house and drown for some reason. Game Over.")
    elif input3 == "red":
      print("\nWow this house is spectacular!\nYou decide to settle down and never find the treasure. Game Over.")
    else:
      print("\nYou can't do that, but you did anyway. Game Over.")
  elif input2 == "wait":
    print("\nYou die of boredom. Game Over.")
  else:
    print("\nYou can't do that, but you did anyway. Game Over.")
elif input1 == "right":
  print("\nThis forest is kind of creeping you out. You call the adventure off. Game Over.")
else:
  print("\nYou can't do that, but you did anyway. Game Over.")
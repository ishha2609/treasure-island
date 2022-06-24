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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Tresure Island")
print("Your Mission is  to find  the Tresure")
choice1 = input('you \'re at a crossroad, where do you want to go? Type "left" or "right".').lower() 
 if choice1 == "left":
    choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake.Type "wait" to wait for a boat.type "swim" for swim across.').lower()
    if choice2 == "wait":
       choice3 = input("you arrive at the island unharmed. there is a house with 3 doors.one red,one yellow and one blue. which colour do you choose?").lower()
       if choice3 == "red":
         print("Its's a room full of fire. Game over.")
       elif choice == "yellow":
         print("You found the teasure! You Win!")
       elif choice == "blue":
         print("You enter a room of beasts. Game over.")
       else:
         print("You choose a door that doesn't exist . Game over.")
    else:
      print("You got attacked by an angry trout,Game over")
else:
     print(" You fell into a hole.Game over")


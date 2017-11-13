# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure

def day():
    global days
    print("\nDay", days)
    print("=====")

def score(playerScore):
    print("\nYour score is: ", playerScore)

def start(title, intro, gameLocations, playerScore, placeVisit):
    print(title)
    print("======\n")
    print(intro)
    print(gameLocations[0])
    placeVisit[0] = True



def end():
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")

#end() Testing new end function

gameMap = "    Bed\n    |\n    Room -- Living Room -- Kitchen"

def goto(matrix, currentLocation, playerLocation, direction):

    if currentLocation == 0:
        newLocation = matrix[currentLocation][direction]
    
    elif currentLocation == 1:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 2:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 3:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 4:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 5:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 6:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 7:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 8:
        newLocation = matrix[currentLocation][direction]

    elif currentLocation == 9:
        newLocation = matrix[currentLocation][direction]
    print(newLocation)
    return newLocation

    #elif currentLocation == "Bedroom" and days == 0:
     #   playerLocation = "Bedroom"
      #  if placeVisit[1] == False:
       #     placeVisit[1] = True
        #    print(gameLocations[1])
         #   playerScore = playerScore + 5
          #  score()
        #elif placeVisit[1] == True:
         #   print("\nThe bed is so close...")
    #elif currentLocation == "Bedroom" and days == 1:
#        playerLocation = "Bedroom"
 #       if placeVisit[8] == False:
  #          placeVisit[8] = True
   #         print(gameLocations[8])
   #         playerScore = playerScore + 5
    #        score()    

#    elif location == "Bed" and days == 0:
 #       if placeVisit[2] == False:
  #          playerLocation = "Bed"
   #         placeVisit[2] = True
    #        print(gameLocations[2])
     #       playerScore = playerScore + 5
      #      score()
       # elif placeVisit[2] == True:
        #    playerLocation = "Bed"
         #   print("\nEnter 'Sleep' to sleep.")
#    elif location == "Bed" and days == 1:
 #       if placeVisit[7] == False:
  #          playerLocation = "Bed"
   #         print(gameLocations[7])
    #        placeVisit[7] = True
     #       playerScore = playerScore + 5
      #      score()
       # elif placeVisit[7] == True:
        #    print("\nYou should really get going if you want to get to work on time.")
    #
    #elif location == "Living Room?" and days == 0:
     #   if placeVisit[4] == False and placeVisit[3] == False:
      #      print(gameLocations[3])
       #     placeVisit[3] = True
        #    print(gameLocations[4])
         #   placeVisit[4] = True
          #  playerScore = playerScore + 10
           # score()
#        if placeVisit[4] == True:
 #           playerLocation = "Living Room?"
  #          print("\nIt is unusually cold in the house.")
#
 #   elif location == "Bedroom?" and days == 0:
  #      playerLocation = "Bedroom?"
   #     if placeVisit[5] == False:
    #        placeVisit[5] = True
     #       print(gameLocations[5])
      #      print("\nYou need to wake up. Type 'Wake up' at any time to wake up.")
       #     playerScore = playerScore + 5
        #    score()
#        elif placeVisit[5] == True:
 #           print("\nThe note is still laying on the bed. You take in the handwriting of your name, " + name + ", once again. It's just the same as that night...")
        
def game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation):
    while True:
    
        command = input("\nEnter a command: ").lower()

        if command == "help":
            print(commands)

        elif command == "quit":
            break

        elif command == "points":
            score(playerScore)

        elif command == "map":
            print(gameMap)

        elif command == "location":
            print("\nLocation:", playerLocation)

        elif command == "search":
            pass

        elif command == "take":
            pass

        elif command == "look":
            pass

        elif command == "north":
            direction = 0
            place = goto(matrix, currentLocation, playerLocation, direction)
            if placeVisit[place] == False:
                print(gameLocations[place])
                placeVisit[place] = True
                playerScore = playerScore + 5
                score(playerScore)
            else:
                print(gameShortLoc[place])
            currentLocation = place
    
        elif command == "south":
            direction = 1
            place = goto(matrix, currentLocation, playerLocation, direction)
            if placeVisit[place] == False:
                print(gameLocations[place])
                placeVisit[place] = True
                playerScore = playerScore + 5
                score(playerScore)
            else:
                print(gameShortLoc[place])
            currentLocation = place

        elif command == "east":
            direction = 2
            place = goto(matrix, currentLocation, playerLocation, direction)
            if placeVisit[place] == False:
                print(gameLocations[place])
                placeVisit[place] = True
                playerScore = playerScore + 5
                score(playerScore)
            else:
                print(gameShortLoc[place])
            currentLocation = place
            
        elif command == "west":
            direction = 3
            place = goto(matrix, currentLocation, playerLocation, direction)
            if placeVisit[place] == False:
                print(gameLocations[place])
                placeVisit[place] = True
                playerScore = playerScore + 5
                score(playerScore)
            else:
                print(gameShortLoc[place])
            currentLocation = place

        elif command == "sleep":
            if playerLocation == "Bed" and days == 0:
                goto("Living Room?")
            else:
                print("\nYou can't possibly expect to sleep here...")

        elif command == "wake up":
            if playerLocation == "Living Room?" or "Bedroom?" and days == 0:
                days = days + 1
                day()
                goto("Bed")

            else:
                print("\nYou're not asleep, are you?")

        else:
            print("\nThat is not a valid command")

            
            
            
                
  
            
def main():
    intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter."
    title = "\nAsleep"
    commands = "\nValid commands: North, South, East, West, Help, Map, Points, Location, Quit"
    wrongWay = "\nYou can't go that way!"
    playerLocation = "Living Room"
    currentLocation = 0
    days = 0
    playerScore = 0
    direction = "some way"
    name = str(input("What is your name? "))
    
    livingRoom0 = 0
    kitchen0 = 1
    bedRoom0 = 2
    bathroom0 = 3
    bed0 = 4
    livingRoomDream0 = 5
    bedRoomDream0 = 6
    bed1 = 7
    bedRoom1 = 8
    bathroom1 = 9
    
    placeVisit = [False,
                  False,
                  False,
                  False,
                  False,
                  False,
                  False,
                  False,
                  False,
                  False]
    
    items = ["Map",
             "Knife",
             None,
             None,
             None,
             None,
             None,
             None,
             "Medicine",
             None]
    
    placeSearched = [False,
                     False,
                     False,
                     False,
                     False,
                     False,
                     False,
                     False,
                     False,
                     False]
    sleeping = "\nYou drift to sleep, and find yourself arriving home after a long and difficult day of work, like all the others..."
                   
    gameLocations = [ ("\nYou drop your keys and jacket on the table, exhausted "
                       "after a long and difficult day of work, like all the others. "
                       "Your room is just down the hall to the West, waiting for you."),
                      ("\nYou go into the kitchen, even though you aren't hungry. A "
                       "letter with " + name + " on it is held on the fridge by a magnet, you "
                       "don't really want to think about it..."),
                      ("\nYour bedroom, with your bed in the center of the back "
                       "wall, to the North. You take your medicine and prepare for "
                       "bed. You'll have to remember to take it every morning and night"),
                      ("\nYou use the bathroom, even though you didnt really have to, "
                       "and prepare to go to sleep"), 
                      ("\nYour bed, not as comfortable as it used to be... Still, "
                       "you are weary enough to sleep. Enter 'Sleep' to sleep."),
                      ("\nYou drift to sleep, and find yourself arriving home "
                       "after a long and difficult day of work, like all the others... "
                       "You drop your keys and winter jacket on the table, "
                       "exhausted. It takes you a minute to realize what you're "
                       "doing, you should be asleep, right? A faint glow is coming "
                       "from your bedroom down the hall."),
                      ("\nYou push open the door, and find the TV still on. A note "
                       "lies on the bed, with the name " + name + " written on the "
                       "top in HER handwriting."),
                      ("\nYou wake in a cold sweat. Your dream had been so real, "
                       "it felt as if you had really been there reliving that same "
                       "night. You don't feel so well, but still, you decide to get "
                       "out of bed and go to work."),
                      ("\nYou change into your work clothes and take your medicine "
                       "for the morning, but you still need to shower and brush your "
                       "teeth in the bathroom to the West."),
                      ("\nYou enter the bathroom and take your shower, but still, "
                       "the cold feeling from that dream stays with you")]

    gameShortLoc = [ ("\nYou're back in the living room, struggling to keep your eyes open."),
                     ("\nYou're really TIRED, not HUNGRY."),
                     ("\nThe bed is so close..."),
                     ("\nYou don't need to use the bathroom again"),
                     ("\nEnter 'Sleep' to sleep."),
                     ("\nIt is unusually cold in the house..."),
                     ("\nThe note is still laying on the bed. You take in the handwriting of your "
                      "name, " + name + ", once again. It's just the same as that night..."),
                     ("\nYou should really get going if you want to get to work on time."),
                     ("\nDid you remember to take your medicine?"),
                     ("\nYou give yourself a once-over in the mirror. You look like a mess today")]
                     
        #      N     S     E     W
    matrix = [[None, None, 1, 2],
              [None, None, None, 0],
              [4, None, 0, 3],
              [None, None, 2, None],
              [None, 2, None, None],
              [None, None, None, 6],
              [None, None, 5, None],
              [None, 8, None, None],
              [7, None, None, 9],
              [None, None, 8, None]]

    inventory = [ "Ring" ]
    start(title, intro, gameLocations, playerScore, placeVisit)
    game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation)
    end()

main()









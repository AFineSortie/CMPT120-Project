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

gameMap = "                Bed\n                 |\n    Bathroom -- Room -- Living Room -- Kitchen"

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

        
def game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation, inventory):
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
            if placeSearched[currentLocation] == False:
                placeSearched[currentLocation] = True
                print("\nYou find", items[currentLocation])
            else:
                print("\nYou've already searched here.")

        elif command == "take":
            if placeSearched[currentLocation] == True:
                if items[currentLocation] != "Nothing":
                    inventory.append(items[currentLocation])
                    print("\nYou take the item.")
                else:
                    print("\nThere is nothing to take!")
            else:
                print("\nYou have not searched here!")
                
        elif command == "inventory":
            print(inventory)

        elif command == "look":
            print(gameLocations[currentLocation])

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
            if currentLocation == 4:
                currentLocation = 5
                place = 5
                if placeVisit[place] == False:
                    print(gameLocations[place])
                    placeVisit[place] = True
                    playerScore = playerScore + 5
                    score(playerScore)
                else:
                    print(gameShortLoc[place])
            else:
                print("\nYou can't possibly expect to sleep here...")

        elif command == "wake up":
            if currentLocation == 5 or currentLocation == 6:
                currentLocation = 7
                place = 7
                if placeVisit[place] == False:
                    print(gameLocations[place])
                    placeVisit[place] = True
                    playerScore = playerScore + 5
                    score(playerScore)
                else:
                    print(gameShortLoc[place])

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
    
    items = ["a map.",
             "a knife.",
             "nothing.",
             "nothing.",
             "nothing.",
             "nothing.",
             "nothing.",
             "nothing.",
             "your medicine.",
             "nothing."]
    
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
                       "and prepare to go to sleep."), 
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
                       "top in HER handwriting. Enter 'wake up' to wake."),
                      ("\nYou wake in a cold sweat. Your dream had been so real, "
                       "it felt as if you had really been there reliving that same "
                       "night. You don't feel so well, but still, you decide to get "
                       "out of bed and go to work."),
                      ("\nYou change into your work clothes and take your medicine "
                       "for the morning, but you still need to shower and brush your "
                       "teeth in the bathroom to the West."),
                      ("\nYou enter the bathroom and take your shower, but still, "
                       "the cold feeling from that dream stays with you.")]

    gameShortLoc = [ ("\nYou're back in the living room, struggling to keep your eyes open."),
                     ("\nYou're really TIRED, not HUNGRY."),
                     ("\nThe bed is so close..."),
                     ("\nYou don't need to use the bathroom again."),
                     ("\nEnter 'Sleep' to sleep."),
                     ("\nIt is unusually cold in the house..."),
                     ("\nThe note is still laying on the bed. You take in the handwriting of your "
                      "name, " + name + ", once again. It's just the same as that night..."),
                     ("\nYou should really get going if you want to get to work on time."),
                     ("\nDid you remember to take your medicine?"),
                     ("\nYou give yourself a once-over in the mirror. You look like a mess today.")]
                     
        #      N     S     E     W
    matrix = [[0, 0, 1, 2],
              [1, 1, 1, 0],
              [4, 2, 0, 3],
              [3, 3, 2, 3],
              [4, 2, 4, 4],
              [5, 5, 5, 6],
              [6, 6, 5, 6],
              [7, 8, 7, 7],
              [7, 8, 8, 9],
              [9, 9, 8, 9]]

    inventory = [ "Ring" ]
    start(title, intro, gameLocations, playerScore, placeVisit)
    game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation, inventory)
    end()

main()









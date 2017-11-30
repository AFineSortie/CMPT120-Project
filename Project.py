# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure

from Locale.py import *

def day():
    global days
    print("\nDay", days)
    print("=====")

def score(playerScore):
    print("\nYour score is: ", playerScore)

def start(title, intro, gameLoc):
    print(title)
    print("======\n")
    print(intro)
    gameLoc[0].printLong()
    gameLoc[0].searchLoc()



def end(playerScore):
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
    return newLocation

        
def game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation, inventory):
    while True:
        if "your medicine." in inventory:
            return playerScore
        
        command = input("\nEnter a command: ").lower()

        if command == "help":
            print("\nValid commands: North, South, East, West, Help, Search, Take, Drop, Look, Map, Points, Location, Quit")

        elif command == "quit":
            break

        elif command == "points":
            score(playerScore)

        elif command == "map":
            if "a map." in inventory:
                print(gameMap)
            else:
                print("\nYou have no map!")

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
                if items[currentLocation] != "nothing.":
                    inventory.append(items[currentLocation])
                    print("\nYou take the item.")
                    items[currentLocation] = "nothing."
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
            if "a knife." in inventory:
                print("\nYou shouldn't have taken a knife to bed with you! You accidentally cut yourself and have to go to the hospital.")
                return playerScore
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
    wrongWay = "\nYou can't go that way!"
    playerLocation = "Living Room"
    currentLocation = 0
    days = 0
    direction = "some way"
    name = str(input("What is your name? "))
    gameLoc = []

    class Player:
        def __init__(self, name, score, currLoc, moveCount, inventory):
            self.name = name
            self.score = score
            self.currLoc = currLoc
            self.moveCount = moveCount
            self.inventory = inventory

        def addScore(self):
            self.score = self.score + 5


    player = Player(name, 0, "Living Room", 0, "Nothing")

    class Locale:
        def __init__(self, name, longDes, shortDes, wasVisited, wasSearched, items):
            self.name = name
            self.longDes = longDes
            self.shortDes = shortDes
            self.wasVisited = wasVisited
            self.wasSearched = wasSearched
            self.items = items

        def printLong(self):
            print(self.longDes)

        def printShort(self):
            print(self.shortDes)

        def visitLoc(self):
            self.wasVisited = True

        def searchLoc(self):
            self.wasSearched = True

    livingRoom0 = Locale("Living Room",
                         ("\nYou drop your keys and jacket on the table, exhausted "
                         "after a long and difficult day of work, like all the others. "
                         "Your room is just down the hall to the West, waiting for you."),
                         ("\nYou're back in the living room, struggling to keep your eyes open."),
                         False,
                         False,
                         "a map.")

    kitchen0 = Locale("Kitchen",
                     ("\nYou go into the kitchen, even though you aren't hungry. A "
                      "letter with " + name + " on it is held on the fridge by a magnet, you "
                      "don't really want to think about it..."),
                     ("\nYou're really TIRED, not HUNGRY."),
                      False,
                      False,
                      "a knife.")

    bedroom0 = Locale("Bedroom",
                     ("\nYour bedroom, with your bed in the center of the back "
                      "wall, to the North. You take your medicine and prepare for "
                      "bed. You'll have to remember to take it every morning and night"),
                     ("\nThe bed is so close..."),
                      False,
                      False,
                      "nothing.")

    bathroom0 = Locale("Bathroom",
                      ("\nYou use the bathroom, even though you didnt really have to, "
                       "and prepare to go to sleep."),
                      ("\nYou don't need to use the bathroom again."),
                       False,
                       False,
                       "nothing.")

    bed0 = Locale("Bed",
                 ("\nYour bed, not as comfortable as it used to be... Still, "
                  "you are weary enough to sleep. Enter 'Sleep' to sleep."),
                 ("\nEnter 'Sleep' to sleep."),
                  False,
                  False,
                  "nothing.")

    livingRoomDream0 = Locale("Living Room?",
                             ("\nYou drift to sleep, and find yourself arriving home "
                              "after a long and difficult day of work, like all the others... "
                              "You drop your keys and winter jacket on the table, "
                              "exhausted. It takes you a minute to realize what you're "
                              "doing, you should be asleep, right? A faint glow is coming "
                              "from your bedroom down the hall. You feel compelled to go to it"),
                             ("\nIt is unusually cold in the house... The pull from the Bedroom is still there."),
                              False,
                              False,
                              "a key.")

    bedroomDream0 = Locale("Bedroom?",
                          ("\nYou push open the door, and find the TV still on. A note "
                           "lies on the bed, with the name " + name + " written on the "
                           "top in HER handwriting. Enter 'wake up' to wake."),
                          ("\nThe note is still laying on the bed. You take in the handwriting of your "
                           "name, " + name + ", once again. It's just the same as that night..."),
                           False,
                           False,
                           "nothing.")

    bed1 = Locale("Bed",
                 ("\nYou wake in a cold sweat. Your dream had been so real, "
                  "it felt as if you had really been there reliving that same "
                  "night. You don't feel so well, but still, you decide to get "
                  "out of bed and go to work."),
                 ("\nYou should really get going if you want to get to work on time."),
                  False,
                  False,
                  "nothing.")

    bedroom1 = Locale("Bedroom",
                     ("\nYou change into your work clothes, but you still need to shower and brush your "
                      "teeth in the bathroom to the West."),
                     ("\nYou feel like you might be forgetting something.."),
                      False,
                      False,
                      "your medicine.")

    bathroom1 = Locale("Bathroom",
                      ("\nYou enter the bathroom and take your shower, but still, "
                       "the cold feeling from that dream stays with you."),
                       ("\nI knew you wouldn't forget to brush your teeth."),
                       False,
                       False,
                       "nothing.")

    livingRoom1 = Locale("Living Room",
                        ("/nYou grab your jacket and keys, somewhat ready to head ",
                         "out for the day. Go 'south' to exit your home and go to work"),
                         "\nIt is time to leave for work, unfortunately.",
                         False,
                         False,
                         "a gold necklace.")

    kitchen1 = Locale("Kitchen",
                      "\nMaybe you should grab some breakfast, even if you'll be late.",
                      "\nYou realize that the letter is gone...",
                      False,
                      False,
                      "a delicious bowl of cereal.")
                       
    gameLoc.append(livingRoom0)
    gameLoc.append(kitchen0)
    gameLoc.append(bedroom0)
    gameLoc.append(bathroom0)
    gameLoc.append(bed0)
    gameLoc.append(livingRoomDream0)
    gameLoc.append(bedroomDream0)
    gameLoc.append(bed1)
    gameLoc.append(bedroom1)
    gameLoc.append(bathroom1)
    gameLoc.append(livingRoom1)
    gameLoc.append(kitchen1)
# livingRoom0 = 0
# kitchen0 = 1
# bedRoom0 = 2
# bathroom0 = 3
# bed0 = 4
# livingRoomDream0 = 5
# bedRoomDream0 = 6
# bed1 = 7
# bedRoom1 = 8
# bathroom1 = 9
# livingRoom1 = 10
# kitchen1 = 11
    
                     
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
    
    start(title, intro, gameLoc)
    end(game(matrix, gameLocations, gameShortLoc, playerScore, placeVisit, items, placeSearched, playerLocation, currentLocation, inventory))
    

main()









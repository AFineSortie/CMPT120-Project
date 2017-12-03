# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure

from Locale import *
from Player import *



def score(player):
    print("\nYour score is: ", player.score)

def start(title, intro, gameLoc, player):
    print(title)
    print("======\n")
    print(intro)
    gameLoc[0].printLong()
    gameLoc[0].visitLoc()
    player.addScore()



def end(playerScore):
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")

#end() Testing new end function

gameMap = "                Bed\n                 |\n    Bathroom -- Room -- Living Room -- Kitchen"

def goto(matrix, gameLoc, player, direction):

    newLocation = matrix[player.numLoc][direction]

    if player.numLoc == newLocation:
        print("\nYou can not go that way!")

    if newLocation == 0:
        player.nameLoc = "Living Room"
    elif newLocation == 1:
        player.nameLoc = "Kitchen"
    elif newLocation == 2:
        player.nameLoc = "Bedroom"
    elif newLocation == 3:
        player.nameLoc = "Bathroom"
    elif newLocation == 4:
        player.nameLoc = "Bed"
    elif newLocation == 5:
        player.nameLoc = "Living Room?"
    elif newLocation == 6:
        player.nameLoc = "Bedroom?"
    elif newLocation == 7:
        player.nameLoc = "Bed"
    elif newLocation == 8:
        player.nameLoc = "Bedroom"
    elif newLocation == 9:
        player.nameLoc = "Bathroom"
    elif newLocation == 10:
        player.nameLoc = "Living Room"
    elif newLocation == 11:
        player.nameLoc = "Kitchen"
    
    player.numLoc = newLocation
    return newLocation

        
def game(matrix, gameLoc, player):
    while True:
        if "your medicine" in player.inventory:
            return player.score
        
        command = input("\nEnter a command: ").lower()

        if command == "help":
            print("\nValid commands: North, South, East, West, Help, Search, Take, Drop, Look, Map, Points, Location, Quit")

        elif command == "quit":
            break

        elif command == "points":
            print("\nYou have", player.score, "points")

        elif command == "map":
            if "map" in player.inventory:
                print(gameMap)
            else:
                print("\nYou have no map!")

        elif command == "location":
            print("\nLocation:", player.nameLoc)

        elif command == "search":
            if gameLoc[player.numLoc].wasSearched == False:
                gameLoc[player.numLoc].searchLoc()
                print("\nYou find a/an", gameLoc[player.numLoc].items)
            else:
                print("\nThere is a/an", gameLoc[player.numLoc].items, "here.")

        elif command == "take":
            if gameLoc[player.numLoc].wasSearched == True:
                takeItem = str(input("\nWhat do you want to take: "))
                if takeItem.lower() == str(gameLoc[player.numLoc].items) and gameLoc[player.numLoc].items != "nothing":
                    player.inventory.append(gameLoc[player.numLoc].items)
                    print("\nYou take the item.")
                    gameLoc[player.numLoc].remItem()
                else:
                    print("\nThere is nothing like that to take!")
            else:
                print("\nYou have not searched here!")

        elif command == "drop":
            dropItem = str(input("\nWhat do you want to drop: ")).lower()
            if dropItem in player.inventory and gameLoc[player.numLoc].items == "nothing":
                player.dropItem(dropItem)
                gameLoc[player.numLoc].items = dropItem
                print("\nYou drop the", dropItem + ".")
            else:
                print("\nYou can't drop that!")

        elif command == "use":
            useItem = str(input("\nWhat do you want to use: ")).lower()
            if useItem in player.inventory:
                if useItem == "knife":
                    onWhat = str(input("\nWhat do you want to use the knife on: ")).lower()
                    if onWhat == "self" or onWhat == "myself" or onWhat == player.name:
                        print("\nWhy would you go and do that! Now you have to go to the hospital!")
                        return player.score
                    else:
                        print("\nYou cant use the knife on that.")
                elif useItem == "key":
                    if player.numLoc == 10:
                        print("\nYou head off to work once more.")
                        return player.score
                    else:
                        print("\nWhy would you use the front door key here?")
                elif useItem == "bowl of cereal":
                    print("\nMmm delicious cereal.")
                    player.remItem("bowl of cereal")
                else:
                    print("\nYou can't use that now")
            else:
                print("\nYou don't have anything like that.")
                
                
        elif command == "inventory":
            print(player.inventory)

        elif command == "look":
            print(gameLoc[player.numLoc].longDes)

        elif command == "north":
            direction = 0
            place = goto(matrix, gameLoc, player, direction)
            if gameLoc[player.numLoc].wasVisited == False:
                gameLoc[player.numLoc].printLong()
                gameLoc[player.numLoc].visitLoc()
                player.addScore()
                score(player)
            else:
                gameLoc[player.numLoc].printShort()
            currentLocation = place
    
        elif command == "south":
            direction = 1
            place = goto(matrix, gameLoc, player, direction)
            if gameLoc[player.numLoc].wasVisited == False:
                gameLoc[player.numLoc].printLong()
                gameLoc[player.numLoc].visitLoc()
                player.addScore()
                score(player)
            else:
                gameLoc[player.numLoc].printShort()
            currentLocation = place

        elif command == "east":
            direction = 2
            place = goto(matrix, gameLoc, player, direction)
            if gameLoc[player.numLoc].wasVisited == False:
                gameLoc[player.numLoc].printLong()
                gameLoc[player.numLoc].visitLoc()
                player.addScore()
                score(player)
            else:
                gameLoc[player.numLoc].printShort()
            currentLocation = place
            
        elif command == "west":
            direction = 3
            place = goto(matrix, gameLoc, player, direction)
            if gameLoc[player.numLoc].wasVisited == False:
                gameLoc[player.numLoc].printLong()
                gameLoc[player.numLoc].visitLoc()
                player.addScore()
                score(player)
            else:
                gameLoc[player.numLoc].printShort()
            currentLocation = place

        elif command == "sleep":
            if "knife" in player.inventory:
                print("\nYou shouldn't have taken a knife to bed with you! You accidentally cut yourself and have to go to the hospital.")
                return player.score
            if player.numLoc == 4:
                player.numLoc = 5
                place = 5
                if gameLoc[player.numLoc].wasVisited == False:
                    gameLoc[player.numLoc].printLong()
                    gameLoc[player.numLoc].visitLoc()
                    player.addScore()
                    score(player)
                else:
                    gameLoc[player.numLoc].printShort()
            else:
                print("\nYou can't possibly expect to sleep here...")

        elif command == "wake up":
            if player.numLoc == 5 or player.numLoc == 6:
                player.numLoc = 7
                place = 7
                if gameLoc[player.numLoc].wasVisited == False:
                    gameLoc[player.numLoc].printLong()
                    gameLoc[player.numLoc].visitLoc()
                    player.addScore()
                    score(player)
                else:
                    gameLoc[player.numLoc].printShort()

            else:
                print("\nYou're not asleep, are you?")

        else:
            print("\nThat is not a valid command")

            
            
            
                
  
            
def main():
    intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter."
    title = "\nAsleep" 
    wrongWay = "\nYou can't go that way!"
    days = 0
    direction = "some way"
    name = str(input("What is your name? "))
    gameLoc = []

    


    player = Player(name, 0, "Living Room", 0, 0, ["ring"])

    

    livingRoom0 = Locale("Living Room",
                         ("\nYou drop your keys and jacket on the table, exhausted "
                         "after a long and difficult day of work, like all the others. "
                         "Your room is just down the hall to the West, waiting for you."),
                         ("\nYou're back in the living room, struggling to keep your eyes open."),
                         False,
                         False,
                         "map")

    kitchen0 = Locale("Kitchen",
                     ("\nYou go into the kitchen, even though you aren't hungry. A "
                      "letter with " + name + " on it is held on the fridge by a magnet, you "
                      "don't really want to think about it..."),
                     ("\nYou're really TIRED, not HUNGRY."),
                      False,
                      False,
                      "knife")

    bedroom0 = Locale("Bedroom",
                     ("\nYour bedroom, with your bed in the center of the back "
                      "wall, to the North. You take your medicine and prepare for "
                      "bed. You'll have to remember to take it every morning and night"),
                     ("\nThe bed is so close..."),
                      False,
                      False,
                      "nothing")

    bathroom0 = Locale("Bathroom",
                      ("\nYou use the bathroom, even though you didnt really have to, "
                       "and prepare to go to sleep."),
                      ("\nYou don't need to use the bathroom again."),
                       False,
                       False,
                       "nothing")

    bed0 = Locale("Bed",
                 ("\nYour bed, not as comfortable as it used to be... Still, "
                  "you are weary enough to sleep. Enter 'Sleep' to sleep."),
                 ("\nEnter 'Sleep' to sleep."),
                  False,
                  False,
                  "nothing")

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
                              "key")

    bedroomDream0 = Locale("Bedroom?",
                          ("\nYou push open the door, and find the TV still on. A note "
                           "lies on the bed, with the name " + name + " written on the "
                           "top in HER handwriting. Enter 'wake up' to wake."),
                          ("\nThe note is still laying on the bed. You take in the handwriting of your "
                           "name, " + name + ", once again. It's just the same as that night..."),
                           False,
                           False,
                           "nothing")

    bed1 = Locale("Bed",
                 ("\nYou wake in a cold sweat. Your dream had been so real, "
                  "it felt as if you had really been there reliving that same "
                  "night. You don't feel so well, but still, you decide to get "
                  "out of bed and go to work."),
                 ("\nYou should really get going if you want to get to work on time."),
                  False,
                  False,
                  "nothing")

    bedroom1 = Locale("Bedroom",
                     ("\nYou change into your work clothes, but you still need to shower and brush your "
                      "teeth in the bathroom to the West."),
                     ("\nYou feel like you might be forgetting something.."),
                      False,
                      False,
                      "medicine")

    bathroom1 = Locale("Bathroom",
                      ("\nYou enter the bathroom and take your shower, but still, "
                       "the cold feeling from that dream stays with you."),
                       ("\nI knew you wouldn't forget to brush your teeth."),
                       False,
                       False,
                       "nothing")

    livingRoom1 = Locale("Living Room",
                        ("\nYou grab your jacket and keys, somewhat ready to head "
                         "out for the day. You have to unlock the door first though..."),
                        ("\nIt is time to leave for work, unfortunately."),
                         False,
                         False,
                         "gold necklace")

    kitchen1 = Locale("Kitchen",
                      "\nMaybe you should grab some breakfast, even if you'll be late.",
                      "\nYou realize that the letter is gone...",
                      False,
                      False,
                      "bowl of cereal")
                       
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
              [7, 8, 10, 9],
              [9, 9, 8, 9],
              [10, 10, 11, 8],
              [11, 11, 11, 10]]
    
    start(title, intro, gameLoc, player)
    end(game(matrix, gameLoc, player))
    

main()









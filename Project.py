# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure
intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter."
title = "\nAsleep"
commands = "\nValid commands: North, South, East, West, Help, Map, Points, Location, Quit"
wrongWay = "\nYou can't go that way!"
playerLocation = "Living Room"
days = 0
playerScore = 0
livingRoomVisit1 = 0
roomVisit1 = 1
bedVisit1 = 2
sleepVisit1 = 3
livingRoomDreamVisit1 = 4
roomDreamVisit1 = 5
kitchenVisit1 = 6
bedVisit2 = 7
roomVisit2 = 8
placeVisit = [False, False, False, False, False, False, False, False, False]
name = str(input("What is your name? "))
gameLocations = [ ("\nYou drop your keys and jacket on the table, exhausted "
                   "after a long and difficult day of work, like all the others. "
                   "Your room is just down the hall to the West, waiting for you."),
                  ("\nYour bedroom, with your bed in the center of the back "
                   "wall, to the North. You take your medicine and prepare for "
                   "bed."),
                  ("\nYour bed, not as comfortable as it used to be... Still, "
                   "you are weary enough to sleep. Enter 'Sleep' to sleep."),
                  ("\nYou drift to sleep, and find yourself arriving home "
                   "after a long and difficult day of work, like all the others..."), 
                  ("\nYou drop your keys and winter jacket on the table, "
                   "exhausted. It takes you a minute to realize what you're "
                   "doing, you should be asleep, right? A faint glow is coming "
                   "from your bedroom down the hall."),
                  ("\nYou push open the door, and find the TV still on. A note "
                   "lies on the bed, with the name " + name + " written on the "
                   "top in HER handwriting."),
                  ("\nYou go into the kitchen, even though you aren't hungry. A "
                   "letter with " + name + " on it is held on the fridge by a magnet, you "
                   "don't really want to think about it..."),
                  ("\nYou wake in a cold sweat. Your dream had been so real, "
                   "it felt as if you had really been there reliving that same "
                   "night. You don't feel so well, but still, you decide to get "
                   "out of bed and go to work."),
                  ("\nYou change into your work clothes and take your medicine "
                   "for the morning, but you still need to shower and brush your "
                   "teeth in the bathroom to the West.")]


def day():
    global days
    print("\nDay", days)
    print("=====")

def score():
    global playerScore
    print("\nYour score is: ", playerScore)

def start():
    print(title)
    print("======\n")

    global playerScore
    # Hey this worked print(("i am really not very sure about how to seperate a string into "
    # "multiple lines but i saw this somewhere"))
    print(intro)
    playerScore = playerScore + 5
    print(gameLocations[0])
    score()



def end():
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")

start()

#end() Testing new end function

gameMap = "    Bed\n    |\n    Room -- Living Room -- Kitchen"

def goto(location):
    global playerScore
    global playerLocation
    if location == "Kitchen":
        playerLocation = "Kitchen"
        if placeVisit[6] == False:
            placeVisit[6] = True
            print(gameLocations[6])
            playerScore = playerScore + 5
            score()
        elif placeVisit[6] == True:
            print("\nYou're really TIRED, not HUNGRY.")
    
def main():
    
    while True:
        global playerLocation
        global playerScore
        global days
        command = input("\nEnter a command: ").lower()

        if command == "help":
            print(commands)

        elif command == "quit":
            break

        elif command == "points":
            score()

        elif command == "map":
            print(gameMap)

        elif command == "location":
            print("\nLocation:", playerLocation)

        elif command == "north":
            if playerLocation == "Bedroom":
                playerLocation = "Bed"
                placeVisit[2] = True
                print(gameLocations[2])
                playerScore = playerScore + 5
                score()
                
            else:
                print(wrongWay)

        elif command == "south":
            if playerLocation == "Bed" and days == 1:
                playerLocation = "Bedroom"
                if placeVisit[8] == False:
                    placeVisit[8] = True
                    print(gameLocations[8])
                    playerScore = playerScore + 5
                    score()
    #Ending here for now
                    break
    #Ending here for now
                elif placeVisit[8] == True:
                    print("You should really get going if you want to get to work on time.")
            else:
                print(wrongWay)

        elif command == "east":
            if playerLocation == "Living Room":
                goto("Kitchen")

            elif playerLocation == "Bedroom":
                playerLocation = "Living Room"
                print("\nYou're back in the living room, struggling to keep your eyes open.")

            elif playerLocation == "Bedroom?":
                playerLocation = "Living Room?"
                print("\nIt is unusually cold in the house.")
                
            else:
                print(wrongWay)

        elif command == "west":
            if playerLocation == "Living Room":
                playerLocation = "Bedroom"
                if placeVisit[1] == False:
                    placeVisit[1] = True
                    print(gameLocations[1])
                    playerScore = playerScore + 5
                    score()
                elif placeVisit[1] == True:
                    print("\nThe bed is so close...")
                    
            elif playerLocation == "Kitchen":
                playerLocation = "Living Room"
                print("\nYou're back in the living room, struggling to keep your eyes open.")

            elif playerLocation == "Living Room?":
                playerLocation = "Bedroom?"
                if placeVisit[5] == False:
                    placeVisit[5] = True
                    print(gameLocations[5])
                    print("\nYou need to wake up. Type 'Wake up' at any time to wake up.")
                    playerScore = playerScore + 5
                    score()
                elif placeVisit[5] == True:
                    print("\nThe note is still laying on the bed. You take in the handwriting of your name, " + name + ", once again. It's just the same as that night...")
                
            else:
                print(wrongWay)

        elif command == "sleep":
            if playerLocation == "Bed" and days == 0:
                playerLocation = "Living Room?"
                print(gameLocations[3])
                print(gameLocations[4])
                placeVisit[3] = True
                placeVisit[4] = True
                playerScore = playerScore + 10
                score()
            else:
                print("\nYou can't possibly expect to sleep here...")

        elif command == "wake up":
            if playerLocation == "Living Room?" or "Bedroom?":
                days = days + 1
                day()
                playerLocation = "Bed"
                print(gameLocations[7])
                placeVisit[7] = True
                playerScore = playerScore + 5
                score()

        else:
            print("\nThat is not a valid command")

            
            
            
                
  
            
         
    

    
main()


end()











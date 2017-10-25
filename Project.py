# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure
intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter."
title = "Asleep"
commands = "\nValid commands: North, South, East, West, Help, Map, Points, Location, Quit"
wrongWay = "\nYou can't go that way!"
playerLocation = "Living Room"
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

def main():
    
    while True:
        global playerLocation
        global playerScore
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
            if playerLocation == "1":
                continue
            else:
                print(wrongWay)

        elif command == "east":
            if playerLocation == "Living Room":
                playerLocation = "Kitchen"
                if placeVisit[6] == False:
                    placeVisit[6] = True
                    print(gameLocations[6])
                    playerScore = playerScore + 5
                    score()
                elif placeVisit[6] == True:
                    print("\nYou're really TIRED, not HUNGRY.")

            elif playerLocation == "Bedroom":
                playerLocation = "Living Room"
                print("\nYou're back in the living room, struggling to keep your eyes open.")

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
            else:
                print(wrongWay)

        elif command == "sleep":
            if playerLocation == "Bed":
                playerLocation = "Living Room?"
                print(gameLocations[3])
                print(gameLocations[4])
            else:
                print("You can't possible expect to sleep here...")


# Bed
        elif playerLocation == "Bed":
            command = input("Type sleep to sleep: ").lower()
            if command  == "help":
                print("\nSleep")

            elif command == "quit":
                break

            elif command == "sleep":
                playerLocation = "Living room?"
                if livingRoomDreamVisit == False:
                    livingRoomDreamVisit = True
                    print(livingRoomDream)
                    playerScore = playerScore + 5

            else:
                print("\nYou don't dare do anything other than go to sleep right now.")



# Living room dream
        elif playerLocation == "Living room?":
            command = input("Enter a command: ").lower()
            if command  == "help":
                print(commands)

            elif command == "quit":
                break

            elif command == "west":
                playerLocation = "Room?"
                if roomDreamVisit == False:
                    roomDreamVisit = True
                    print(roomDream)
                    print("\nYou need to wake up")
                    playerScore = playerScore + 5

                elif roomDreamVisit == True:
                    print("\nThe note is still laying on the bed. You take in the handwriting of your name, " + name + ", once again. It's just the same as that night...")

            elif command == "north" or "south" or "east":
                print("\nYou can not go that way!")

# Room dream
        elif playerLocation == "Room?":
            command = input("Enter a command: ").lower()
            if command  == "help":
                print("\nWake up")

            elif command == "quit":
                break

            elif command == "east":
                playerLocation = "Living room?"
                print("\nIt is unusually cold in the house.")

            elif command == "wake up":
                break
            
            elif command == "north" or "south" or "west":
                print("\nYou can not go that way!")

            
            
            
                
  
            
         
    

    
main()


end()











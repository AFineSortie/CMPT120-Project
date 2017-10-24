# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure
livingRoom1 = "\nYou drop your keys and jacket on the table, exhausted after a long and difficult day of work, like all the others. Your room is just down the hall to the West, waiting for you." 
room1 = "\nYour bedroom, with your bed in the center of the back wall, to the North. You take your medicine and prepare for bed."
bed1 = "\nYour bed, not as comfortable as it used to be... Still, you are weary enough to sleep."
sleep1 = "\nYou drift to sleep, and find yourself arriving home after a long and difficult day of work, like all the others..."
livingRoomDream1 = "\nYou drop your keys and winter jacket on the table, exhausted. It takes you a minute to realize what you're doing, you should be asleep, right? A faint glow is coming from your bedroom down the hall."
intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter."
#I can't figure out how to break these up they will not work for me
playerLocation = "Living Room"
playerScore = 0
title = "Asleep"
commands = "\nValid commands: North, South, East, West, Help, Quit"

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

def start():
    print(title)
    print("======\n")

    global name
    name = str(input("What is your name? "))        

    print(intro)

def end():
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")
    
#end() Testing new end function

start()

kitchen1 = "\nYou go into the kitchen, even though you aren't hungry. A letter with " + name + " on it is held on the fridge by a magnet, you don't dare touch it."
roomDream1 = "\nYou push open the door, and find the TV still on. A note lies on the bed, with the name " + name + " written on the top in HER handwriting."
gameLocations = [ "\nYou drop your keys and jacket on the table, exhausted after a long and difficult day of work, like all the others. Your room is just down the hall to the West, waiting for you."]

playerScore = playerScore + 5
print(livingRoom1)

def main():

    while True:

        global playerLocation
        global playerScore
        global livingRoomVisit
        global roomVisit
        global bedVisit
        global sleepVisit
        global livingRoomDreamVisit
        global roomDreamVisit
        global kitchenVisit
        
        print("\nLocation:", playerLocation, "\n")
        print("Your score is", playerScore, "\n")


# Living Room
        if playerLocation == "Living Room":
            livingRoomVisit = True
            command = input("Enter a command: ").lower()
            if command == "help":
                print(commands)

            elif command == "quit":
                break

            elif command == "west":
                playerLocation = "Room"
                if roomVisit == False:
                    roomVisit = True
                    playerScore = playerScore + 5
                    print(room)
                elif roomVisit == True:
                    print("\nThe bed is so close...")

            elif command == "east":
                playerLocation = "Kitchen"
                if kitchenVisit == False:
                    kitchenVisit = True
                    print(kitchen)
                    playerScore = playerScore + 5
                elif kitchenVisit == True:
                    print("\nYou're really TIRED, not HUNGRY.")
            elif command == "north" or "south":
                print("\nYou can not go that way!")
            

#Room
        elif playerLocation == "Room":
            command = input("Enter a command: ").lower()
            if command == "help":
                print(commands)
                
            elif command == "quit":
                break

            elif command == "east":
                playerLocation = "Living Room"
                print("\nYou're back in the living room, struggling to keep your eyes open.")

            elif command == "north":
                playerLocation = "Bed"
                bedVisit = True
                playerScore = playerScore + 5
                print(bed)
            elif command == "west" or "south":
                print("\nYou can not go that way!")
                
                    


# Kitchen
        elif playerLocation == "Kitchen":
            command = input("Enter a command: ").lower()
            if command == "help":
                print(commands)
                
            elif command == "quit":
                break

            elif command == "west":
                playerLocation = "Living Room"
                print("\nYou're back in the living room, struggling to keep your eyes open.")

            elif command == "east" or "south" or "north":
                print("\nYou can not go that way!")

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











# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure
livingRoom = "\nYou drop your keys and jacket on the table, exhausted after a long and difficult day of work, like all the others. Your room is just down the hall to the West, waiting for you.\n"
kitchen = "\n You go into the kitchen, even tough you aren't hungry. A letter with your name on it is held on the fridge by a magnet, you don't dare touch it."
room = "\nYour bedroom, with your bed in the center of the back wall, to the North. You take your medicine and prepare for bed.\n"
bed = "\nYour bed, not as comfortable as it used to be... Still, you are weary enough to sleep.\n"
sleep = "\nYou drift to sleep, and find yourself arriving home after a long and difficult day of work, like all the others...\n"
livingRoomDream = "\nYou drop your keys and winter jacket on the table, exhausted. It takes you a minute to realize what you're doing, you should be asleep, right? A faint glow is coming from your bedroom down the hall."
intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter.\n"
playerLocation = "Living Room"
playerScore = 0
title = "Asleep"
name = "sampleName"
commands = "\nValid commands: North, South, East, West, Help, Quit"

def start():
    print(title)
    print("======\n")

    global name
    name = input("What is your name? ")        

    print(intro)

roomDream = "\nYou push open the door, and find the TV still on. A note lies on the bed, with the name", name, "written on the top in her handwriting."

def end():
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")
    
#end() Testing new end function

start()

playerScore = playerScore + 5
print(livingRoom)

def main():

    while True:

        global playerLocation
        global playerScore

        livingRoomVisit = False
        roomVisit = False
        bedVisit = False
        sleepVisit = False
        livingRoomDreamVisit = False
        roomDreamVisit = False
        
        print("\nLocation:", playerLocation, "\n")
        print("Your score is", playerScore, "\n")

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
                    playerScore = playerScore + 5
                    roomVisit = True

                print(room)

        if playerLocation == "Room":
            command = input("Enter a command: ").lower()
            if command == "help":
                print(commands)
                
            elif command == "quit":
                break

            elif command == "east":
                playerLocation = "Living Room"

                print("\nYou're back in the living room, struggling to keep your eyes open.")

            
            
    

    
main()

input("Press 'Enter' to continue")
playerLocation = room
playerScore = playerScore + 5

print(room)
print("Your score is", playerScore, "\n")

input("Press 'Enter' to continue")
playerLocation = bed
playerScore = playerScore + 5

print(bed)
print("Your score is", playerScore, "\n")

input("Press 'Enter' to continue")
playerLocation = sleep
playerScore = playerScore + 5

print(sleep)
print("Your score is", playerScore, "\n")

input("Press 'Enter' to continue")

end()











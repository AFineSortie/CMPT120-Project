# Chris Petrucelli
# CMPT 120 Project
# Text-based Adventure
house = "\nYou drop your keys and jacket on the table, exhausted after a long and difficult day of work, like all the others. Your room is just down the hall, waiting for you.\n"
room = "\nYour bedroom, with your bed in the center of the back wall. You take your medicine and prepare for bed.\n"
bed = "\nYour bed, not as comfortable as it used to be... Still, you are weary enough to sleep.\n"
sleep = "\nYou drift to sleep, and find yourself arriving home after a long and difficult day of work, like all the others...\n"
intro = "\nYou finally pull into your driveway after your hour drive home. You shut off your car, unlock your front door, and enter.\n"
playerLocation = house
playerScore = 0
title = "Asleep"
name = "sampleName"

def start():
    print(title)
    print("======\n")

    global name
    name = input("What is your name? ")

    print(intro)

def end():
    print("\nTo Be Continued...")
    print("Final score:", playerScore, "\n")
    print("(c) 2017 Christopher Petrucelli, christopher.petrucelli1@marist.edu")
    
#end() Testing new end function

start()

input("Press 'Enter' to continue")
playerScore = playerScore + 5

print(house)
print("Your score is", playerScore, "\n")

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











import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)

def things(): # Home related things 

    things = {
        "phone": "Here is your phone",
        "TV": "Turning on the TV",
        "bag": "Here is your bag",
        "fan": "Turn on your fan"
    }

    found = 0

    for thing in things:

        if thing in text:

            print("FOUND IT")
            print(things[thing])
            engine.say(things[thing])

            found = 1
            break

    if found == 0:
        print("NOT FOUND")

engine.runAndWait()


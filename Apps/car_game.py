command = ""
started = False

while True:
    command = input("> ").lower()
    if command== "start":
        if started:
            print("Car already running!")
        else:
            started= True
            print("Car started! Lets go! ")
    elif command=="stop":
        if not started:
            print("Car already stopped!")
        else:
            started=False
            print("Car Stopped :) ")
    elif command == "help":
        print('''
start- start the car
stop- stop the car
quit- to exit game''')
    elif command == "quit":
        break
    else:
        print("Sorry invalid command")

play = True
prev_command = ''
while(play):
    command = input('> ').lower()
    if command == 'start' and prev_command != command:
        print('Car started...Ready to go!\n')
    elif command == 'start' and prev_command == command:
        print('Car is already started, cannot start again !!!\n')
    elif command == 'stop' and prev_command != command:
        print('Car stopped.\n')
    elif command == 'stop' and prev_command == command:
        print('Car is already stopped, cannot steop again !!!\n')
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        help - to see instructions\n
        """)
    elif command == 'quit':
        print()
        play = False
    else:
        print("I don't understand that\n")
    prev_command = command
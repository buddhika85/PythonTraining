play = True
while(play):
    command = input('>').lower()
    if command == 'start':
        print('Car started...Ready to go!')
    elif command == 'stop':
        print('Car stopped.')
    elif command == 'quit':
        print()
        play = False
    else:
        print("I don't understand that")
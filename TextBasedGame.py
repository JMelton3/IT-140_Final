# John Melton
# IT-140 22EW6

start_room = 'Cockpit'
current_room = start_room
is_game_over = False

rooms = {
    'Cockpit': {'East': 'Mess Hall'},
    'Mess Hall': {'North': 'Research Lab', 'East': 'Engine Room', 'West': 'Cockpit'},
    'Engine Room': {'North': 'Living Quarters', 'East': 'Cargo Bay',
                    'South': 'Life Support', 'West': 'Mess Hall'},
    'Life Support': {'North': 'Engine Room', 'South': 'Armory'},
    'Armory': {'North': 'Life Support'},
    'Research Lab': {'East': 'Living Quarters', 'South': 'Mess Hall'},
    'Living Quarters': {'South': 'Engine Room', 'West': 'Research Lab'},
    'Cargo Bay': {'West': 'Engine Room'}
}
player_items = []

room_item = {
    'Mess Hall': 'Rations',
    'Engine Room': 'Fuel',
    'Life Support': 'Oxygen',
    'Armory': 'Flamethrower',
    'Research Lab': 'Space Suit',
    'Living Quarters': 'Bandages',
}

#function to display valid input commands
def show_options():
    move_options = rooms.get(current_room)
    r = 'Commands: '
    if current_room in room_item:
        print('There must be something here I can use...')
        r += 'Search Room' + ', '
    for x in move_options.keys():
        r += 'Go ' + x + ', '
    r += 'Check Backpack, Exit Game'
    print(r)
    print('What would you like to do?')


def search_room():
    if current_room in room_item:
        new_item = room_item.pop(current_room)
        player_items.append(new_item)
        print('You search the '+ current_room.lower() + ' and after a few moments you find the ' + new_item
              + '\nYou add the ' + new_item + ' to your backpack.')
        if len(player_items) >= 6:
            print('Your backpack is getting full pretty full')
    else:
        print('You search the room but find nothing of use')


#Displaying basic instructions to the user to set up the game
print('You wake up in the cockpit of your spaceship after losing consciousness.')
print('You see a red light flashing on your terminal that reads “unidentified life-form detected”.')
print('Your ship is on the way to earth and you must search the ship and eliminate the '
      'threat before your ship reaches earth.')
# Main gameplay loop
while not is_game_over:
    print('Current room:', current_room)
    show_options()
    player_input = input()
    if player_input.lower() == 'exit game':
        print('Thank you for playing. \r\nExiting Game...')
        is_game_over = True
    elif player_input.lower() == 'search room':
        search_room()
    elif player_input.lower() == 'check backpack':
        items_msg = 'Items: '
        i = 0
        for x in player_items:
            items_msg += x
            if i != len(player_items) - 1:
                items_msg += ', '
            i += 1
        print(items_msg)
    else:
        move_options = rooms.get(current_room)
        move = player_input[3:]
        is_valid = move.capitalize() in move_options
        if is_valid:
            current_room = move_options.get(move.capitalize())
            if current_room == 'Cargo Bay':
                if len(room_item) == 0:
                    print('You enter the room and see a giant alien guarding the escape pods.\r\n'
                          'You turn your flamethrower towards the monster and burn it to a crisp.\r\n'
                          'You have won the game! Thank you for playing!!!')
                else:
                    print('You enter the room and see a giant alien guarding the escape pods.\r\n'
                          'The alien spits acidic goo and you die.\r\n'
                          'Game over.')
                is_game_over = True
        else:
            print('Invalid input. Please try again...')
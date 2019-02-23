from clear_console import clear


def menu():
    # prints the main menu
    print('WORK LOG')
    print('What whould you like to do?')
    while True:
        answer = input(
            '1: Add new entry \n' +
            '2: Search in existing entries\n' +
            '3: Quit Program\n')
        if answer in '123':
            break
        else:
            clear()
            print(f'Option {answer} is not in the menu. Please choose again.')
            continue
    clear()
    return answer

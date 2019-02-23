from clear_console import clear
from search_options import date_search, date_range_search, regex_search


def search_entry():
    print('Do you want to search by:')
    while True:
        choice = input(
            '1: Exact Date\n' +
            '2: Range of Dates\n' +
            '3: Exact Search\n' +
            '4: Regex pattern\n' +
            '5: Return to menu\n')
        if choice in '12345':
            break
        else:
            clear()
            print(f'Option {choice} is not in the menu')
            input('Press enter to try again')
            continue
    clear()
    if choice in '1':
        date_search()
    elif choice in '2':
        date_range_search()
    elif choice in '3':
        print('Enter search pattern')
        # normal search can use regex function to search
        regex_search()
    elif choice in '4':
        print('Enter regex pattern')
        regex_search()
    elif choice in '5':
        # return to the start menu
        return

from menu import menu
from clear_console import clear
from add_entry import add_entry
from entry_search import search_entry

if __name__ == "__main__":
    while True:
        clear()
        choice = menu()
        if choice == '3':
            break
        elif choice == '1':
            add_entry()
        elif choice == '2':
            search_entry()

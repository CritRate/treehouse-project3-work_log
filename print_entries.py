from clear_console import clear
from edit_entry import edit_entry


def print_entries(entries):
    clear()
    if len(entries) == 0:
        print('No entries found')
        input('Press enter to return to menu')
        return
    index = 0
    while True:
        clear()
        line_number, entry = entries[index]
        print(f'Date: {entry["date"]}')
        print(f'Title: {entry["title"]}')
        print(f'Time spent: {entry["time"]}')
        print(f'Notes: {entry["notes"]}\n')
        print(f'Result {index + 1} of {len(entries)}\n')
        # first result
        option_without_prev = ('[N]ext, [E]dit, [D]elete, ' +
                               '[R]eturn to search menu\n')
        # result between first and last, but not last
        option_with_prev = ('[P]revious, [N]ext, [E]dit, [D]elete, ' +
                            '[R]eturn to search menu\n')
        # last result
        option_without_next = ('[P]revious, [E]dit, [D]elete, ' +
                               '[R]eturn to search menu\n')
        # only one result
        option_without_next_prev = ('[E]dit, [D]elete, ' +
                                    '[R]eturn to search menu\n')

        if index == 0 and len(entries) == 1:
            option = input(option_without_next_prev)
        elif index == 0:
            option = input(option_without_prev)
        elif index + 1 == len(entries):
            option = input(option_without_next)
        else:
            option = input(option_with_prev)
        option = option.upper()
        if option in 'NPEDR':
            if option in 'N':
                if index + 1 == len(entries):
                    continue
                index += 1
            if option in 'P':
                if index == 0:
                    continue
                index -= 1
            # return in options E and D because the data displayed will be old
            if option in 'E':
                edit_entry(line_number, entry_to_edit=entries[index])
                return
            if option in 'D':
                edit_entry(line_number)
                return
            if option in 'R':
                return
        else:
            continue

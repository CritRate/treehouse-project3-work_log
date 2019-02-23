import csv
from datetime import datetime

from clear_console import clear


def edit_entry(line, entry_to_edit=None):
    clear()
    entries = []
    fieldnames = ['date', 'title', 'time', 'notes']
    with open('log.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line_number, entry in enumerate(reader):
            if line_number == 0:
                continue
            if line_number == line:
                # entry=None => delete entry
                if entry_to_edit is None:
                    continue
                # edit entry
                else:
                    clear()
                    print('What whould you like to edit?')
                    while True:
                        choice = input(
                            '1: Date\n' +
                            '2: Title\n' +
                            '3: Time\n' +
                            '4: Notes\n')
                        if choice in '1234':
                            break
                        else:
                            clear()
                            print(f'Option {choice} is not in the menu')
                            input('Press enter to try again')
                            continue
                clear()
                if choice in '1':
                    while True:
                        try:
                            date = input('Please use DD/MM/YYYY: ')
                            entry['date'] = datetime.strptime(
                                date, '%d/%m/%Y').date()
                            break
                        except:
                            clear()
                            print(f'{date} is not a valid date')
                            input('Press enter to try again')
                            continue
                if choice in '2':
                    entry['title'] = input('Enter new title: ')
                if choice in '3':
                    while True:
                        try:
                            time = input(
                                'Time spent (rounded minutes): ')
                            entry['time'] = int(time)
                            break
                        except:
                            clear()
                            print(f'{time} is not a valid number')
                            input('Press enter to try again')
                            continue
                if choice in '4':
                    entry['notes'] = input('Enter new notes: ')
            entries.append(entry)
    with open('log.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow({
                'date': entry['date'],
                'title': entry['title'],
                'time': entry['time'],
                'notes': entry['notes']
            })

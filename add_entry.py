import os
import csv
from datetime import datetime

from clear_console import clear


def add_entry():
    print('Date of the task')
    while True:
        try:
            date = input('Please use DD/MM/YYYY: ')
            valid_date = datetime.strptime(date, '%d/%m/%Y')
            break
        except:
            clear()
            print(f'{date} is not a valid date')
            input('Press enter to try again')
            continue
    clear()
    title = input('Title of the task: ')
    clear()
    while True:
        try:
            time = input('Time spent (rounded minutes): ')
            valid_time = int(time)
            break
        except:
            clear()
            print(f'{time} is not a valid number')
            input('Press enter to try again')
            continue
    clear()
    notes = input('Notes (Optional, you can leave this empty): ')
    clear()
    # https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not
    file_exist = os.path.isfile('log.csv') and os.path.getsize('log.csv') > 0
    # write csv file
    with open('log.csv', 'a', newline='') as csvfile:
        fieldnames = ['date', 'title', 'time', 'notes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exist:
            writer.writeheader()
        writer.writerow({
            'date': valid_date.date(),
            'title': title,
            'time': valid_time,
            'notes': notes
        })
    input('The entry has been added. Press enter to return to the menu.')

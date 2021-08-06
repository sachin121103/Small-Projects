import datetime

Days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

while True:

    print("Enter the year for the calendar below.")
    year_input = input('> ')

    if year_input.isdigit() and int(year_input) > 0:
        year = int(year_input)
        break

    else:
        print('Enter a valid year!')
        continue

while True:

    print("Enter the month between 1-12 below.")
    month_input = int(input('> '))

    if month_input >=1 and month_input <=12:
        month = month_input
        break
    else:
        print("Enter a number between 1-12 to signify a month!")

def getCalendar(year, month):

    calString = ' '
    calString += (' ' *34) + Months[month-1] + ' ' + str(year) + '\n'
    calString += '...Sunday.....Monday....Tuesday...Wednesday...Thursday.... Friday....Saturday..\n'

    weeklysep = ("+----------" * 7) + '+\n'
    blankRow = ('|          ' * 7) + "\n"

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:

        calString += weeklysep

        daynumrow = ''

        for i in range(7):
            daynumlabel = str(currentDate.day).rjust(2)
            daynumrow += '|' + daynumlabel + (' '*8)
            currentDate += datetime.timedelta(days=1)
        
        daynumrow += '|\n'

        calString += daynumrow
        for i in range(3):
            calString += blankRow

        if currentDate.month != month:
            break
    
    calString += weeklysep
    return calString

calText = getCalendar(year, month)
print(calText)











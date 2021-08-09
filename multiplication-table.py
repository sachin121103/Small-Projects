def multiplication_table():

    print("   |   1  2   3   4   5   6   7   8   9   10  11  12")
    print("---+-------------------------------------------------+")

    for num in range(1, 13):

        print(str(num).rjust(2), end=' ')
        print("|", end=' ')

        for num2 in range(1, 13):
            print(str(num * num2).rjust(3), end=' ')
    
        print()
    
    print('---+-------------------------------------------------+')

multiplication_table()
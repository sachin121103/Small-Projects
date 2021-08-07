def collatz(n):

    if n % 2 == 0:
        print(n / 2)
        return n / 2
    if n % 2 == 1:
        print(3*n + 1)
        return 3*n + 1
    

num= int(input('Input a number: '))

while num != 1:
    num = collatz(num)
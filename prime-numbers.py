# Find if a given number is prime

def isPrime(num):
    factors_list = []
    for i in range(2, num):
        if num % i == 0:
            factors_list.append(i)
    
    if factors_list:
        print("The number is not prime")
    
    else:
        print("The number is prime")

isPrime(4)


def factor_finder(num):
    factors = []

    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
        
    return factors
        


num_input = input("Enter a number: ")
print(factor_finder(int(num_input)))
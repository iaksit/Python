num = int(input("Enter number: "))
factors_of_number = [k for k in range(1, num + 1) if num % k == 0]
count_factors_of_number = len(factors_of_number)

print("Factors of {0} are {1}, the factor count of number is {2} " .format(num,factors_of_number,count_factors_of_number))

exit()

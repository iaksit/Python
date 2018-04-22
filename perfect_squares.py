num = int(input("Enter number: "))
dict_perfect_squares = {k * k: k for k in range(1, num + 1)}
count_perfect_squares_of_number = len(dict_perfect_squares)

print("Perfect Squares of {0} are {1}, the perfect squares count of number is {2} ".format(num, dict_perfect_squares,
                                                                                  count_perfect_squares_of_number))

exit()

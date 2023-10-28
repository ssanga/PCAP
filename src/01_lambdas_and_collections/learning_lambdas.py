def square(num):
    return num * num

# the expression in lambda will be returned
square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)
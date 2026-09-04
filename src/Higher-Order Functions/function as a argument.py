def square(x):
    return x * x


def calculate(function, value):
    return function(value)


result = calculate(square, 11)

print(result)
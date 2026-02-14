numbers = range(1, 6)

square_dict = {n: n*n for n in numbers}
even_square_dict = {n: n*n for n in numbers if n % 2 == 0}

print("Squares Dictionary:", square_dict)
print("Even Squares Dictionary:", even_square_dict)

numbers = list(range(1, 11))

squares = [n * n for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]
odd_squares = [n * n for n in numbers if n % 2 != 0]

print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Odd Squares:", odd_squares)

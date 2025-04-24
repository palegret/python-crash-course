squares = []

for number in range(1, 11):
    square = number ** 2
    squares.append(square)

print(f"Here is an example of a list of squares using a for loop: {squares}")

# A list comprehension is a compact way to process all or part of the elements 
# in a sequence and return a list with the results. They combine a for loop
# an if statement, and the creation of a new list into a single line of code.

#          new list part goes here
#                      for loop part goes here
#                                                 if statement part goes here
squares = [number ** 2 for number in range(1, 11) if number % 2 == 0]

print(f"Here is an example of a list of squares using a list comprehension: {squares}")

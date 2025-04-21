print("List sorting:")
cars = ["toyota", "honda", "ford", "chevrolet", "nissan"]
print(cars)

print("The sort() method permanently changes the order of the list.")
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("The sorted() function temporarily changes the order of the list.")
cars = ["toyota", "honda", "ford", "chevrolet", "nissan"]
print(f"Original: {cars}")
print(f"Sorted: {sorted(cars)}")
print(f"Original again: {cars}")

print("The reverse() method permanently changes the order of the list.")
print("Note: the reverse() method does not sort the list, it just reverses the order of the elements:")
cars.reverse()
print(cars)
print("The reversed() function temporarily changes the order of the list.")
print(f"Length: {len(cars)}")

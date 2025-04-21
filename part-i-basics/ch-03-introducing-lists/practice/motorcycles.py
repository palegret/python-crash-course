motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print("The insert() method shifts the list to the right from the index.")

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(2, 'harley davidson')
print(motorcycles)

print("The del statement removes an item from a list if you know the index.")

del motorcycles[2]
print(motorcycles)

print("The pop() method removes the last item in a list and returns it.")

print(motorcycles)
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print("You can also use pop() to remove an item at a specific index.")

print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

print("If all you have is the value, you can use the remove() method.") 
print("Note: the remove() method only removes the first occurrence of the value.") 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")

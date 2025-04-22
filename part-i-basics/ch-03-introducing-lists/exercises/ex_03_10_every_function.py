locations = [
    "himalaya", 
    "andes", 
    "tierra del fuego", 
    "labrador", 
    "guam"
]

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

locations = [
    "himalayas", 
    "andes", 
    "tierra del fuego", 
    "labrador", 
    "guam"
]

print("\nEach location by index")
print(f"I would like to visit {locations[0].title()} one day.")
print(f"I would like to visit {locations[1].title()} one day.")
print(f"I would like to visit {locations[2].title()} one day.")
print(f"I would like to visit {locations[3].title()} one day.")
print(f"I would like to visit {locations[4].title()} one day.")

print("\nChanging a location by index")
print(f"I think {locations[0].title()} are too far away and dangerous.")
replacement_location = "niagra falls"
locations[0] = replacement_location
print(f"I think {locations[0].title()} is more my speed.")


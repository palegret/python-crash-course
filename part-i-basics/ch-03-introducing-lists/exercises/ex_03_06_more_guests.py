guest_list = [
    "Albert Einstein", 
    "Beverly Sills", 
    "Enrique Alegret"
]

name = guest_list[0].title()
print(f"{name}, please come to dinner.")

name = guest_list[1].title()
print(f"{name}, please come to dinner.")

name = guest_list[2].title()
print(f"{name}, please come to dinner.")

name = guest_list[0].title()
print(f"\nSorry, {name} can't make it to dinner.")

del(guest_list[0])
guest_list.insert(0, "Brian Cox")

name = guest_list[0].title()
print(f"\n{name}, please come to dinner.")

name = guest_list[1].title()
print(f"{name}, please come to dinner.")

name = guest_list[2].title()
print(f"{name}, please come to dinner.")

print("\nWe got a bigger table!")
guest_list.insert(0, "Benjamin Franklin")
guest_list.insert(2, "Richard Feynman")
guest_list.append("Grace Hopper")

name = guest_list[0].title()
print(f"{name}, please come to dinner.")

name = guest_list[1].title()
print(f"{name}, please come to dinner.")

name = guest_list[2].title()
print(f"{name}, please come to dinner.")

name = guest_list[3].title()
print(f"{name}, please come to dinner.")

name = guest_list[4].title()
print(f"{name}, please come to dinner.")

name = guest_list[5].title()
print(f"{name}, please come to dinner.")

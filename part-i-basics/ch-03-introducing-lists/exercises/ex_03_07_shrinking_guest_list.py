guest_list = [
    "Albert Einstein", 
    "Beverly Sills", 
    "Enrique Alegret"
]

print(guest_list)

guest_list.insert(0, "Marie Curie")
guest_list.insert(2, "Leonardo da Vinci")
guest_list.append("Ada Lovelace")

print(guest_list)

print(f"Hello {guest_list[0]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[1]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[2]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[3]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[4]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[5]}, would you join me for dinner this evening please?")

removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner, the large table was unavailable.")
print(guest_list)

removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner, the large table was unavailable.")
print(guest_list)

removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner, the large table was unavailable.")
print(guest_list)

removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner, the large table was unavailable.")
print(guest_list)

print(f"Hello {guest_list[0]}, would you still like to join me for dinner this evening please?")
print(f"Hello {guest_list[1]}, would you still like to join me for dinner this evening please?")

del guest_list[0]
del guest_list[0]
print(guest_list)

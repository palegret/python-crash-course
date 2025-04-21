guest_list = [
    "Albert Einstein", 
    "Beverly Sills", 
    "Enrique Alegret"
]

print(f"Hello {guest_list[0]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[1]}, would you join me for dinner this evening please?")
print(f"Hello {guest_list[2]}, would you join me for dinner this evening please?")

print(f"It appears {guest_list[0]} will be unable to join us for dinner this evening.")
replacement_guest = "Brian Cox"
guest_list[0] = replacement_guest
print(f"We will be inviting {guest_list[0]} instead.")

print(f"I have confirmed that {guest_list[0]} will be joining us for dinner this evening!")
print(f"I have confirmed that {guest_list[1]} will be joining us for dinner this evening!")
print(f"I have confirmed that {guest_list[2]} will be joining us for dinner this evening!")


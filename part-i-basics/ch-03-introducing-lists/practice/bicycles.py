bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print("Asking for the item at index -1 returns the last item in the list:")
print(bicycles[-1])

print("Index -2 returns the second to last item in the list, and so on:")
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

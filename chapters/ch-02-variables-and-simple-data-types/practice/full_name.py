first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = "python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = " python"
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = " python "
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)

person_name = "Phil Alegret"
print(f"Person Name:\n\t{person_name}")

person_name = "Phil Alegret "
print(f"[{person_name}]")
person_name = person_name.rstrip()
print(f"[{person_name}]")

person_name = " Phil Alegret"
print(f"[{person_name}]")
person_name = person_name.lstrip()
print(f"[{person_name}]")

person_name = " Phil Alegret "
print(f"[{person_name}]")
person_name = person_name.strip()
print(f"[{person_name}]")

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)

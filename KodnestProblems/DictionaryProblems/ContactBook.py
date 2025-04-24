contact = {}

while True:
    user_input = input().strip()
    if user_input == 'done':
        break
    name,phone_number = user_input.split(",")
    phone_number = phone_number.strip()
    contact[name] = phone_number
for name, phone_number in contact.items():
    print(f"{name}: {phone_number}")
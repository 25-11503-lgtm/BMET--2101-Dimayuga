correct_pin = "1234"
attempts = 0
while attempts < 3:
    user_pin = input("PIN: ")
    attempts += 1
    if user_pin == correct_pin:
        print("Access granted")
        break
else:
    print("Card blocked")

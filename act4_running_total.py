total = 0
count = 0
price = float(input("Price (0 to stop): "))
while float(input("Price (0 to stop): ")):
    total += price
    count += 1
if count > 0:
    average = total / count
else:
    average = 0
print(f"Items: {count}  Total: {total:.2f}")
print(f"Average:{average:.2f}")

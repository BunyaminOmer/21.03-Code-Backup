# Aralık belirterek for döngüsünü çalıştırmak -> range

for item in range(1, 101):
    if item % 5 == 0:
        print(item)

# Liste içindeki verileri tek tek işlemek
users = ["Aysen", "Fatma", "Cigdem", "Hasan", "Ahmet", "Mehmet"]

print("*" * 30)

for user in users:
    print(user)


print("*" * 30)

# item ve index bilgisi ile listleri döngüde kullanmak -> enumerate
for obj in enumerate(users):
    # print(obj[0], obj[1])
    print(users[obj[0]])
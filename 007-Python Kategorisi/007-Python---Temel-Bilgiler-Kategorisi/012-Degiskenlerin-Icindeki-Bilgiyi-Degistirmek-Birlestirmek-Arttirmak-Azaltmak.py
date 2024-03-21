# Değişken İçindeki Bilgiyi Değiştirmek
user_name = "Lorem"
print(user_name)

# user_name = input("Adınız: ")
user_name = "Değişti"
print(user_name)

# Değişkenler İçindeki Bilgileri Birleştirmek
first_name = "Bünyamin Ömer"
last_name = "Karakuş"
full_name = first_name + last_name # Boşluk Yok
full_name = first_name + "" + last_name # Yine Boşluk Yok
full_name = first_name + " " + last_name

print(full_name)

# full_name = full_name + " Python"
full_name += " Python"
print(full_name)

# Değişken İçindeki Bilgiyi Arttırmak
age = 20
print(age)
age += 1
age += 10
print(age)

# Değişken İçindeki Bilgiyi Arttırmak
age -= 20
print(age)

age *= 20
print(age)

age /= 2
print(age)
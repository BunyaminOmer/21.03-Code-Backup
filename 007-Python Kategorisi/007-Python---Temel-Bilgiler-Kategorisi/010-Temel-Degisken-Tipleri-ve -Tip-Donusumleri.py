# Metinsel ifadeler -> str
first_name = "Hakan"
print("first_name", first_name, type(first_name))

# Tam Sayılar -> int
age = 33
print("age", age, type(age) )


# Virgüllü Sayılar -> float
tax = 1199 * 0.18
print("tax", tax, type(tax))

# True / False -> bool
is_active = True
print("is_active", is_active, type(is_active))

# Metinden Tam Sayı Dönüşümü
age = input("Yasin Kac:  ")
age = int(age)
print("age", age, type(age) )

# Virgüllü Sayıdan Tam Sayıya Dönüşüm
tax = int(tax)
print("tax", tax, type(tax))

# Boolean Dönüşümü
print(bool(tax))
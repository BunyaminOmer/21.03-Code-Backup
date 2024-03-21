# Toplama Çıkarma

print(2 + 2)
print(3 + -2)

# Çarpma Bölme

print(2 * 10)
print(3 / 2) # Python3: Sonuç 1.5, Python2: Sonuç 1 // Neden ? Python3 Bölmede Float, Python2 Bölmede Int döner...
print("3 / 3:::", type(3 / 3))
print("3 * 3:::", type(3 * 3))

# İşlem Önceliği ve Parantez Kullanımı
# print(2 + 8 * 5) -> 50 Çıkmadı :)))
print( (2 + 8) * 5)

# Kalansız Bölme (Int)
print(3 / 3)
print("3 / 3:::", type(3 / 3))

print(3 // 3)
print("3 // 3:::", type(3 // 3))
print(4 // 3)

# Mod Alma (Kalanı Bulma) / Divmod

print("Kalan Nedir?", 9 % 3)
print("Kalan Nedir?", 20 % 6)
print(20 // 6)

# Kalansız Bölme ve Kalanı Bulma :)
print("Divmod'u göster")
print( divmod(20, 6) )
first_name = "peLin"
last_name = "dJaNGo"
user_name = "123456789"

# Str'nin ilk karakteri [0]
print(first_name[0])
print(last_name[1])

# Belli bir yerden başlayan bilgiyi göster [3:10]
print(first_name[2:4])

# Baştan 3 Karakter [:3]
print(first_name[:3])

# Sondan 3 Karakter [-3:]
print(first_name[-3:])

# Sondan 3 Karakteri Gösterme [:-3]
print(user_name[:-3])

# Ters çevir [::-1]
print(user_name[::-1])

# Tümü Büyük Harf Olsun -> Upper
full_name = first_name + " " + last_name
print(full_name.upper())

# İlk Harfi Büyük Olsun -> Capitalize
print(full_name.capitalize())

# İlk Harfleri Büyük Olsun -> Title
print(full_name.title())

# Ters Çevir -> Swapcase
print(full_name.swapcase())

# Küçük Harf Olsun -> Lower
print(full_name.lower())

# say -> count
print(full_name.lower().count("n"))

# Liste İçindekileri Birleştir -> Join

names = ["Pelin", "Cem", "Bilge", "Deniz"]
print(",".join(names))

# Parçala / Ayır -> Split
print(full_name.split(" "))

# SOR:::

# Başlık Şeklinde Mi? İstitle
print("Django".istitle())
print(last_name.istitle()) 

# Hepsi Küçük Harf Mi? İslower
print("pelin".islower())
print(first_name.islower())

# print(input("Adınızı Yazın : ").islower())

# Belli Bir Karakterle Başlıyor Mu? Startswith
print("Belli Bir Karakterle Başlıyor Mu? Startswitch", first_name.startswith("p"))

# Belli Bir Karakterle Bitiyor Mu? Endswith
print("Belli Bir Karakterle Başlıyor Mu? Endswith", first_name.endswith("p"))

# Aradığım Bilgi Str İçinde Varmı? Find
print(user_name.find("3"))
print(user_name[user_name.find("7"):])

print(full_name[full_name.lower().find("n"):])

# Belli bir bilgiyi Değiştir? Replace
print(full_name.replace("peLin", "Python"))
# İçinde Bilgi Var mı?
# "lorem"
# 10
# -10
# 0
username = ""
print(bool(username))

age = 10
print(bool(age))

# Yaş Eşit mi 0'a?

age = 0
print(bool(age == 0))

# Yaş Eşit Değildir 0'a
age = 25
print(age != 0)
print(not age == 0)

# Yaşı 18'den Büyük mü?
print( age > 18 )

# Yaşı 18'den Küçük mu?
print( age < 18 )

# Yaşı 18'den Büyük veya Eşit mi?
print( age >= 18 )

# Yaş Bilgisi 20 ile 30 Arasında mı ?
age = 25
print(20 < age < 30)

# Yaşı 18'den Büyük mü veya Kadın mı? OR Kullanımı
gender = "f"
age = 10
print("Yaşı 18'den Büyük mü veya Kadın mı? OR Kullanımı", age > 18 or gender == 'f')

# Yaşı 18'den Büyük mü ve Kullanıcı Bilgisi Var mı?
username = ""
age = 20
print("Yaşı 18'den Büyük mü ve Kullanıcı Bilgisi Var mı?", age > 18 and bool(username))
print("Yaşı 18'den Büyük mü ve Kullanıcı Bilgisi Var mı?", age > 18 and username != "")
print("Yaşı 18'den Büyük mü ve Kullanıcı Bilgisi Var mı?", age > 18 and not username == "")

username = "lorem"
print("Yaşı 18'den Büyük mü ve Kullanıcı Bilgisi Var mı?", age > 18 and bool(username))
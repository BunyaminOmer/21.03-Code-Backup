# Yaş bilgisi int olarak mı girildi?
# eğer KOŞUL:
#    DOĞRUYSA BUNU YAP
# DEĞİLSE:
#   BUNU YAP

age = input("Yaşınızı Girin: ")
print(type(age))

if age.isdigit():
    age = int(age)
    age += 1

# print(age)

# Kullanıcı Adı Doğru Mu?
SYS_USER_NAME = "Bünyamin Ömer"
user_name = input("Kullanıcı Adınızı Giriniz: ").title()

if SYS_USER_NAME == user_name:
    print("Kullanıcı Adı Doğru.")

else:
    print("Kullanıcı Adını Hatalı Girdiniz.")

# Kullanıcı 18 Yaşından Büyük Mü?

if age.isdigit() and int(age) > age:
    print("18 Yaşından Büyüksünüz")

else:
    print("18 Yaşından Küçüksünüz")
    
# Kullanıcı ad bilgisini bildirene kadar devam et.. Ve en az 5 karakter olsun
user = ""

while len(user) < 5:
    print("Lütfen kullanıcı adı 5 karakter veya daha fazla olsun..")
    user = input("Kullanıcı Adını Giriniz : ")
    print(user)


# kullanici ad ve soyad bilgisini bildirene kadar sormaya devam et..
first_name, last_name = "", ""
while len(first_name) < 5 and len(last_name) < 5:
    print("Lütfen kullanıcı adı 5 karakter veya daha fazla olsun..")
    first_name = input("Adınız : ")
    last_name = input("Soyadınız : ")

# Kullanıcı ad veya soyad bilgisini bildirene kadar sormaya devam et..

first_name, last_name = "", ""
while len(first_name) < 5 or len(last_name) < 5:
    print("Lütfen kullanıcı adı 5 karakter veya daha fazla olsun..")
    first_name = input("Adınız : ")
    last_name = input("Soyadınız : ")
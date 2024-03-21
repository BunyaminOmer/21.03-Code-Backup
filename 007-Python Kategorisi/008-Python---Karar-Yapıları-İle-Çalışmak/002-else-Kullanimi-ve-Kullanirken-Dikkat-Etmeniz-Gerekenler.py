from curses.ascii import isdigit

age = input("Yasinizi Giriniz: ")

# Kullanıcı 18 Yaşından Büyük mü?

# if age.isdigit() and int(age) > 18:
#     print("18 yaşından büyük")
# else:
#     print("Verdiğiniz bilgiler doğru değil veya 18 yaşından küçüksünüz")


if not age.isdigit():
    print('Yas Bilgisini Dogru Girmediniz')
else:
    if int(age) > 18:
        print("18 yasindan buyuk")
    else:
        print("18 yasindan kucuksunuz")


if age.isdigit():
    if int(age) > 18:
        print("18 yasindan buyuk")
    else:
        print("18 yasindan kucuksunuz")
else:
    print('Yas Bilgisini Dogru Girmediniz')
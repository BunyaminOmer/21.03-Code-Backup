"""

print('''

--------------------------------------------------------------

Merhaba Bu Bir Çalışma Kodudur
Lütfen önünüze çıkacak soruları doğru bir şekilde yanıtlayınız

--------------------------------------------------------------

''')

name = str(input("Merhaba Sana Adınla Hitap Edebilmem İçin İsmini Söyler Misin: ")).title()
age = int(input(f"Peki O Zaman {name} Bana Yaşını Söyler Misin: "))

# --------------------------------------------------------------------------------------------

age = input("Yaşınızı Girin: ")
if age.isdigit():
    print(True)

else:
    print(False)


"""


print("Mağazamızın giriş sayfasına hoşgeldin!")

print("Sayfamıza üyeliğiniz yoksa üye olmalı, üyeliğiniz varsa giriş yapmalısınız.")
print("""
----------------------------------------------------------------------------------------------
""")

USER_NAMES = []
USER_PASSWORDS = []

while True:
    login = str(input("Giriş: G, Üye Ol, U: ")).title
    
    if login == "G" or login == "Giriş":
        while True:

            SYS_USER_NAME = str(input("Kullanıcı Adı Giriniz: "))
            sys_user_password = input("Şifrenizi Giriniz: ")

            if SYS_USER_NAME == USER_NAMES and sys_user_password == USER_PASSWORDS:
                print("Giriş Başarılı")
                break
            
            else:
                print("Giriş hatalı, şifre ya da kullanıcı adı yanlış.")
    
    elif login == "U" or "Ü" or "Üye" or "Üye Ol":
        new_user_name = str(input("Yeni Kullanıcı Adınız: "))
        new_user_password = input("Yeni Şifreniz: ")
        
        USER_NAMES.append(new_user_name)
        USER_PASSWORDS.append(new_user_password)
        
        print("Üyelik başarıyla oluşturuldu.")
        print("Yeni kullanıcı adınız: ", new_user_name)
        print("Yeni şifreniz: ", new_user_password)

    else:
        print("Yanlış Bilgi Girdiniz")


while True:
    USER_NAME = "bunyaminomer"
    user_password = "Sifre1234"

    SYS_USER_NAME = str(input("Kullanıcı Adı Giriniz: "))
    sys_user_password = input("Şifrenizi Giriniz: ")

    if SYS_USER_NAME == USER_NAME and sys_user_password == user_password:
        print("Giriş Başarılı")
        break

    else:
        print("Giriş hatalı, şifre ya da kullanıcı adı yanlış.")


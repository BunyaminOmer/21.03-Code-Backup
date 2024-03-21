# İnput ile first_name bilgisini al # Yaptım
# İnput ile last_name bilgisini al # Yaptım
# İnput ile year_of_birth bilgisini al # Yaptım
# first_name ve last_name bilgilerinin karakter sayısını yaz # Yapamadım
# fString ile kullanıcının adını ilk harfi büyük olacak şekilde full_name yazdır.
# Yaşını gelecek yılki yaşını fString ile yazdır. # Yaptım
# 18 Yaşından Büyükse True olacak şekilde bilgisini dön. # Hatalı

first_name = str(input("Adınızı Girin: "))
last_name = str(input("Soyadınızı Girin: "))
year_of_birth = int(input("Yaşınızı Girin: "))
full_name = first_name + " " + last_name # full_name i ben ekledim

print(f"Adınızın Karakter Sayısı: {len(full_name)}")
print(f"Adınız: {full_name.title()}")
print(f"Yaşınız: {year_of_birth}, Gelecek Seneki yaşınız: {year_of_birth + 1}")
print(f"Yaşınız 18'den Büyük Mü??? {(2022 - int(year_of_birth)) > 18}") # Bunu hocada test etmedi ve cevap ne olursa olsun True veriyor 
# https://pyformat.info/

first_name = "peLin"
last_name = "dJaNGo"

full_name = f"{first_name} {last_name}"

# Birden Fazla Değiken İçindeki Bilgiyi Birleştirme
hello = "Merhaba " + first_name[0].upper() + ". " + last_name
print(hello)

# fString ile yazımı:
hello = f"Merhaba {first_name[0].upper}. {last_name}"
print(hello)

# Hesaplama Yaparak Str Sonuç Dönmek
# print("Sonuc: " + 10 * 10)  # Çalışmaz Çünkü str ve int birleşmez
print("Sonuç: ", 10 * 10, sep="") 
result = "Sonuç: 10 * 10"
result = "Sonuç: " + str(10 * 10)
print(result)

result = f"Sonuç: {10 * 10}"
print(result)

# Function içinde yapılan hesaplamanın sonucunu dönmek
def multiply(number):
    return number * number

result = f"Sonuç {multiply(10)}"
print("Multiply fonksiyonu kullanıldı:", result)

# Uzun içeriklerin belli bir kısmını göstermek
print(f"{result[:4]}")

# Yazıları Ortalamak Veya Sağa Yaslamak
print("*" * 30)
print(f"{full_name:->30}")
print(f"{'Python':->30}")
print(f"{'Django':->30}")
print("*" * 30)

# Belli Bir Uzunlukta int yapılar oluşturmak: 000034 gibi
number = 34
print(f"{number:06d}")
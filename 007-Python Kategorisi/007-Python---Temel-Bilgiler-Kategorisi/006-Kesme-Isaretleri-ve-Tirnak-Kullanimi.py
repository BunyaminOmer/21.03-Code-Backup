# Tek tırnak, Çıft Tırnak ve DocString
# Not her bilgi satır başından başlamalı ama : karakteri varsa girinti vardır.
# ve girintili yapıyı kullanmamız gerekir.

print("Çift Tırnak Kullandık")
print("Tek Tırnak Kullandık")

print(
"""
Çift tırnak ile birden
fazla satır yazdık
"""
)

'''
Tek Tırnak İle
Birden fazla satır yazdık.
'''

# Aşağıdaki bilgi hatalı çünkü tek tırnak olduğu için birden fazla satıra bilgi giremeyiz.
# print("
# dshdıhoa
# ")

# \n, \t, \\, \', \" Kullanımları:

print("\nKullanmak istiyorum")
print("\\7nNasıl Kullanılır")

print("İçeride \"Çift Tırnak Kullanmak\" istiyorum.")
print('Tek Tırnak İçerisinde \'Tek Tırnak Kullanmak\' istiyorum. ')
print('Django\'nun Yetenekleri:')

print("Deneme \nYandaki Bilgi \nYandaki Diğer Bilgi")
print("Deneme \tYandaki Bilgi \tYandaki Diğer Bilgi")
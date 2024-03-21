# Bos Liste Nasil Olusturulur
users = []
# users = list()
print(users)

# Icinde Bilgi Olan Liste Nasil Olusturulur?
items = [1, 2, 3, 43,]
print(items)

# List Hangi Türde Verileri Kabul Eder?
item = "Laptop"

new_items = [
    1,
    2,
    3,
    bool(""),
    bool(item),
    4,
    'item',
    5,
    6,
    "Django",
    "Pelin",
    10.11,
    item,
    bool(1), # Hoca Burda True
    bool(0), # Burada False yazmıştı ama ben böyle bir şey denedim
]

print(new_items)
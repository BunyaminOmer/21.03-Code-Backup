items = [
    "html",
    "python",
    "django",
    "css",
    "python",
    "bootstrap",
    "python",
]

# Liste içinde kaç öğe var? -> len
print(len(items))

# Liste içinde bir öğe var mı? -> in
print( "python" in items)

# item = input("Bu Egitimde Hangi Yazilim Dili Var mi Diye Sor:")
# if item in items: 
#     print(f"{item} bilgi var")
# else:
#     print("Yok")

# Liste içinde bir öğe kaç kez var? -> count
print("Kaç adet python var", items.count("python"))


# Liste içindeki öğenin yeri(index) nedir? -> index
print("python index:", items.index("python"))


# Liste içindeki öğe adlarını sil -> remove
items.remove("python")
print(items)

# Liste içindeki son öğeyi çıkar -> pop
last_item = items.pop()
print(items)
print(last_item)

# Liste içindeki x indeksli öğeyi çıkar -> pop
first_item = items.pop(0)
print(items)
print(first_item)

# Listeyi boşalt -> clear
items.clear()
print(items)

# Liste içindeki öğeleri topla
numbers = [
    1, 2, 3, 4, 5, 6
]
print(sum(numbers))

# Liste içindeki en küçük fiyat -> min
print(min(numbers))

# Liste içindeki en büyük fiyat -> max
print(max(numbers))
# List Içindeki Oğelere Erişmek
first_item, second_item, third_item = "first", "second", "third"

items = [
    first_item, 
    second_item,
    third_item,
]

print(items)
print(items[0])
print(items[1])

# List İçine Yeni Öğe Eklemek
fourth_item = 'fourth'
items.append(fourth_item)
items.append('fifth')
items.append(1)
print(items)


# list Icindeki Ogenin Icindeki Bilgiyi Degistirmek
print(len(items))
items[len(items) -1] = 'sonuncu oge'
items[-1] = 'gercekten sonuncu oge..'
print(items)

# list Icinde Belli Bir Yere Oge Eklemek
items.insert(3, "yeni oge")
items.insert(0, "en basa eklenen oge")
# ensona insert ile ekle ;)
items.insert(len(items), 'en sonnnn..')
print(items)

# List İçindeki Belli Bir Bölümü Listelemek
print(items[2:5])
print(items[2:])

# List'in İlk 3 Öğesi
print(items[:3])

# List'in son 3 Öğesi
print(items[len(items) -3 :])

# List'i Terse Çevir
print(items[::-1])
print(items)  # Değismemiş eğer değişmesini istersen eşitlemeyi unutma.. 
# items = items[::-1]

# Son Öğeye Ulaş
print(items[-1])

# STEP belirleyerek bilgileri al.. 1, 3, 5
step_items = items[::2]
print(step_items)
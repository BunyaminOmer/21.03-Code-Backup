# Liste içine list Eklemek
users = []

user_1 = ["Ayse", 1234]
user_2 = ["Hasan", 12344556]

users.append(user_1)
users.append(user_2)

print(users)

products = [
    ["laptop", "mouse", "keyboard"],
    ["monitor", "printer"],
    "headphone",
]


# List içindeki List'e Erişmek

print(products)

print(products[2]) 

print(users[1])


# List içindeki List'i Silmek

first_user = users.pop(0)

print("first_user:", first_user)
print("users:", users)


print("products:", type(products))
print("products 0. öğe", type(products[0]))
print("products 2. öğe", type(products[2]))
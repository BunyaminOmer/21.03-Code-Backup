# Test Skoru Rakamsal bilgi içermelidir
# Test Skoru 0 ila 100 arasında olmalıdır
# Test Skoru 45 altı ise kaldı
# Test Skoru 45 ve üzeri ise geçer
# Test Skoru 55 ve üzeri ise orta
# Test Skoru 75 ve üzeri ise iyi
# Test Skoru 85 ve üzeri ise pekiyi


test_score = input("Test Skorunu Giriniz: ")
result = ""

if not test_score.isnumeric():
    print("Lutfen Rakamsal Bilgi Giriniz")
elif 0 <= int(test_score) <= 100:
    test_score = int(test_score)
    if test_score >= 85:        
        result = "pekiyi"
    elif test_score >= 75:
        result = "iyi"
    elif test_score >= 55:
        result = "orta"
    elif test_score >= 45:
        result = "gecer"
    else:
        result = "kaldi"
else:
    print("Lütfen 0 ile 100 arasında bilgi giriniz")

print(result)
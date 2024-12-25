import random

sayilar = [random.randint(1, 100) for _ in range(20)]

print("Orijinal Dizi:", sayilar)

for i in range(len(sayilar)):
    for j in range(i + 1, len(sayilar)):
        if sayilar[i] > sayilar[j]:
            sayilar[i], sayilar[j] = sayilar[j], sayilar[i]


print("Küçükten Büyüğe Sıralı Dizi:", sayilar)

for i in range(len(sayilar)):
    for j in range(i + 1, len(sayilar)):
        if sayilar[i] < sayilar[j]:
            sayilar[i], sayilar[j] = sayilar[j], sayilar[i]


print("Büyükten Küçüğe Sıralı Dizi:", sayilar)
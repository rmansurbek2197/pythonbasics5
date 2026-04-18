def katta_harflar_soni(matn):
    soni = 0
    for harf in matn:
        if harf.isupper():
            soni += 1
    return soni

matn = input("Matn kiriting: ")
print(katta_harflar_soni(matn))
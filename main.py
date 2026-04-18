def katta_harflar_soni(matn):
    return sum(1 for harf in matn if harf.isupper())

matn = input("Matn kiriting: ")
print(katta_harflar_soni(matn))
def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def boish(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def daraja(a, b):
    return a ** b

def ildiz(a):
    if a < 0:
        raise ValueError
    return a ** 0.5

print("Kalkulyator")
print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")
print("5. Daraja")
print("6. Ildiz")

amal = int(input("Amalni tanlang: "))

if amal == 1:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print(qoshish(a, b))
elif amal == 2:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print(ayirish(a, b))
elif amal == 3:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print(kopaytirish(a, b))
elif amal == 4:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print(boish(a, b))
elif amal == 5:
    a = float(input("Sonni kiriting: "))
    b = float(input("Darajani kiriting: "))
    print(daraja(a, b))
elif amal == 6:
    a = float(input("Sonni kiriting: "))
    print(ildiz(a))
else:
    print("Noto'g'ri amal")
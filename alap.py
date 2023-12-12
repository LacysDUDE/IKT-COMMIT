#BMI kalkulátor

suly = float(input("Hány kg vagy?: "))
magassag = float(input("Ird be a magasságot méterben!: "))

szamolas = suly / magassag**2



print(suly," kg vagy.")
print(magassag, "méter magas vagy")
print(szamolas)

print("Táblázat")
print("Vékony | <0.68 - 0.74")
print("Normál | 0.74 - 1")
print("Túlsúly | 1 - 1.2")
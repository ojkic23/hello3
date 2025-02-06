#1 Deljivi brojevi sa 3 i 5 u razmaku od 1 do 100

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: Deljiv sa 3 i sa 5")
    elif i % 3 == 0:
        print(f"{i}: Deljiv sa 3")
    elif i % 5 == 0:
        print(f"{i}: Deljiv sa 5")
    else:
        print(i)
        
print("------------------------------------------")

#2 Funkcija koja vraća string 

def vraca_string(s):
    return s[::-1]

string = "Pozdrav ABC timu"
obrnuti_string = vraca_string(string)
print(obrnuti_string)

print("------------------------------------------")

#3 Sortiranje niza pomocu Bubble Sort algoritma

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

niz = [67, 34, 25, 12, 20, 7, 93, 47]
bubble_sort(niz)
print("Sortiran niz je:", niz)

print("------------------------------------------")

#4 Broj ponavljanja istih reci

def broj_reci(tekst):
    tekst = tekst.lower()
    reci = tekst.split()

    brojaci = {}
    
    for rec in reci:
        if rec in brojaci:
            brojaci[rec] += 1
        else:
            brojaci[rec] = 1
            
    return brojaci

tekst = "Evo jednog malo lakseg primera . Evo nema lakseg primera od ovog."
izbrojano = broj_reci(tekst)
print(izbrojano)

print("------------------------------------------")

#5 Vracanje najduze reci u nizu stringova

def najduza_rec(niz_reci):
    if not niz_reci:  
        return None
    
    najduza = max(niz_reci, key=len)
    return najduza

reci = ["pas", "crvena", "automobil", "kosarka", "industrija", "monitor"]
najduza = najduza_rec(reci)
print("Najduza rec je:", najduza)
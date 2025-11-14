liczba_strzelonych_bramek = int(input("liczba bramek:"))
bonus = 0
liczba_punktow = liczba_strzelonych_bramek * 10
if liczba_strzelonych_bramek > 10:
    bonus += 10
if liczba_strzelonych_bramek > 5:
    bonus += 5
wynik = liczba_punktow + bonus
print("wynik druzyny:", wynik)
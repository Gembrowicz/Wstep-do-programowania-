import random
Droga=random.randint(1,100)
spalanie=float(input("Podaj średnie spalanie (w litrach na 100km):"))
cena_paliwa=float(input("Podaj aktualną cene paliwa za litr:"))
spalone_paliwo=(Droga * spalanie)/100
koszt=round(spalone_paliwo * cena_paliwa,2)
print(f'Przybliżone zużycie paliwa: {spalone_paliwo}')
print(f'Przybliżony koszt podróży:{koszt} zł')
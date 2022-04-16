import math

def oblicz_pole(param=[]):
    if len(param) >= 4:
        print("Błąd: można podać maksymalnie 3 liczby")
        return 0
    else:
        if len(param) == 1:
            pole = math.pi*math.pow(param[0], 2)
            return pole
        elif len(param) == 2:
            pole = param[0] * param[1]
            return pole
        elif len(param) == 3:
            p = (param[0] + param[1] + param[2]) / 2
            czesc_wzoru =(p*(p-param[0])*(p-param[1])*(p-param[2]))
            pole = math.sqrt(czesc_wzoru)
            return pole

liczba_figur = input()

n = int(liczba_figur)

liczba_figur = [input() for figura in range(n)]

wynik = 0
lista_floatow=[]

for param_figury in liczba_figur:
    lista_stringow = param_figury.split()
    lista_floatow = [float(i) for i in lista_stringow]
    wynik += oblicz_pole(lista_floatow)
    if len(lista_floatow) >= 4:
        break

if len(lista_floatow) <= 4:
    print(round(wynik, 2))

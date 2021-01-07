print("inserire i valore per trovare l'incognita X  nella seguente equazione: ax+b=0")
primo_numero = int(input("inserire il valore di a"))
secondo_numero = int(input("inserire il valore di b"))
if primo_numero == 0 and secondo_numero == 0:
    print("indeterminata")
if primo_numero == 0 and secondo_numero>0 or secondo_numero<0:
    print("impossibile")
if primo_numero<0 or primo_numero>0 and secondo_numero == 0:
    print("X=0")
if primo_numero<0 or primo_numero>0 and secondo_numero<0 or secondo_numero>0:
    print("X=", -secondo_numero/primo_numero)
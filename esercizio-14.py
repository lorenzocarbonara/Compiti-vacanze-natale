numeri = int(input("inserire il numero di valori dei quali vuoi sapere la differenza"))
for n in range(1, numeri + 1):
    primo_numero = int(input("inserisci il primo numero "))
    secondo_numero = int(input("inserisci il secondo numero "))
    if primo_numero*secondo_numero > 10:
        if primo_numero < secondo_numero:
            print("differenza: ",secondo_numero-primo_numero)
        else:
            print("differenza: ",primo_numero-secondo_numero)
    if primo_numero*secondo_numero <= 10:
        print("somma: ", primo_numero+secondo_numero)

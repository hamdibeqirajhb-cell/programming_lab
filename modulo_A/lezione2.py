
#es1
#stampare 538 minuti in 8h:58min
def minuti_ore(minuti):
    ore = minuti // 60
    min_rimasti = minuti - ore*60
    return f"{ore}h:{min_rimasti}min"

#print(minuti_ore(538))

#es2
#quadrato e cubo
def operazioni():
    numero = int(input("Inserisci il numero: "))
    return f"quadrato: {numero**2} \ncubo: {numero**3}"

#print(operazioni())

#es3
#verifica pari o dispari
def verifica():
    numero = int(input("Inserisci il numero: "))
    if (numero % 2 == 0):
        return "pari"
    else:
        return "dispari"
    
#print(verifica())

#es4 
#stringa e lettera
def conta_lettera(stringa, lettera):
    k = 0
    for char in stringa:
        if lettera == char:
            k += 1
    return k

#print(conta_lettera("aia","0"))

#es5
def verifica_primo():
    numero = int(input("Inserisci il numero: "))
    for i in range(2,numero):
        if numero%i == 0:
            return "non primo"
    return "primo"

#print(verifica_primo())

#es6
#somma di n numeri
def sommatoria():
    somma = 0
    numero = int(input("Inserisci il numero, per fermarti inserisci 0 "))
    while(numero != 0):
        somma += numero
        numero = int(input("Inserisci il numero, per fermarti inserisci 0 "))
    return somma

#print(sommatoria())

#es7
#funzione n!
def fattoriale(n):
    fat = 1
    for i in range(1,n+1):
        fat *= i
    return fat

#print(fattoriale(2))

#es8
def triangolo(lat1, lat2, lat3):
    if not (lat1+lat2 > lat3 and lat1+lat3 > lat2 and lat2+lat3 > lat1):
        return "Non può essere un triangolo"
    if (lat1 == lat2 or lat1 == lat3 or lat2 == lat3):
        if (lat1 == lat2 == lat3):
            return "equilatero"
        else:
            return "isoscele"
    else:
        return "scaleno"
    
#print(triangolo(2,1,4))

#es9
def conta_vocali(stringa):
    vocali = "aeiou"
    k = 0
    for char in stringa:
        if char in vocali:
            k += 1
    return k

print(conta_vocali("ciao gente come va?"))
"""Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del 
parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit."""

def convert_temperature(temp,*to_fahrenheit) -> float:
    
    if len(to_fahrenheit)>0:
        if to_fahrenheit[0]==False:
            temp=((temp-32)*5/9)
    else:
        temp=(temp*(9/5)+32)
    return temp

"""Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi."""
def list_statistics(numbers: list[int]) -> list[float]:
    massimo=max(numbers)
    minimo=min(numbers)
    media=(sum(numbers)/len(numbers))
    return massimo,minimo,media

"""Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
mantenendo l'ordine originale degli elementi."""
def remove_duplicates(l) -> list:
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

"""Il codice dovrebbe stampare i numeri all'interno di una lista."""
numbers: list[int] = [1, 2, 3, 4, 5]

for i in numbers:
    print('Number:', i)

"""La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati."""
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

"""Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero 
definito threshold."""
def sum_above_threshold(numbers: list[int], threshold:float) -> int:
    somma=0
    for i in numbers:
        if i > threshold:
            somma+=i
    return somma

"""Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude."""
def check_parentheses(expression: str) -> bool:
    for i in range(0,len(expression)):
        if expression[i]=="(":
            if ")" not in expression[i:]:
                return False
    return True

"""Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali."""
def count_isolated(l:list[int]) -> int:
    if len(l)>0:
        count=0
        for i in range (1,len(l)-1):
            if l[i]!=l[i-1] and l[i]!=l[i+1]:
                count+=1
        if l[0]!=l[1]:
            count+=1
        if l[-1]!=l[-2]:
            count+=1
        return count
    else:
        return 0
    
"""Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
ritorni un nuovo insieme senza i numeri specificati nella lista."""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    original_set=list(original_set)   
    for i in elements_to_remove:
        if i in original_set:
            original_set.remove(i)
    original_set=set(original_set)
    return original_set

"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori."""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    d={}
    for i in dict1:
        d[i]=dict1[i]
    for i in dict2:
        if i in d:
            d[i]+=dict2[i]
        else:
            d[i]=dict2[i]
    return d
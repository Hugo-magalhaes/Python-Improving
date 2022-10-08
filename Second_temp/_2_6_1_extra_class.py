l1 = [1, 2, 3, 4, 5]

l2 = l1  # Sâo a mesma coisa e são afetadas simultaneamente
l3 = [v for v in l1]  # São diferentes e não são afetadas simultaneamente

l4 = [
    (x, y)
    if x != 4 else 10  # Se x = 4 então ele será 10
    for x in range(1, 11)
    for y in range(1, 4)
    if y != 2
]

string = 'Hugo Maglhães'

nova = [
    string[indice:indice + 2]
    for indice in range(len(string))
]
nova1 = [
    string[indice:indice + 3]
    for indice in range(0, len(string), 3)
]

lista = ['Hugo', 'Julia', 'Roseane', 'Milena']

# Retira a última letra, aumenta ela e soma de volta
nova_l = [f'{v[:-1]}{v[-1].upper()}' for v in lista]

coisas = [[n, n ** 2, n * 2] for n in range(1, 11)]

# Isso itera sobre a iteração
# x recece cada par de n's e y itera sobre cada x
coisas_separadas = [y for x in coisas for y in x]

print(nova_l)

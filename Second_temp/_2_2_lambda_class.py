# Dessa forma lambda é um def., mas sem um nome
a = lambda x, y: x * y

print(a(2, 3))

lista = [
    ['p2', 6],
    ['p1', 13],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]

# A função ordena o nome pelo preço, e com reverse do maior para menor
print(sorted(lista, key=lambda i: i[1], reverse=True))

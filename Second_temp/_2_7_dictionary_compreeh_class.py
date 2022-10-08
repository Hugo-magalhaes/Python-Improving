lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista}  # Mesma lógica de dict
d11 = dict(lista)

d2 = {x.upper(): y*2 for x, y in lista}

d3 = {x*2: y**2 for x, y in enumerate(range(5))}

d4 = {f'chave_{x}': x**2 for x in range(5)}
print(d4)

set1 = {x for x in range(5)}

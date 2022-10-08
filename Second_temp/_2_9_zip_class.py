from itertools import zip_longest, count

cidade = ['São Paulo', 'Belo Horizonte', 'Minas Gerais', 'Monte Carlo']
estados = ['Sp', 'BH', 'MG']

indice = count() # conta a quantidade de entradas
cidade_estados = zip(indice, cidade, estados)
# Só uni a mesma quantidade de cada lista
cidade_estados_relacionados = zip(cidade, estados)

cidade_estado = zip_longest(cidade, estados, fillvalue='Estado') # Gerador

# print(list(cidade_estados))


contador = count(5, -0.5)

for valor in contador:
    print(round(valor, 2))
    if valor <= 0:
        break

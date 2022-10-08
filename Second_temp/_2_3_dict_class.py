dicio = {'amostra': 12, 'amostra1': 15}
dicio1 = dict(amostra=12, amostra1=15)

# Chaves duplicadas recebem o último valor que ela recebe
dicio2 = {1: 'eu', 1: 'ela', 2: 'ele'}

# tuplas são aceitas como chave
dicio3 = {(1, 2, 3): 'Tupla'}

dicio['algo'] = 'adicionando'
dicio3[(1, 2, 3)] = 'Nova'
del dicio2[2]

print(dicio.get('algo'))
print(2 in dicio1)
print('amostra1' in dicio1.keys())
print(15 in dicio.values())

#  len funciona em dicionários

print(len(dicio))

for k, v in dicio.items():
    print(k, v)

clientes = {
    'cliente 1': {'nome': 'Hugo',
                  'sobrenome': 'Magalhães'
                  },
    'cliente 2': {'nome': 'Geovana',
                  'sobrenome': 'Vieira'
                  }
}

for cliente_k, cliente_v in clientes.items():
    print(f'{cliente_k}')
    for nome, sobrenome in cliente_v.items():
        print(f'\t {nome} : {sobrenome}')

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}

# São idetênticos
v = d1
# Muda os dois
v[1] = 'ab'
print(d1)
print(v)

# Copia rasa pode alteral listas dentro do dict
c = d1.copy()
c[1] = 'abc'
c['d'][0] = 'Hugo'
print(d1)
print(c)

# Apaga o último item
d1.popitem()
# soma dois dicionários
d1.update(dicio)

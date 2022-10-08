l1 = [3, 2, 3, 4, 7, 6]

ex1 = [v for v in l1]
ex2 = [2 * v for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(2)]

l2 = ['Hugo', 'Julia', 'Milena', 'Roseane']

ex4 = [v.replace('a', '@') for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave1', 'valor1')
)

ex5 = [(y, x) for x, y in tupla]

l3 = list(range(100))

ex6 = [v for v in l3 if v % 7 == 0 if v % 5 == 0]
ex7 = [v if v % 3 == 0 else 0 for v in l3]
ex8 = [v if v % 4 == 0 and v % 3 == 0 else '#' for v in l3]
print(ex8)

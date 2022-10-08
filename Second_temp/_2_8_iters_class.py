import sys
import time

lsita = [0, 2, 3, 4]  # iteravel, mas não iterador
lista = 1234
lista1 = '1234'
print(hasattr(lsita, '__iter__'))  # Assim demosntra se é um iterável
print(hasattr(lsita, '__next__'))  # Assim demosntra se é um iterador

print(sys.getsizeof(lsita))  # Quantos bytes estão seu consumidos

nome = 'Hugo '
iterador = iter(nome)

next(iterador)  # Observe que o H não repete porque o next consome as iterações
for letra in iterador:
    print(letra)

" Geradores"

gerador = (x for x in nome)

next(gerador)
next(gerador)
print()
for x in gerador:
    print(x)


def gerador():
    for n in range(10):
        yield n


g = gerador()
print(next(g))
print(next(g))

l1 = (x for x in range(5))  # Isso é um gerador
l2 = [x for x in range(5)]
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
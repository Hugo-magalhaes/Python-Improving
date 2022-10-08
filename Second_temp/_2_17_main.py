# Tem o ponto porque matplotlib é a pasta raiz, e o pyplot é a subpasta



def divide(n1, n2, formata=False):
    if format:
        return round(n1 / n2, 2)
    else:
        return n1 / n2


def multiplica(n1, n2):
    return n1 * n2


# Dessa forma este código pode ser importado sem rodar todas as funções
if __name__ == '__main__':
    print(multiplica(2, 3))
    print(divide(2, 3))

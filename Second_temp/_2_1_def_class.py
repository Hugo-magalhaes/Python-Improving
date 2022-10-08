variavel = 'Coisa'  # Variavel global


def func(*args, **kwargs):
    print(args)
    global variavel  # Isso é prática ruim
    variavel = 'Outra'  # Variavel local
    idade = kwargs['idade']  # Dessa forma se não existir dá erro
    nome = kwargs.get('nome')  # Dessa forma não dá erro
    print(idade)
    print(nome)


n1, n2, *lista = [1, 2, 3, 4, 5]
func(*lista, nome='Hugo', idade=3)
# * representa o empacotamento da lista

perguntas = {

    'pergunta 1':  {'pergunta': 'Quanto é 2 + 2?', 'escolhas': {
        'a': '1',
        'b': '2',
        'c': '4',
        'd' : '8'

        }, 'resposta certa': 'c'
    },

    'pergunta 2':  {'pergunta': 'Quanto é 3 x 3?', 'escolhas': {
        'a': '6',
        'b': '9',
        'c': '12',
        'd': '3'

        }, 'resposta certa': 'b'
    },

    'pergunta 3':  {'pergunta': 'Quanto é 49 / 7?', 'escolhas': {
        'a': '7',
        'b': '14',
        'c': '21',
        'd': '9'

        }, 'resposta certa': 'a'
    },

    'pergunta 4':  {'pergunta': 'Quanto é 8 - 7?', 'escolhas': {
        'a': '2',
        'b': '3',
        'c': '4',
        'd': '1'

        }, 'resposta certa': 'd'
    },

}

acertos = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    for rk, rv in pv['escolhas'].items():
        print(f"{rk}) {rv}")

    resposta_usuario = input('Qual sua resposta? ')

    if resposta_usuario == pv['resposta certa']:
        print('Parabéns, você acertou!')
        acertos += 1
    else:
        print('Precisa melhorar, você errou!')

qtd_perguntas = len(perguntas)
percentual = acertos/qtd_perguntas*100

if percentual > 50:
    print(f'Parabéns, Você obteve um total de {percentual}% de acerto')
else:
    print(f'Que pena, Você obteve um total de {percentual}% de acerto')
    



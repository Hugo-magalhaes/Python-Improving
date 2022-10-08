'''
Formatando valores

:s - Textos string()
:d - Inteiros int()
:f - Números com casas float()
:. - Quantidade de casas decimais
: (Caractere) (> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

< - Valor de casas adicionadas aparecem à direita do valor inserido
> - Valor de casas adicionadas aparecem à esquerda do valor inserido
^ - Valor de casas adicionadas aparecem ao centro do valor inserido

'''


num = 150
valor = 'Hugo'
print(f'{num:0>5}')
print(f'{num:0<10.2f}')
print(f'{num:0<5}')
print(f'{valor:#^10}')

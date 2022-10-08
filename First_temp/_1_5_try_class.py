
# Utilizando blocos para não houver erros

num1 = input('Diga um número: ')
num2 = input('Diga um número: ')

try:
    print(float(num1) + float(num2))
except:
    print('Não é possível calcular ')
n1 = int(input('digite o valor 1: '))
n2 = int(input('digite o valor 2: '))
n3 = int(input('digite o valor 3: '))

if n1 > n2:
    print(f'o valor {n1} é o maior')

elif n2 > n1 and n2 > n3:
    print(f'o valor {n2} é o maior')
else:
    print(f'o valor {n3} é o maior')


num1 = float(input('Entrez un nombre:'))
op = input('Entrez un opérateur')
num2 = float(input('Entrez un second nombre'))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print('Invalid operator')

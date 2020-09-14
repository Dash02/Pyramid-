a = 161
a3 = int(input('Число строк: '))

a1 = ' '
a2 = '*'

b = a // 2
c = len(a2)

for i in range(a3):
    print(a1 * b, a2 * c, a1 * b)
    b -= 1
    c += 2
#1
drinks = ["coffee", "tea"]
storage = [2, 5]
for idx in range(len(drinks)):
    print("idx: " + str(idx) + ": " + drinks[idx])
    print(drinks[idx] + " amount: " + str(storage[idx]))

#2
shopping = ({"milk": 2, "oats": 3, "banana": 2, "nuts": 20, "chesse": 5})

price = shopping.values()
total = sum(price)

if "milk" and "chesse" in shopping:
    print(str(total - total * 0.1))
else:
    print(total)

#3
products = ["a", "b", "c", "d", "f"]
prices = [1000, 20, 30, 5, 15]

x = list(zip(products, prices))
y = sum(n[1] for n in x)
z = sum(1 for n in x)



if z > 3 and y < 500:
    print(str(y - y * 0.05))
elif z > 3 and y > 500:
    print(str(y - y*0.15))
elif z < 3 and y < 500:
    print(str(y - y * 0.1))

#4
prod = {'S1222': 'sukienka trojkatna',
            'P1222': 'koszulka',
            'X212': 'konsola do gier'}

igla = 'P12'

if igla in prod:
    print('istnieje')
else:
    print(prod['P1222'])


produkty = {'SS12': {'nazwa': 'sukienka trojkatna', 'rozmiary': ['s','l','xl']},
            'P12': {'nazwa': 'spodnica','rozmiary': ['s', 'xl']}
            }

for id in produkty:
    p = produkty[id]
    rozmiary = p['rozmiary']
    print(p['nazwa'])
    for r in rozmiary:
        print(r)

#5
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    return 0


if __name__ == '__main__':
    c = calculator(1, 2, '+')
    print(c)
    d = calculator(100, 20, '-')
    print(d)
    e = calculator(5, 4, '*')
    print(e)
    f = calculator(100, 20, '/')
    print(f)
from random import randint

x = (int(input('Довжина списку = ')))
y = (int(input('Найбільше значення списку = ')))

if x == 0:
  print('Ах ти бешкетник довжина має бути більше 0, запускай ще раз!')

def Bill(a,b):
  ab = []
  for i in range(a):
	  ab.append(randint(0,b))
  return ab

list_A=Bill(x,y)


print(list_A)
from random import randint

x = (int(input('Довжина 1го списку = ')))
y = (int(input('Найбільше значення 1го списку = ')))
z = (int(input('Довжина 2го списку = ')))
w = (int(input('Найбільше значення 2го списку = ')))


if x == 0 or z==0:
  print('Ах ти бешкетник довжина має бути більше 0, запускай ще раз!')

def Bill(a,b):
  ab = []
  for i in range(a):
	  ab.append(randint(0,b))
  return ab

list_A = Bill(x,y)
list_B = Bill(z,w)

print(list_A)
print(list_B)
list_C = []
for i in list_A:
    if i in (list_C):
        continue
    for j in (list_B):
        if i == j:
            list_C.append(i)
            break
print(list_C)

if len(list_C)==0:
   print('Співпадіння не виявлені')

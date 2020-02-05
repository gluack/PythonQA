import random
a=(random.randint(0,10))
print("a=",a)
b=(random.randint(0,10))
print("b=",b)
c=(random.randint(0,10))
if a>b:
  print("Good boy")
elif a<b:
  print("Sorrow")
elif a==b:
  print("Try this one: c=",c)
  if a+b <c:
       print("Super")
  elif a+b >c:
       print("Badly")
  elif a+b==c:
       print("Страдания")
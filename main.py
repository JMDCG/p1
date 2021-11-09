a = int(input("""Please type one of theese numbers:

1: Average in python
2: Gauss' formula

  """))

if a == 1:
  i = 0
  n = []
  x = int(input("""
How many values?
  """))
  hecho = True
  for i in range(x):
    n.append(float(input("value "+str(i+1)+": ")))
  c = 0
  b = len(n)
  while b != 0:
    c += n[b-1]
    b -= 1
  print("The average is ", str(c/len(n)))
  print(n)
if a == 2:
  n = int(input("""
Count on from 1 to... """))
  b = (n*(n+1))/2
  d = []
  m = n
  while m != 0:
    d.append(str(m))
    m -= 1
  d.reverse()
  x = "+".join(d)
  if n >= 6:
    print("The sum of 1+2+3+...+"+str(n)+" is equal to "+str(b))
  elif n >= 1:
    print("The sum of", x, "is equal to "+str(int(b)))
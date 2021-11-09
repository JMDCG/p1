a = int(input("""Please type one of theese numbers:

1: Conditionals in python practice
2: Average in python

  """))

if a == 1:
  name = str(input("""
Please type your name
  """))
  age = input("""
Please type your age
  """)
  age = int(age)
  if age >= 18:
    print("""
You are able to vote
""")
  elif age >= 15:
    print("""
StopAsyncIteration
""")
  elif age >= 1:
    print("""
Hasattr
""")
  elif age == 0:
    print("")
    print("Happy birthday ", name,"!")
    print("")
  else:
    print("""
tu papa
""")

elif a == 2:
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
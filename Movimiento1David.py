print("Hello guys,"
      "today where gona do the fibonacci sequence"
      "let's gooooooooo! ")

nterms = int(input("Cuantos valores requieres? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Por favor ingresa un valor positivo")
elif nterms == 1:
   print("Secuencia fibonacci hasta: ",nterms,":")
   print(n1)
else:
   print("Serie fibonacci:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
listaNumeros = [40,75,12,80,101,102,1,21,30,18]
listaOrdenada = []

for i in range(len(listaNumeros)):
  menor = 1000
  for numero in listaNumeros:
      if numero < menor:
          menor = numero
  listaNumeros.remove(menor)
  listaOrdenada.append(menor) 
print(listaOrdenada)

#Coloca os itens da lista em ordem crescente
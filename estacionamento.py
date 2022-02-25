lista = []
opcao = -1
quantidadelista = 2
while True:
  if len(lista) < quantidadelista:
    if opcao == "1":
      veiculo = input("Nome do veículo: ")
      lista.append(veiculo) 
    elif opcao == "2":
      indice = 0
      for veiculo in lista:
        print(str(indice), " - ", veiculo )
        indice += 1
      veiculo = int(input("Qual o carro quer retirar? "))
      lista.pop(veiculo)
    elif opcao == "3":
      pass
    elif opcao == "4":
      pass
    elif opcao == "5":
      print(lista)
    elif opcao == "0":
      break
    opcao = input("Qual a opcao? ")
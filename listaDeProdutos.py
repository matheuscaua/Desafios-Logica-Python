print("0 - Sair")
print("1 - Inserir Produto")
print("2 - Soma o valor pessoal de consumo (obs: Seleciona pelo indice do item na lista!!! ) ")
listaDeCompra = []
precoItem = []
opcao = -1
totalPreco = 0
while True:
  #Aqui se insere os produtos na lista!!!!!
  if opcao == "1":
    item = input("Produto consumido pela mesa: ")
    preco = input("Preço do Produto: ")
    precoItem = [item, preco]
    listaDeCompra.append(precoItem)
 #Opção para selecionar os produtoss consumidos!!!!!
  elif opcao == "2":
      indice = 0
      print("")
      for item in listaDeCompra:
        print(str(indice), " -> ", item)
        indice+=1
      listaTemporaria = []
      while True:
        itemConsumido = input("Produtos consumidos por você (obs: Para realizar o calculo aperte '='): ")
        if itemConsumido == "=":
          break
        listaTemporaria.append(listaDeCompra[int(itemConsumido)])
      print(listaTemporaria)
      for itemConsumido in listaTemporaria: 
        totalPreco = totalPreco + float(itemConsumido[1])
      print("O valor total dos produtos consumidos por você é : ", totalPreco)
#Opção para sair!!!
  elif opcao == "0":
    print("Saindo...")
    break
 
  opcao = input("Qual opcao deseja: ")

print("------- Lista de Compras -------")
print(" 1 - Colocar item na lista")
print("--------------------------------")
print("2 - Excluir item da lista")
print("--------------------------------")
print("3 - Quantidade de itens")
print("--------------------------------")
print("4 - Listar itens")
print("--------------------------------")
print("5 - SubTotal")
print("--------------------------------")
print("0 = Sair da lista")
print("--------------------------------")

listaDeCompra = []
tamanhoListaDeCompra = 10
opcao = -1


while True:
    if opcao == "1":
        if len(listaDeCompra) < tamanhoListaDeCompra:
            #Inserir item na lista de compra
            itemLista = input("Item: ").lower()
            qtdProduto = input("Quantidade: ")
            precoProduto = float(input("Preço do Produto: "))  

            subtotal = 0
            if itemLista in listaDeCompra:
                print("Este item não será adcionado, pois já estava contido na lista!!! ")
            else:   
                detalhesItem = ["Quantidade: ",qtdProduto, "Produto:", itemLista, "Preço: ", precoProduto]
                listaDeCompra.append(detalhesItem)
                print("O item foi inserido na lista! ")
                subtotal = subtotal + precoProduto
        else:
            print("Limite de itens! ")
    
    #Remover item
    elif opcao == "2":
        indice = 0
        for detalhesItem in listaDeCompra :
            print(str(indice), "->" , detalhesItem)
            indice += 1
        detalhesItem = int(input("Digite qual item remover da lista: "))
        retornarItemLista = listaDeCompra.pop(detalhesItem)
        print("Item Removido! ")
   
    #Quantidade Itens Lista
    elif opcao == "3":
        qtdItensLista = len(listaDeCompra)
        print("A quantidade de itens é igual a ",qtdItensLista)
    
    #Lista
    elif opcao == "4":
      for detalhesItem in listaDeCompra:
        print(detalhesItem)
        if len(listaDeCompra) == 0:
          print("Lista vazia! ")
        pass
    elif opcao == "0":
        print("Saindo.....")
        break
    else:
      print("Opção Inválida!!!")

    opcao = input("Opção: ")
    
    #Parar
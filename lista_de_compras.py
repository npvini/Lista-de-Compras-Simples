lista_de_produtos = [] #inicia uma lista de produtos vazia

while True: #enquanto toda a aplicação for executada, através do "continue" e "break", a aplicação volta ao menu ou encerra a aplicação
    print ("Olá, seja bem vindo(a) à sua lista de compras!!")
    
    print ("1. Adicionar produto")
    print ("2. Remover produto")
    print ("3. Pesquisar produtos")
    print ("4. Sair do programa")
    print ()
    acao = input ("Por favor, escolha uma das opções acima: ")
    print()
    
    if acao not in ['1', '2', '3', '4']: #caso o usuário não digite nenhum desses 3 números, a operação será inválida
        print ("Opção inválida, voltando ao menu inicial.\n")
        continue

    if acao == '1':
        produto = input ("Digite o produto que quer adicionar: ")
        lista_de_produtos.append (produto) #adiciona o produto à lista
        
        print ()
        print ("KG. Quilograma")
        print ("G. Grama")
        print ("L. Litro")                   
        print ("ML. Mililitro")                  
        print ("U. Unidade")
        print ("M. Metro")
        print ("CM. Centímetro")
        print()
        
        medidas_validas = input ("Qual será a unidade de medida?: ").lower()
        print ()
        if medidas_validas in ['kg', 'g', 'l', 'ml', 'u', 'm', 'cm']: #se dentro deste colchete o usuário digitar as palavras em "", a unidade de medida será validada
            print ("O produto", produto, "na unidade de medida", medidas_validas, "foi adicionado à sua lista!\n")  
        else:
            print ("Opção inválida, tente novamente. Voltando ao menu incial.\n") #se o usuário digitar algo que não esteja no colchete da linha 34, a operação também será invalidada
            continue
                
    elif acao == '2':
         if not lista_de_produtos: #caso da linha 14, porém, no caso de não haver produto na lista
           print ("Não há produto para remover.\n")
         else:
           print (lista_de_produtos)
           remove_produto = input ("Qual produto você quer remover?: ")
           print()
           lista_de_produtos.remove(remove_produto) #através do nome do produto, será possível removê-lo
           print ("Produto removido.\n")
           print (lista_de_produtos)
           print ("A lista está vazia novamente.\n")
           continue
       
    elif acao == '3':
         if not lista_de_produtos: #caso da linha 41
            print ("A lista está vazia.\n")
         else:
            print (lista_de_produtos) #apenas exibe a lista
            print()
            continue

    else: #finaliza o programa
        print ("Obrigado por utilizar o programa.")
        break
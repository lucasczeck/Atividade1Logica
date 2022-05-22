print('Bem vindo a lanchonete do Lucas Humberto Czeck lanches')
a = ('=================Cardapio================= \n| COD |          PRODUTO        |  VALOR | \n| 100 |     Cachorro Quente     |  9,00R$| \n'
      '| 101 |  Cachorro Quente Duplo  | 11,00R$|\n| 102 |          X-Egg          | 12,00R$|\n| 103 |         X-Salada        | 12,00R$| \n'
      '| 104 |         X-Bacon         | 14,00R$|\n| 105 |         X-Tudo          | 17,00R$| \n| 200 |    Refrigerante Lata    |  5,00R$|\n| 201 |        Chá Gelado       |  4,00R$|\n'
      '==========================================\n') # Cardápio em forma de tabela
print(a) # Para exibir o cardápio
total = 0 # Deixar a variável zerada para não dar erro no somatório final
while True: # Permite repetição em caso de erro ou de adicionar mais itens
 COD = int(input('Entre com o código desejado: ')) # Para o cliente escolher o item do pedido
 if COD == 100: # Identifica qual o produto pedido e o valor
     valor = 9.00 # Valor do produto
     PRODUTO = 'Cachorro Quente' # Produto que foi pedido
 elif COD == 101:
       valor = 11.00
       PRODUTO = 'Cachorro Quente Duplo'
 elif COD == 102:
       valor = 12.00
       PRODUTO = 'X-Egg'
 elif COD == 103:
       valor = 12.00
       PRODUTO = 'X-Salada'
 elif COD == 104:
       valor = 14.00
       PRODUTO = 'X-Bacon'
 elif COD == 105:
       valor = 17.00
       PRODUTO = 'X-Tudo'
 elif COD == 200:
       valor = 5.00
       PRODUTO = 'Refrigerante'
 elif COD == 201:
       valor = 4.00
       PRODUTO = 'Chá Gelado'
 else: # Identifica um código inexistente e retorna para o começo do laço
        print('Código inválido') # Informa que o código não existe
        continue # Retorna ao começo no while em caso de código inválido
 print('Você pediu um {} no valor de R$ {:.2f}'.format(PRODUTO, valor)) # Para informar ao cliente o nome do item que foi adicionado e o valor dele
 total = total + valor # Soma sempre o total atual + o valor do último produto pedido, acumulando todos os produtos no final
 continuar = int(input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n>> ')) # Variável para poder identificar no if
 if continuar == 1: # Identifica se o cliente que pedir mais algum item
   continue # Para voltar ao começo do while quando o cliente quiser inserir mais um item no pedido
 else: # Identifica caso o cliente não quer pedir mais nada
   break # Encerra o while finalizando o pedido
print('O total a ser pago é: R${:.2f}' .format(total)) # Informa ao cliente o valor total do pedido
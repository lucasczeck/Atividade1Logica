print('Bem vindo a lanchonete do Lucas Humberto Czeck lanches')
a = ('=================Cardapio================= \n| COD |          PRODUTO        |  VALOR | \n| 100 |     Cachorro Quente     |  9,00R$| \n'
      '| 101 |  Cachorro Quente Duplo  | 11,00R$|\n| 102 |          X-Egg          | 12,00R$|\n| 103 |         X-Salada        | 12,00R$| \n'
      '| 104 |         X-Bacon         | 14,00R$|\n| 105 |         X-Tudo          | 17,00R$| \n| 200 |    Refrigerante Lata    |  5,00R$|\n| 201 |        Chá Gelado       |  4,00R$|\n'
      '==========================================\n')
print(a)
total = 0
while True:
 COD = int(input('Entre com o código desejado: '))
 if COD == 100:
     valor = 9.00
     PRODUTO = 'Cachorro Quente'
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
 else:
        print('Código inválido')
        continue
 print('Você pediu um {} no valor de R$ {:.2f}'.format(PRODUTO, valor))
 total = total + valor
 continuar = int(input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n>> '))
 if continuar == 1:
   continue
 else:
   break
print('O total a ser pago é: R${:.2f}' .format(total))
print('Olá, bem vindo a loja do Lucas Humberto Czeck')
valor = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade: '))
sub_total = valor * quantidade

if quantidade <= 9:
  desconto = 0
  porcentagemDesconto = '0%'
elif 10 <= quantidade <= 99:
  desconto = sub_total * 0.05
  porcentagemDesconto = '5%'
elif 100 <= quantidade <= 999:
  desconto = sub_total * 0.1
  porcentagemDesconto = '10%'
else:
  desconto = sub_total * 0.15
  porcentagemDesconto = '15%'

total = sub_total - desconto

print('O valor sem desconto foi: R$ {:.2f}' .format(sub_total))
print('O valor com desconto foi: R$ {:.2f} (Desconto de {})' .format(total, porcentagemDesconto))
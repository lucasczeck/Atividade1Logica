print('Seja bem-vindo a Lucas Humberto Czeck transportes!')
def dimensoesObjeto():
    global dimensoes
    while True:
      try:
       altura = int(input('Qual a altura do objeto? (em cm) '))
       comprimento = int(input('Qual o comprimento do objeto? (em cm) '))
       largura = int(input('Qual a largura do objeto? (em cm) '))
       volume = altura * largura * comprimento
       print('O volume do seu objeto é (em cm³): {:.1f}'.format(volume))
       if volume < 1000:
        dimensoes = 10
        break
       elif 1000 <= volume < 10000: 
        dimensoes = 20
        break 
       elif 10000 <= volume < 30000: 
        dimensoes = 30 
        break 
       elif 30000 <= volume < 100000: 
        dimensoes = 50 
        break 
       else:
        print('Não aceitamos objetos com dimensões tão grandes')
        print('Por favor, entre com as dimensões desejadas novamente')
       continue
      except ValueError:
       print('Você digitou alguma dimensão do objeto com valor não númerico')
       print('Por favor, entre com as dimensões desejadas novamente')

def pesoObjeto():
    global multiplicadorpeso
    while True:
      try:
       peso = int(input('Digite o peso do objeto? (em kg) '))
       if peso <= 0.1:
        multiplicadorpeso = 1
        break
       elif 0.1 <= peso < 1:
        multiplicadorpeso = 1.5
        break
       elif 1 <= peso < 10:
        multiplicadorpeso = 2
        break 
       elif 10 <= peso <= 30:
        multiplicadorpeso = 3
        break
       else:
        print('Não aceitamos objetos tão pesados')
        print('Entre com o peso desejado novamente')
       continue
      except ValueError:
       print('Você digitou um peso com valor não númerico')
       print('Entre com o peso desejado novamente')

def rotaObjeto():
    global multiplicadorrota
    while True:
      rota = input('Digite a sigla referente a rota desejada:\n CP - De Curitiba para Paranaguá\n CL - De Curitiba para Londrina\n PC - Paranaguá para Curitiba\n PL - Paranaguá para Londrina\n'
    ' LC - Londrina para Curitiba\n LP - Londrina para Paranaguá\n>>')
      if (rota == 'CP') or (rota == 'cp'):
        multiplicadorrota = 1
        break
      elif (rota == 'CL') or (rota == 'cl'):
        multiplicadorrota = 1
        break
      elif (rota == 'PC') or (rota == 'pc'):
        multiplicadorrota = 1.2
        break
      elif (rota == 'PL') or (rota == 'pl'):
        multiplicadorrota = 1.2
        break
      elif (rota == 'LC') or (rota == 'lc'):
        multiplicadorrota = 1.5
        break
      elif (rota == 'LP') or (rota == 'lp'):
        multiplicadorrota = 1.5
        break
      else:
        print('Você digitou uma rota que não exite')
        print('Por favor, entre com a rota desejada novamente')
      continue


dimensoesObjeto()
pesoObjeto() 
rotaObjeto()
total = (dimensoes*multiplicadorpeso*multiplicadorrota)
print('Total a pagar: R${:.2f} (dimensões: R${:.2f} x peso: {} x rota: {})' .format(total, dimensoes, multiplicadorpeso, multiplicadorrota))
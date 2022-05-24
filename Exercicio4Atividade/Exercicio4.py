listaPecas = []

def cadastrarPeca(codigo):
  print('O código do produto é {:03d}' .format(codigo))
  nome = input('Qual o nome da peça? ')
  fabricante = input('Qual o fabricante da peça? ')
  valor = float(input('Qual o valor da peça? '))
  dicionarioPecas = {'Código': codigo, 'Nome': nome, 'Fabricante': fabricante, 'Valor': valor}
  listaPecas.append(dicionarioPecas.copy())
    
def consultarPeca():
  while True:
    try:
      print('Você selecionou a opção de Consultar Peças')
      consulta = int(input('Escolha a opção desejada:\n1-Consultar todas as peças\n'
      '2-Consultar peças por código\n3-Consultar peças por fabricante\n'
      '4-Retornar\n>> '))

      if consulta == 1:
        print('-'*30)
        for pecas in listaPecas:
          for key, value in pecas.items():
            print('{}: {}' .format(key, value))
          print('-'*30)

      elif consulta == 2:
        try:
          consultaCodigo = int(input('Insira o código: '))
          encontrado = False
          for pecas in listaPecas:
            if(pecas['Código'] == consultaCodigo):
              encontrado = True
              print('-'*30)
              for key, value in pecas.items():
                print('{}: {}' .format(key, value))
              print('-'*30)
          if encontrado == False:
             print('-'*30)
             print('Código não encontrado')
             print('-'*30)
        except ValueError:
           print('Código inválido')

      elif consulta == 3:
        consultaFabricante = input('Insira o fabricante: ')
        encontrado = False
        for pecas in listaPecas:
          if (pecas['Fabricante'] == consultaFabricante):
            encontrado = True
            print('-'*30)
            for key, value in pecas.items():
              print('{}: {}' .format(key, value))
            print('-'*30)
        if encontrado == False:
            print('-'*30)
            print('Fabricante não encontrado')
            print('-'*30)

      elif consulta == 4:
        print('Retornando ao menu principal')
        return

      else:
        print('Opção inválida, insira uma das opções do menu')
    except ValueError:
      print('Opção inválida, insira uma das opções do menu')

def removerPeca():
  print('Você selecionou a opção de Remover Peças')
  try:
    consultaRemocao = int(input('Insira o código da peça a ser removida: '))
    encontrado = False
    for pecas in listaPecas:
      if (pecas['Código'] == consultaRemocao):
        encontrado = True
        listaPecas.remove(pecas)
        print('Peça removida com sucesso')
    if encontrado == False:
      print('Código não encontrado')
  except ValueError:
    print('Código inválido')

codigo = 0

print('Bem vindo ao controle de estoque da bicicletaria do Lucas Humberto Czeck')
while True:
 try:
   comando = int(input('Escolha a opção desejada:\n1-Cadastrar Peça\n'
   '2-Consultar Peça\n3-Remover Peça\n4-Sair\n>> '))

   if comando == 1:
    codigo = codigo + 1
    cadastrarPeca(codigo)
    continue
   elif comando == 2:
    consultarPeca()
    continue
   elif comando == 3:
    removerPeca()
    continue
   elif comando == 4:
    print('Você escolheu a opção sair, encerrando o sistema...')
    break
   else:
    print('Opção inválida, insira uma das opções do menu')
    continue
 except ValueError:
   print('Opção inválida, insira uma das opções do menu')
   continue
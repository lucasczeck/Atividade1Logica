listaPecas = [] # Lista para armazenar as peça

def cadastrarPeca(codigo): # Função para cadastrar peças (recebendo a váriavel do código)
  print('O código do produto é {:03d}' .format(codigo)) # Informa ao cliente o código da peça que é gerado
  nome = input('Qual o nome da peça? ') # Insere o nome da peça
  fabricante = input('Qual o fabricante da peça? ') # Insere o fabricante da peça
  valor = float(input('Qual o valor da peça? ')) # Insere o valor da peça
  dicionario3989019 = {'Código': codigo, 'Nome': nome, 'Fabricante': fabricante, 'Valor': valor} # Dicionário para armazenar os dados de cada peça
  listaPecas.append(dicionario3989019.copy()) # Adiciona cada dicionário para a lista de peças
    
def consultarPeca(): # Função para consultar as peças
  while True: # Para criar um loop no menu ao final de cada pesquisa
    try: # Garante que a opção selecionada no menu é válida
      print('Você selecionou a opção de Consultar Peças') # Informa ao cliente a opção selecionada
      consulta = int(input('Escolha a opção desejada:\n1-Consultar todas as peças\n'
      '2-Consultar peças por código\n3-Consultar peças por fabricante\n'
      '4-Retornar\n>> ')) # Lista de opções da função

      if consulta == 1: # Identifica que foi selecionada a opção de consultar todas as peças
        print('-'*30) # Separa as peças para melhor visualização
        for pecas in listaPecas: # Seleciona cada peça na lista de peças
          for key, value in pecas.items(): # Seleciona cada dado de cada peça individualmente
            print('{}: {}' .format(key, value)) # Retorna para o usuário todas as peças cadastradas 
          print('-'*30)

      elif consulta == 2: # Identifica que foi selecionada a opção de consultar por código
        try: # Garante que valor inserido como código é numérico
          consultaCodigo = int(input('Insira o código: ')) # Insere o código desejado para consulta
          encontrado = False # Váriavel para definir se foi encontrado uma peça com o código indicado
          for pecas in listaPecas: # Seleciona cada peça na lista de peças
            if(pecas['Código'] == consultaCodigo): # Consulta se existe uma peça na lista com o mesmo código consultado
              encontrado = True # Caso existe uma peça com esse código a váriavel se torna verdadeira
              print('-'*30) # Separação para melhor visualização
              for key, value in pecas.items(): # Seleciona os dados da peça 
                print('{}: {}' .format(key, value)) # Retorna os dados da peça selecionada ao usuário
              print('-'*30)
          if encontrado == False: # Caso não exista peça com esse código a váriavel fica em falso
             print('-'*30)
             print('Código não encontrado') # Imprime para o usuário que não existe esse código
             print('-'*30)
        except ValueError: # Identifica caso o valor digitado no código não seja um número inteiro
           print('Código inválido') # Informa o usuário que o código está inválido

      elif consulta == 3: # Identifica que foi selecionada a opção de consultar por fabricante
        consultaFabricante = input('Insira o fabricante: ') # Insere o fabricante para consulta
        encontrado = False # Váriavel para definir se foi encontrado uma ou mais peças do fabricante indicado
        for pecas in listaPecas: # Seleciona da peça na lista de peças
          if (pecas['Fabricante'] == consultaFabricante): # Consulta de existe uma ou mais peças com o fabricante digitado
            encontrado = True # Caso existe peças desse fabricante a váriavel se torna verdadeira
            print('-'*30)
            for key, value in pecas.items(): # Seleciona os dados da(s) peça(s) correspondentes
              print('{}: {}' .format(key, value)) # Retorna os dados da(s) peça(s) para o usuário
            print('-'*30)
        if encontrado == False: # Caso nenhuma peça tenha esse fabricante fica em falso
            print('-'*30)
            print('Fabricante não encontrado') # Informa o usuário que nenhuma peça corresponde ao fabricante indicado
            print('-'*30)

      elif consulta == 4: # Identifica que a opçao selecionada foi retornar ao menu principal
        print('Retornando ao menu principal') # Informa o cliente que está retornando
        return # Encerra o while retornando ao anterior

      else: # Identifica que a opção selecionada não existe
        print('Opção inválida, insira uma das opções do menu') # Informa ao usuário que a opção não é válida
    except ValueError: # Identifica que o valor inserido não foi um número inteiro
      print('Opção inválida, insira uma das opções do menu') # Informa ao usuário que a opção não é válida

def removerPeca(): # Função para remover peça
  print('Você selecionou a opção de Remover Peças') # Informa o usuário que a opção selecionada
  try: # Garante que valor inserido como código é númerico
    consultaRemocao = int(input('Insira o código da peça a ser removida: ')) # Insere o código da peça a ser removida
    encontrado = False  # Váriavel para definir se foi encontrado uma peça com o código indicado
    for pecas in listaPecas: # Seleciona as peças na lista de peça
      if (pecas['Código'] == consultaRemocao): # Identifica qual peça corresponde ao código indicado
        encontrado = True # Caso existe uma peça com esse código a váriavel se torna verdadeira
        listaPecas.remove(pecas) # Remove a peça correspondente ao código
        print('Peça removida com sucesso') # Informa ao usuário que a peça foi removida com sucesso
    if encontrado == False: # Caso não exista peça com esse código a váriavel fica em falso
      print('Código não encontrado') # Informa ao usuário que o código não foi encontrado
  except ValueError: # Identifica caso tenha sido informado um valor que não é um número inteiro
    print('Código inválido') # Informa ao usuário que o código é inválido

codigo = 0 # Zera o código

print('Bem vindo ao controle de estoque da bicicletaria do Lucas Humberto Czeck')
while True: # Cria um loop para o menu
 try: # Verifica se o comando é válido
   comando = int(input('Escolha a opção desejada:\n1-Cadastrar Peça\n'
   '2-Consultar Peça\n3-Remover Peça\n4-Sair\n>> ')) # Informa ao usuário as opções do menu

   if comando == 1: # Identifica a opção de cadastro de peças
    codigo = codigo + 1 # Gera um código único para a peça
    cadastrarPeca(codigo) # Executa a função e repassa o código
    continue # Retorna para o while após a execução da função
   elif comando == 2: # Identifica a opção de consulta de peça
    consultarPeca() # Executa a função
    continue # Retorna para o while após a execução da função
   elif comando == 3: # Identifica a opção de remover peça
    removerPeca() # Executa a função
    continue # Retorna para o while após a execução da função
   elif comando == 4: # Identifica a função sair
    print('Você escolheu a opção sair, encerrando o sistema...') # Informa o usuário que está encerrando o sistema
    break # Termina o loop do while encerrando o sistema
   else: # Identifica se a opção é inválida
    print('Opção inválida, insira uma das opções do menu') # Informa ao usuário que o código não existe
    continue # Retorna ao começo do loop para inserir um código válido
 except ValueError: # Identifica que foi inserido um valor que não é número inteiro
   print('Opção inválida, insira uma das opções do menu') # Informa ao usuáiro que o código não é válido
   continue # Retorna ao começo do loop para inserir um código válido
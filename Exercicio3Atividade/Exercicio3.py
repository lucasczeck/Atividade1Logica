print('Seja bem-vindo a Lucas Humberto Czeck transportes!') # Identificador pessoal
def dimensoesObjeto(): # Função para as dimensões do objeto
    global dimensoes # Retorna o resultado fora da função local para calcular o valor a ser pago
    while True: # Verifica excesso na dimensão do objeto
      try: # Verifica valores inválidos
       altura = int(input('Qual a altura do objeto? (em cm) ')) # Insere a altura do objeto
       comprimento = int(input('Qual o comprimento do objeto? (em cm) ')) # Insere o comprimento do objeto
       largura = int(input('Qual a largura do objeto? (em cm) ')) # Insere a largura do objeto
       volume = altura * largura * comprimento # Calcula o volume do objeto
       print('O volume do seu objeto é (em cm³): {:.1f}'.format(volume)) # Mostra ao usuário o volume do objeto
       if volume < 1000: # Define o valor a ser cobrado conforme o volume do objeto
        dimensoes = 10 # Valor a ser cobrado
        break # Encerra o while true caso a dimensão esteja dentro do padrão
       elif 1000 <= volume < 10000: 
        dimensoes = 20
        break 
       elif 10000 <= volume < 30000: 
        dimensoes = 30 
        break 
       elif 30000 <= volume < 100000: 
        dimensoes = 50 
        break 
       else: # Usado para verificar a dimensão máxima aceita
        print('Não aceitamos objetos com dimensões tão grandes') # Informa o usuário que a dimensão não é aceita
        print('Por favor, entre com as dimensões desejadas novamente') # Conduz o usuário a inserir novamente caso queira enviar um objeto menor
       continue # Reinicia a função em caso de dimensão inválida
      except ValueError: # Caso o try retorne um erro por valor inválido essa exceção é ativada
       print('Você digitou alguma dimensão do objeto com valor não númerico') # Informa ao usuário que o valor está inválido
       print('Por favor, entre com as dimensões desejadas novamente') # Conduz o usuário a inserir os dados da forma correta

def pesoObjeto(): # Função para o peso do objeto
    global multiplicadorpeso # Retorna o resultado fora da função local para calcular o valor a ser pago
    while True: # Verifica excesso no peso do objeto
      try: # Verifica valores inválidos
       peso = int(input('Digite o peso do objeto? (em kg) ')) # Insere o peso do objeto
       if peso <= 0.1: # Define o multiplicador a ser usado no valor conforme o peso
        multiplicadorpeso = 1 # Multiplicador a ser usado
        break # Encerra o while true caso o peso esteja dentro dos padrões
       elif 0.1 <= peso < 1:
        multiplicadorpeso = 1.5
        break
       elif 1 <= peso < 10:
        multiplicadorpeso = 2
        break 
       elif 10 <= peso <= 30:
        multiplicadorpeso = 3
        break
       else: # Usado para verificar o peso máximo aceito
        print('Não aceitamos objetos tão pesados') # Informa o usuário que o peso passa do limite
        print('Entre com o peso desejado novamente') # Conduz o usuário a inserir novamente caso queira enviar um objeto menor
       continue # Reinicia a função em caso de peso inválido
      except ValueError: # Caso o try retorne um erro por valor inválido essa exceção é ativada
       print('Você digitou um peso com valor não númerico') # Informa ao usuário que o valor está inválido
       print('Entre com o peso desejado novamente') # Conduz o usuário a inserir os dados da forma correta

def rotaObjeto(): # Função para a rota da entrega
    global multiplicadorrota # Retorna o resultado fora da função local para calcular o valor a ser pago
    while True: # Verifica se a rota é válida
      rota = input('Digite a sigla referente a rota desejada:\n CP - De Curitiba para Paranaguá\n CL - De Curitiba para Londrina\n PC - Paranaguá para Curitiba\n PL - Paranaguá para Londrina\n'
    ' LC - Londrina para Curitiba\n LP - Londrina para Paranaguá\n>>') # Insere a rota desejada baseado em uma tabela com as opções
      if (rota == 'CP') or (rota == 'cp'): # Verifica qual multiplicador usar no valor conforme a rota
        multiplicadorrota = 1 # Multiplicador do valor
        break # Encerra o while true caso a rota selecionada seja válida
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
      else: # Usado para verificar se o código da rota que foi inserido é válido
        print('Você digitou uma rota que não exite') # Informa o usuário que a rota não é válida
        print('Por favor, entre com a rota desejada novamente') # Conduz o usuário a verificar a rota certa
      continue # Reinicia a função em caso de rota inválida


dimensoesObjeto() # Ativa a função no programa
pesoObjeto() 
rotaObjeto()
total = (dimensoes*multiplicadorpeso*multiplicadorrota) # Calcula o valor a ser pago pelo cliente
print('Total a pagar: R${:.2f} (dimensões: R${:.2f} x peso: {} x rota: {})' .format(total, dimensoes, multiplicadorpeso, multiplicadorrota)) # Informa ao cliente o valor a ser pago e como ele foi calculado
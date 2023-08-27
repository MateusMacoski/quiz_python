# Exibe uma mensagem de boas-vindas ao quiz.
print('Seja muito bem-vindo ao quiz do Mateus!')

# Pede ao usuário se ele deseja começar o quiz.
ansewr_user = input('Quer começar?(s/n) ')

# Se a resposta não for "s", o programa se encerra.
if ansewr_user != "s":
    print('Tudo bem...\nAté mais!')
    quit()

# Inicializa a pontuação do jogador.
score = 0
# Caso contrário, o quiz começa.
print('Começando...\n Lembre-se de responder "A, B ou C" em MAIÚSCULO!')

# Pergunta 1
print('1. Quanto é 1+1?\n (A) 23\n (B) 3\n (C) 2')
ansewr_1 = input("Resposta: ")
# Verifica se a resposta da Pergunta 1 está correta e atualiza a pontuação.
if ansewr_1 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Pergunta 2
print('2. Quantas cores tem o arco-íris?\n (A) Sete\n (B) Oito\n (C) Nove\n (D) Dez')
ansewr_1 = input("Resposta: ")
# Verifica se a resposta da Pergunta 2 está correta e atualiza a pontuação.
if ansewr_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Pergunta 3
print('3. Qual é a letra que antecede a letra O no alfabeto brasileiro?\n (A) M\n (B) N\n (C) P\n (D) Q')
ansewr_1 = input("Resposta: ")
# Verifica se a resposta da Pergunta 3 está correta e atualiza a pontuação.
if ansewr_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

# Exibe a pontuação final do jogador.
print(f'Você chegou ao fim do quiz! Pontuação: {score}/3')
    
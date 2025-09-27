import random 

#cria uma lista de palavras que serão sorteadas
palavras = ['python', 'programação', 'computador', 'aula', 'variavel']


#escolhemos uma das palavras
palavra_sorteada = random.choice(palavras)
print(palavra_sorteada)

#Criamos uma string com traços que representam as letras
palavra_escondida = "-" * len(palavra_sorteada)

letras_adivinhadas = []
max_tentativas = 6


while True:
    #mostra na tela a palavra escondida
    print(palavra_escondida)

    #pedir ao jogador para digitar uma letra
    letra = input('Digite uma letra: ')

    #verificamos se a letra já foi digitada
    if letra in letras_adivinhadas:
        print('Você já digitou esta letra. Tente outra por favor!')
        continue #continue está mandando parar e continuar novamente o loop

    #verifica se digitou mesmo somente uma letra
    if len(letra) > 1 or not letra.isalpha():
        print('Entrada inválida. Digite apenas UMA letra (sem números ou símbolos).')
        continue
     
   
    #adicionar a letra a lista de letras digitada
    letras_adivinhadas.append(letra)
    print(letras_adivinhadas)

    #verificar se a letra digitada, esta na palavra sorteada
    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)#se o jogado digitou a letra a então teremos a**a
        print(palavra_escondida)       
        continue
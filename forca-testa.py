import random
lista = []
palavra = input("Selecione 6 palavras para incluir no jogo da forca: ").lower()

for i  in range(4):
    palavra = input("Selecione 6 palavras para incluir no jogo da forca: ").lower()
    lista.append(palavra)
    
print(lista)

palavra_sorteada = random.choice(palavra)

print(palavra)


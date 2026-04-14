#Exercício 9: a partir da var word = "engenharia de sofware".    se a indice da word == 'e' or 'o', continue  

i = 0
word = "engenharia de software"

while i < len(word):
  if word[i] == 'e' or word[i] == 'o':
    i += 1
    continue
  print(word[i])
  i += 1

string = input('Escreva a frase aqui: ')

#Nova string para armazenar a inversa, comecando vazia
string_inversa = ''

#Aqui inverteremos a string baseado nos indices, visto que o ultimo indice é sempre -1, e vai diminuindo um conforme vai voltando os caracteres da string.
#Por exemplo: a string 'Hello', tem como indice -1 o 'o', o indice -2 e -3 como 'l' e assim por diante.
for i in range(1, len(string) + 1):
    string_inversa += string[-i]

print(f'A string inversa é a seguinte: {string_inversa}')
#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
#programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#Aqui vamos usar sempre somar os dois anteriores pra ver se é igual:

def pertence_fibonacci(n):

    #Definir os dois primeiros termos
    a,b = 0,1

    #Ir progredindo na sequência
    while b < n:
        a,b = b, a + b


    #Testar se é igual ao numero da entrada
    if b == n:
        return True
    
    else:
        return False
    
numero = int(input("Digite um numero: "))

#Se retornar True entra aqui
if pertence_fibonacci(numero):
    print(f"O numero {numero} pertence à sequencia!")

#Senão entra aqui
else:
    print(f"O numero {numero} não pertence à sequencia!")
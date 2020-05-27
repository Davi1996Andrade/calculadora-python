#CALCULADORA EM LINGUAGEM DE PROGRAMAÇÃO PYTHON

#esse primeiro print é o nome no titulo
#o segundo pede que seja selecionada a opção
#os seguintes informam os numeros correspondentes
print('\n ----python calculator----\n---CALCULADORA EM PYTHON---\n')


print('Selecione o numero da operação desejada:')

print('SOMA - 1                SUBTRAÇÃO - 2 \nMULTIPLICAÇÃO - 3       DIVISÃO  - 4')


#Aqui estão os códigos que processam os dados
operação = input('digite a opção desejada (1,2,3,4): ')
if operação >= '5':
    print('opção inválida!')
    operação=input('digite uma opção válida(1/2/3/4):')

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
if operação == '1':
    print('o resultado da soma é:%a '%(n1+n2))

elif operação=='2':
    print('o resultado da subtração é:%a '%(n1-n2))
    #print('o resultado da subtração',n1,'-',n2' é:%a '%(n1-n2))
    
elif operação=='3':
    print('o resultado da multiplicação é:%a '%(n1*n2))
    
elif operação=='4':
    print('o resultado da divisão é:%a '%(n1//n2))
else:
    print('Você digitou opção inválida duas vezes\nObrigado por usar a calculadora do Davi')
    print('inicie o código novamente para nova operação!')
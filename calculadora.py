class Calculadora:
    def __init__(self):
        self.historico_da_calculadora = []


    def somar (self, numero1, numero2):
        numero3 = numero1 + numero2
        print(numero3)
        texto = str(numero1) + "+" + str(numero2) + "=" + str(numero3)
        self.historico_da_calculadora.append(texto)

    def subtrair (self, numero1, numero2):
        numero3 = numero1 - numero2
        print(numero3)
        texto = str(numero1) + "-" + str(numero2) + "=" + str(numero3)
        self.historico_da_calculadora.append(texto)
        

    def multiplicar (self, numero1, numero2):
        numero3 = numero1 * numero2
        print(numero3)
        texto = str(numero1) + "*" + str(numero2) + "=" + str(numero3)
        self.historico_da_calculadora.append(texto)

    def dividir (self, numero1, numero2):
        try:
            numero3 = numero1 / numero2
            print(numero3)
            texto = str(numero1) + "/" + str(numero2) + "=" + str(numero3)
            self.historico_da_calculadora.append(texto)
        except ZeroDivisionError:
            return "Não é possível dividir por zero"

    def exibir_historico (self,):
        for i in self.historico_da_calculadora:
            print(i)


calculadora = Calculadora()
condicao = 1
opcao = 0
while (condicao != 0):
    print("1-Soma \n"
    "2-Subtração \n"
    "3-Multiplicação \n"  
    "4-Divisão \n" 
    "5-Exibir Histórico \n" 
    "0-Sair \n")
    opcao = float(input("Selecione uma opção: "))

    

    if (opcao == 1):
        numero1 = float(input("Numero 1:"))
        numero2 = float(input("Numero 2:"))
        calculadora.somar(numero1, numero2)

    if (opcao == 2):
        numero1 = float(input("Numero 1:"))
        numero2 = float(input("Numero 2:"))
        calculadora.subtrair(numero1, numero2)


    if(opcao == 3):
        numero1 = float(input("Numero 1:"))
        numero2 = float(input("Numero 2:"))
        calculadora.multiplicar(numero1, numero2)
 

    if (opcao == 4):
        numero1 = float(input("Numero 1:"))
        numero2 = float(input("Numero 2:"))
        calculadora.dividir(numero1, numero2)

    if(opcao == 5):
        calculadora.exibir_historico()

    if (opcao == 0):
        condicao = opcao

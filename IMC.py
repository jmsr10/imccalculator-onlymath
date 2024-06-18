try:
    def imc(peso, altura):
        result = peso/(altura**2)


        return result

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    resultado = imc(peso,altura)
    print("O seu IMC é: ",resultado)
except TypeError:
    print("O dado informado não é um número, por favor, execute novamente.")
except ValueError:
    print("O dado informado não é um número, por favor, execute novamente.")
except ZeroDivisionError:
    print("Não é possível dividir por zero, por favor, execute novamente.")
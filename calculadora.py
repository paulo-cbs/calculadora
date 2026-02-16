"""
Calculadora Simples em Python
Suporta: +, -, *, /, **, %, //, raiz quadrada
"""

import math


def pedir_numero(prompt, anterior=None):
    """Pede um número, aceita vírgula, ponto ou '=' para usar o resultado anterior."""
    while True:
        entrada = input(prompt).strip().replace(",", ".")
        if entrada == "" and anterior is not None:
            return anterior
        if entrada in ("=", "anterior") and anterior is not None:
            return anterior
        try:
            return float(entrada)
        except ValueError:
            print("  Digite um número válido (ex: 10 ou 3,14)")


def calculadora():
    print("=" * 45)
    print("          CALCULADORA SIMPLES")
    print("=" * 45)
    print("\nEscolha a operação pelo número:")
    print("  1 - Soma (+)          2 - Subtração (-)")
    print("  3 - Multiplicação (x) 4 - Divisão (/)")
    print("  5 - Potência          6 - Raiz quadrada")
    print("  7 - Resto da divisão  8 - Divisão inteira")
    print("  0 - Sair")
    print("=" * 45)
    print("Dica: pressione Enter ou digite '=' para usar o último resultado\n")

    resultado_anterior = None

    while True:
        try:
            op = input("Operação (1-8 ou 0 para sair): ").strip()
            
            if op == "0" or op.lower() in ("s", "sair", "q", "quit"):
                print("\nAté logo!")
                break

            if op not in "12345678":
                print("  Escolha um número de 1 a 8\n")
                continue

            if op == "6":  # Raiz quadrada
                num = pedir_numero("Número: ", resultado_anterior)
                if num < 0:
                    print("  Erro: não existe raiz de número negativo!\n")
                    continue
                resultado = math.sqrt(num)
                print(f"\n  √{num} = {resultado}\n")
            else:
                n1 = pedir_numero("Primeiro número: ", resultado_anterior)
                n2 = pedir_numero("Segundo número: ", resultado_anterior)

                if op == "1":
                    resultado = n1 + n2
                    print(f"\n  {n1} + {n2} = {resultado}\n")
                elif op == "2":
                    resultado = n1 - n2
                    print(f"\n  {n1} - {n2} = {resultado}\n")
                elif op == "3":
                    resultado = n1 * n2
                    print(f"\n  {n1} × {n2} = {resultado}\n")
                elif op == "4":
                    if n2 == 0:
                        print("  Erro: divisão por zero!\n")
                        continue
                    resultado = n1 / n2
                    print(f"\n  {n1} ÷ {n2} = {resultado}\n")
                elif op == "5":
                    resultado = n1 ** n2
                    print(f"\n  {n1} elevado a {n2} = {resultado}\n")
                elif op == "7":
                    if n2 == 0:
                        print("  Erro: divisão por zero!\n")
                        continue
                    resultado = n1 % n2
                    print(f"\n  Resto de {n1} ÷ {n2} = {resultado}\n")
                elif op == "8":
                    if n2 == 0:
                        print("  Erro: divisão por zero!\n")
                        continue
                    resultado = n1 // n2
                    print(f"\n  {n1} ÷ {n2} (inteiro) = {resultado}\n")

            resultado_anterior = resultado

        except (KeyboardInterrupt, EOFError):
            print("\n\nAté logo!")
            break


if __name__ == "__main__":
    calculadora()

"""
# Operadores Aritiméticos

    + Soma

    - Subtração

    * Multiplicação

    / Divisão

    // Divisão Inteira

    % resto da divisão ou modulo

    ** Exponencial


"""

#soma

num1 = 4
soma= num1 + num1
print(F"O valor da soma é: {soma}")

print("\n")

#Subtração

Sub = num1 - 2
print(f"O valor da subtração é: {Sub}")

print("\n")

#Multiplicação

mult = num1 *num1
print(f"O valor da multiplicação é: {mult}")

print("\n")

# Divisão
div = num1 / num1
print(f"O valor da divisão é: {div}")

print("\n")
# no exemplo abaixo da divisão exata peguei outras variaveis para fins didaticos

# Divisão exata

num2 = 5
div2 = num2 // 2
resto= num2 % 2

print(f"a divisão inteira é: {div2}")

print("\n")

#Divisão com Modulo

print(f"O modulo da divisão é: {resto}")# nesse caso vai retornar 1
                                        # porque é a quantidade de numeros após
                                        # a virgula e não o valor do numero apos a virgula

print("\n")

# Exponencial

expo = num1 ** 2

print(f"O valor ao quadrado é {expo}")

"""
 Ordem procedetoria 

Em Python, assim como em muitas outras linguagens de programação, a 
ordem de precedência dos operadores aritméticos segue as regras convencionais da matemática. 
Aqui está a ordem de precedência dos operadores aritméticos em Python, da mais alta para a mais baixa:

Parênteses (): Execução de expressões dentro de parênteses primeiro.
Exponenciação ():** Cálculos exponenciais.
Multiplicação (*), Divisão (/), Divisão inteira (//), Resto da divisão (%): Executados da esquerda para a direita.
Adição (+), Subtração (-): Executados da esquerda para a direita.

"""




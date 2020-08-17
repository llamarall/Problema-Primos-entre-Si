#coding: utf-8

# Entrada dos valores
x = int(raw_input("Digite primeiro valor: "))
y = int(raw_input("Digite segundo valor: "))

# Algoritmo para calcular o MDC por Algoritmo de Euclides Recursivo
def mdc(x, y):
  if y == 0:
    return x
  else:
    return mdc(y, x%y)


# Se o MDC for 1 então são numeros entre si
if mdc(x, y) == 1:
  print("Sao primos entre si")
else:
  print("Nao sao primos entre si")


# Tempo de complexidade
# O(log y)


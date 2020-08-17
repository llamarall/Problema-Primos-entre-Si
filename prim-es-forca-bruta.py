#coding: utf-8

# Entrada dos valores
x = int(raw_input("Digite primeiro valor: "))
y = int(raw_input("Digite segundo valor: "))

aux = 0

if x > y:
  aux = y
else:
  aux = x

# Utilizando o metodo de força bruta
# Para checar o MDC dos valores
while(x % aux != 0 or y % aux != 0):
  aux = aux - 1

if aux == 1:
  print("São primos entre si")
else:
  print("Não são primos entre si")


# Tempo de complexidade
# O(aux)
# Onde aux é o max(x, y) -> o maior entre x e y
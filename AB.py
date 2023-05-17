N = int(input())

count = 0
encaixa = True

while(count < N):
  entrada = input()
  A = entrada.split()[0]
  B = entrada.split()[1]
  
  if A.endswith(B):
    print("encaixa")
  else:
    print("nao encaixa")

  count = count + 1
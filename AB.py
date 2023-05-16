N = int(input())

count = 0
encaixa = True

while(count < N):
  A = str(input())
  B = str(input())
  i = -1
  while B[i] is not B[0] and A[i] is not A[0]:
    if B[i] != A[i]:
      encaixa = False
      break
    else:
      i = i - 1
  else:
    if B[i] == B[0] or A[i] != A[0]:
      encaixa = True
    else:
      encaixa = False
  if encaixa == True:
    count = count + 1
    print("encaixa")
  else:
    count = count + 1
    print("nao encaixa")
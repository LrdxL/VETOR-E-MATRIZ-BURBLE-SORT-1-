import random

a = ("Luis Felipe da Silva Arruda")
ra = ("n8449A-3")
v1 = [random.randint(0, 1000) for i in range(50)]

v2 = [[random.randint(0, 1000) for j in range(10)] for i in range(9)]
#numeros randoms


def ArrayPrinter(array):
  for i in range(len(array)):
    print(array[i])


print(f"VETOR *DESORGANIZADO*:\n")
print("******************************************************")
print(v1)
#print do vetor em desordem
for i in range(len(v1)):
  for j in range(len(v1) - 1):
    if (v1[j] > v1[j + 1]):
      x = v1[j + 1]
      v1[j + 1] = v1[j]
      v1[j] = x
#organização do vetor e print
print("******************************************************")
print(f"\nVETOR *ORGANIZADO*:\n")
print("******************************************************")
print(v1)

print("******************************************************")
#matriz em desordem
print(f"\nMATRIZ *DESORGANIZADA*:\n")
print("******************************************************")
ArrayPrinter(v2)
print("******************************************************")
#matriz em ordem na horizontal e print ---
for i in range((len(v2) * len(v2[0]))):
  for j in range(len(v2)):
    for k in range(len(v2[0]) - 1):
      if (v2[j][k] > v2[j][k + 1]):
        x = v2[j][k + 1]
        v2[j][k + 1] = v2[j][k]
        v2[j][k] = x

print(f"\nMATRIZ ORGANIZADA NA *HORIZONTAL*:\n")
print("******************************************************")
ArrayPrinter(v2)
print("******************************************************")
#matriz em ordem na vertical e print |
for i in range((len(v2) * len(v2[0]))):
  for j in range(len(v2) - 1):
    for k in range(len(v2[0])):
      if (v2[j][k] > v2[j + 1][k]):
        x = v2[j + 1][k]
        v2[j + 1][k] = v2[j][k]
        v2[j][k] = x

print(f"\nMATRIZ *ORGANIZADA* NA VERTICAL:\n")
print("******************************************************")
ArrayPrinter(v2)
print("******************************************************")
print("ALUNO : {} ---- RA :{} ".format(a,ra))

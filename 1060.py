valores_positivos = 0

for i in range(0, 6):
  entrada = float(input())
  if entrada > 0:
    valores_positivos += 1

print ("%i valores positivos" % valores_positivos)
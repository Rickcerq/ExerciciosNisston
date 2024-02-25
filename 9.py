nomes = ['Arthur', 'Lucas', 'Ana', 'Matheus', 'Carlos']
tem_letra_a = False
for novalista in nomes:
  if novalista.startswith("a"):
    tem_letra_a = True
    break
if tem_letra_a:
  print("um dos nomes começam com 'a'")
else:
  print("nenhum nome começa com 'a'")
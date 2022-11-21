inp_str = input("Введите выражение: ")
z = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*']
a = ''
corr = False
for i in inp_str:
  if i in z:
    corr = True
    a += i
  else:
    corr = False
    break
if corr:
  print(f'{inp_str} = {eval(a)}')

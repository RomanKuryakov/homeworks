list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []

for i in list:
  if i == '+5':
    i = str(i).split('+')
    if len(i[1]) <= 2:
      if len(i[1]) < 2:
        i = f'"+0{i[1]}"'
      elif len(i[1]) == 2:
        i = f'"+{i[1]}"'
  elif i.isdigit():
    if len(i) <= 2:
      if len(i) < 2:
        i = f'"0{i}"'
      elif len(i) == 2:
        i = f'"{i}"'

  new_list.append(''.join(i))


print(*new_list)

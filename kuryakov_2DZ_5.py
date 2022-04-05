list = [6.7,5.3,15.2,6.2,12.01,22.33,54.21,5.4, 8.6,10.22,33.7,7.7,1.2,5.4,12.19,25.9,33.6, 9.8,22.21,21.23,34.22,65.30]
print(id(list))


new_price = []

for i in list:
  i = str(i).split('.')
  if len(i[0]) <= 2:
    if len(i[0]) < 2:
      i[0] = f'0{i[0]} руб'
    if len(i[0]) == 2:
      i[0] = f'{i[0]} руб'
  if len(i[1]) <= 2:
    if len(i[1]) < 2:
      i[1] = f'0{i[1]} коп,' 
    if len(i[1]) == 2:
      i[1] = f'{i[1]} коп,' 
  new_price.append(' '.join(i))

print(*new_price)

list.sort()

print(id(list))

new_price.reverse()

top_5 = new_price[0:5]

print (*top_5)
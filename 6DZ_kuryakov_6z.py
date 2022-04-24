start = input('Введите команду (Внесение/просмотр): ')

if start.lower() == 'внесение':
  with open('bakery.csv', 'r+') as bakery:
    j = input('Введите вносимую сумму: ')
    j = float(j)
    bakery.write('{}\n'.format(j))
    amount = []
    for i in bakery:
      i = i.replace('\n', '')
      i = float(i)
      amount.append(i)
    sales = sum(amount) + j
    print('Внесено. Общая сумма', sales,'руб')
    bakery.close()

    
elif start.lower() == 'просмотр':
  with open('bakery.csv', 'r') as bakery:
    amount = []
    for i in bakery:
      i = float(i)
      amount.append(i)
      print (i)
    first = float(input('Введите искомую сумму:'))
    last = float(input('Введите искомую сумму (0, если вторая сумма не нужна):'))
    if last != 0:
      if first and last in amount:
        f = amount.index(first)
        l = amount.index(last)
        total = amount[f:l+1]
        for i in total:
          print (i)
      else: 
        print ('одна из сумм не найдена')
    elif last == 0:
      if first in amount:
        f = amount.index(first)
        total = amount[f:]
        for i in total:
          print (i)
      else:
        print ('Сумма не найдена')
else:
  print('нет команды')
  
def calc_cube(num_list):
  res = list()
  for j in res:
    return j ** 3, type(j)
  return res


@calc_cube
def val_checker(one):
  def int():
    res = one()
    i = 0
    while i >= len(res):
      for j in res:
        if j is not int:
          print (j)
          i += 1
        else:
          return f'{j} не число'
          i += 1
    return res
  return int

@val_checker
def numbers():
  num = []
  while True:
    x = input()
    if x:
        num += x + " "
    else:
        break
  for i in num:
    num.remove(' ')
  return num
  print (num)


print(numbers())




  
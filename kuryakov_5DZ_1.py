def nums(stop):
  num = 0
  while num < stop:
    if num % 2 != 0:
      yield num
      num += 1
    else:
      num += 1

gen = nums(15)
for i in gen:
  print (i)
print (type(gen))
  
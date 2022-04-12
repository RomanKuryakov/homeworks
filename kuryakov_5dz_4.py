
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

def nums():
  i = 1
  while i != len(src):
    if src[i] > src[i-1]:
      yield src[i]
      i += 1
    else:
      i += 1
  
gen = nums()
for i in gen:
  print(i)
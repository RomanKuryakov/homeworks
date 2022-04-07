
numbers_list = {
  'One' : 'один',
  'Two' : 'два',
  'Three' : 'три',
  'Four' : 'четыре',
  'Five' : 'пять',
  'Six' : 'шесть',
  'Seven' : 'семь',
  'Eight': 'восемь', 
  'Nine' : 'девять',
  'Ten' : 'десять',
}


def num_translate(n):
  n = n.capitalize()
  if n in numbers_list:
    number = numbers_list[n]
    return number.capitalize()
  else:
    print(None)

print (num_translate(input()))

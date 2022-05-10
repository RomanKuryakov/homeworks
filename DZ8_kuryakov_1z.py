import re

mail = input('введите e-mail адрес: ')
valid_mail = re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', mail)
if valid_mail is None:
  print ('wrong mail')
else:
  split_mail = re.split(r'@', mail)
  username = split_mail[0]
  domain = split_mail[1]
  print ({username: domain})

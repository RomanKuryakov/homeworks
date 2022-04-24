with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
  hobbys_list = []
  for hobby in hobbies:
    hobby = hobby.replace('\n', '')
    hobbys_list.append(hobby)


with open('users.csv', 'r', encoding='utf-8') as users:
  users_list = []
  for user in users:
    user = user.replace('\n', '')
    users_list.append(user)


with open('users_hobbies.csv', 'a') as file:
  i = 0
  for user in users_list:
      if len(hobbys_list) <= len(users_list):
        if i >= len(hobbys_list):
          file.write('{}: {}\n'.format(user, None))
          break
        else:
          file.write('{}: {}\n'.format(user, hobbys_list[i]))
          i += 1
      else:
        if i > len(users_list):
          print ('code 1')
          break
        else:
          file.write('{}: {}\n'.format(user, hobbys_list[i]))
          i += 1 

print (len(hobbys_list))
print (len(users_list))


with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
  for line in file_1:
    tuple = line.split(' ')
    request_ip = tuple[0]
    request_type = tuple[5].replace('"', '')
    requested_resource = tuple[6]
    final = request_ip, request_type, requested_resource
    print (final)

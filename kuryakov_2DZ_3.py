#Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

list = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]

name_first = list[0].lower()
position_first = name_first.split()[-2]
position_first = position_first.capitalize()
name_first = name_first.split()[-1]
name_first = name_first.capitalize()
print('Привет,', name_first)
print('Должность:', position_first)

name_second = list[1].lower()
position_second = name_second.split()[-2]
position_second = position_second.capitalize()
name_second = name_second.split()[-1]
name_second = name_second.capitalize()
print('Привет,', name_second)
print('Должность:', position_second)

name_third = list[2].lower()
position_third = name_third.split()[-4] + name_third.split(
)[-3] + name_third.split()[-2]
position_third = position_third.capitalize()
name_third = name_third.split()[-1]
name_third = name_third.capitalize()
print('Привет,', name_third)
print('Должность:', position_third)

name_fourth = list[3].lower()
position_fourth = name_fourth.split()[-2]
position_fourth = position_fourth.capitalize()
name_fourth = name_fourth.split()[-1]
name_fourth = name_fourth.capitalize()
print('Привет,', name_fourth)
print('Должность:', position_fourth)

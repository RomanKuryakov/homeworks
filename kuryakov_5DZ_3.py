123tutors = [ 
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def timetable():
  i = 0
  while i < len(klasses):
    if i >= len(tutors):
      yield None, klasses[i]
      break
    else:
      for tutor in tutors:
        yield tutor, klasses[i]
        i += 1

gen = timetable()
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (type(gen))


class Car:
  def __init__(self, name, color, speed, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
    
  def go(self):
    if self.speed > 0:
      return f'{self.name} поехал'
    else:
      return f'{self.name} стоит'

  def left(self):
    return f'{self.name} повернул налево'
  
  def right(self):
    return f'{self.name} повернула направо'    
  
  def show_speed(self):
      return f'Текущая скорость {self.name} - {self.speed}'
    
    
      
  


class TownCar(Car):
  
  def __init__(self, name, color, speed, is_police):
    super().__init__(name, color, speed, is_police)
  
  def show_speed(self):
    if self.speed > 60:
      return f'{self.speed}км/ч Превышение скорости!'
    else:
      return f'{self.speed}км/ч нет превышения скорости'

class WorkCar(Car):
  
  def __init__(self, name, color, speed, is_police):
    super().__init__(name, color, speed, is_police)
  
  def show_speed(self):
    if self.speed > 40:
      return f'{self.speed}км/ч Превышение скорости!'
    else:
      return f'{self.speed}км/ч нет превышения скорости'

class SportCar(Car):
  
  def __init__(self, name, color, speed, is_police):
    super().__init__(name, color, speed, is_police)
  


class PoliceCar(Car):
  
  def __init__(self, name, color, speed, is_police):
    super().__init__(name, color, speed, is_police)
  
  def police(self):
    if self.is_police is True:
      return f'{self.name} - полицейская машина'
    else:
      return f'{self.name} не полицейская машина'
 

audi = SportCar('audiTT', 'красная', 65, None)
lada = TownCar('Lada Priora', 'фиолетовая', 0, None)
VAZ = PoliceCar('VAZ2107', 'бело-синяя', 60, True)
KAMAZ = WorkCar('Камаз', 'оранжевый', 80, None)

print(KAMAZ.left())
print(f'скорость {KAMAZ.name} - {KAMAZ.show_speed()}')
print(f'цвет {KAMAZ.name} - {KAMAZ.color}')


print(audi.right())
print(f'скорость {audi.name} - {audi.show_speed()}')
print(f'цвет {audi.name} - {audi.color}')

print(lada.go())
print(f'скорость {lada.name} - {lada.show_speed()}')
print(f'цвет {lada.name} - {lada.color}')

print(VAZ.go())
print(f'скорость {VAZ.name} - {VAZ.show_speed()}')
print(f'цвет {VAZ.name} - {VAZ.color}')
print(f'машина {VAZ.police()}')





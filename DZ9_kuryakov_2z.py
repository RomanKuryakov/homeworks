

class Road:
  def __init__(self, lenght, width):
    self._lenght = lenght
    self._width = width
    

  def calc_weight(self):
    mass_per_cm = 25
    road_cm = 5
    weight = self._lenght * self._width * mass_per_cm * road_cm
    print (f'{weight} кг')


len_wid = Road(5000, 20)

len_wid.calc_weight()




import time

class TrafficLight:
  def __init__(self, red, yellow, green):
    self.red = red
    self.yellow = yellow
    self.green = green

  def work_time(self):
    while True:
      print (f'сейчас горит {self.red} свет')
      time.sleep(7)
      print (f'сейчас горит {self.yellow} свет')
      time.sleep(2)
      print (f'сейчас горит {self.green} свет')
      time.sleep(8)

Lights = TrafficLight('красный', 'желтый', 'зеленый')

Lights.work_time()






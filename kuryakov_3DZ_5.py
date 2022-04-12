from random import choice

nouns = [
    "автомобиль",
    "лес", 
    "огонь", 
    "город", 
    "дом"]
adverbs = [
    "сегодня", 
    "вчера", 
    "завтра", 
    "позавчера", 
    "ночью"
]
adjectives = [
    "веселый",
    "яркий", 
    "зеленый", 
    "утопичный", 
    "мягкий"
]

joke_list = []

def get_jokes(n, flag=False):
  for i in range(n):
    random_nouns = choice(nouns)
    random_averbs = choice(adverbs)
    random_adjectives = choice(adjectives)
    joke = f'{random_nouns} {random_averbs} {random_adjectives}'
    joke_list_1 = []
    print (joke)
    if flag == True:
      joke_list_1 = joke.split()
      for noun in nouns:
        for fun in joke_list_1:
          if noun == fun:
            nouns.remove(noun)


      for adverb in adverbs:
        for fun in joke_list_1:
          if adverb == fun:
            adverbs.remove(adverb)


      for adjective in adjectives:
       for fun in joke_list_1:
         if adjective == fun:
           adjectives.remove(adjective)

get_jokes (n=3, flag = True)

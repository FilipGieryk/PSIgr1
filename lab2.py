# 1
# def listy (list1,list2):
#   newlist = [x for x in list1 if list1.index(x)%2==0]
#   newlist += [x for x in list2 if list2.index(x)%2==1]
#   return newlist

# print(listy(a_list,b_list))


# 2
# data_text = 'dog'

# def zwrocSlownik(data_text):
#   length = len(data_text)
#   letters = [x for x in data_text]
#   big_letters = data_text.upper()
#   small_letters = data_text.lower()
#   dictionary = {
#     'length':length,
#     'letters':letters,
#     'big_letters':big_letters,
#     'small_letters':small_letters
#   }
#   return dictionary

# print(zwrocSlownik(data_text))


# 3
# text = 'dog was found'

# def roznicaWystapien(letter,text):
#   return text.replace(letter, '')
# print(roznicaWystapien('o',text))


# 4
# def przelicz(temperature, temperature_type):
#   if(temperature_type == 'farenheit'):
#     return temperature*9/5+32
#   elif(temperature_type == 'rankine'):
#     return (temperature+273.15)*1.8
#   elif(temperature_type == 'kelvin'):
#     return temperature+273.15
#   else:
#     return 'bledna wartosc'

# print(przelicz(27,'kevin'))


# 5
# class Calculator:

#   def __init__(self, number1,number2):
#     self.number1 = number1
#     self.number2 = number2
#   def add(self):
#     return self.number1 + self.number2
#   def difference(self):
#     return self.number1 - self.number2
#   def multiply(self):
#     return self.number1 * self.number2
#   def divide(self):
#     return self.number1 / self.number2

# ss = Calculator(2,3)
# print(ss.difference())

# 6
# class ScienceCalculator(Calculator):
#   def potegowanie(self):
#     return self.number1**self.number2

# sss = ScienceCalculator(2,4)
# print(sss.potegowanie())

# 7
# def odTylu(word):
#   return word[::-1]

# print(odTylu('hej'))

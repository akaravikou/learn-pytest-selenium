# value = ['samsung', 'Samsung', 'samsung', 'samsung', 'samsung']
#
# word = 'samsung'
#
# # for wrd in value:
# #     newas = wrd.lower()
# #     print(newas)
#
#
# mapa = list(map(lambda x: x.lower(), value))
# print(mapa)
# mapa2 = list(filter(lambda x: word in x, mapa))
# print(mapa2)
# answer = True if mapa.__sizeof__() == mapa2.__sizeof__() else False
# print(answer)

vals = ['samsung', 'samsung', 'SAMSUNG', 'SamSunG']

word = 'samsung'


def check_value_in_list(value, list_of_values):
    lower_list = list(map(lambda x: x.lower(), list_of_values))
    list_of_containing_values = list(filter(lambda x: value in x, lower_list))
    return True if len(list_of_values) == len(list_of_containing_values) else False



answer = check_value_in_list(word, vals)
print(answer)

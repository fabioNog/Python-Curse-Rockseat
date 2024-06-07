my_dictionary = {"name": "Fabio","idade": 20, "cidade": "SaoPaulo"}

print(my_dictionary["name"])


del my_dictionary["cidade"]

print(my_dictionary)

my_dictionary["skill"] = "javascript"

print(my_dictionary)


chaves = my_dictionary.keys()

print(chaves)


keys = list(my_dictionary.keys())

print(keys)


values = my_dictionary.values()

print(values)


item = list(my_dictionary.items())

print(item)

print("%s = %s " % (item[0][0],item[0][1]))

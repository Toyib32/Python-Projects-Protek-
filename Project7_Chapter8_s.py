hargaBuah = {"Apel" : 5000,
        "Jeruk" : 8500,
        "Mangga" : 7800,
        "Duku" : 6500}
def termahal (dictionary) :
    key  = list (dictionary.keys())
    values = tuple (dictionary.values())

    hargaMahal = max (values)

    indexhargaMahal = values.index(hargaMahal)

    print (key[indexhargaMahal])

termahal (hargaBuah)

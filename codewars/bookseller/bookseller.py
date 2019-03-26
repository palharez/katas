# Modelo será n
# Valor da modelo será n + 1

def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ""
    arraysOfArt = [n.split(" ") for n in listOfArt]
    priceClassified = {n: 0 for n in listOfCat}
    for arrayOfArt in arraysOfArt:
        classifiedOfArt = arrayOfArt[0][0]
        if classifiedOfArt in listOfCat and classifiedOfArt in priceClassified:
            priceClassified[classifiedOfArt] +=  int(arrayOfArt[1])
    return ' - '.join([f"({k} : {v})" for k, v in priceClassified.items()])


def test_stock_list():
    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    assert stock_list(b, c) == "(A : 200) - (B : 1140)"



if __name__ == "__main__":
    test_stock_list()
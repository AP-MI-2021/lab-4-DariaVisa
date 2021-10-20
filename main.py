def citire_date1():
    """
Citim o lista 1 de numere intregi
    :return: lista 1
    """
    lista1 = []
    lst1 = input("Notati elementele listei 1 si separati-le prin virgula: ")
    lst1_separata = lst1.split(",")
    for n in lst1_separata:
        lista1.append(int(n))
    return lista1


def citire_date2():
    """
Citim o lista 2 de numere intregi
    :return: lista 2
    """
    lista2 = []
    lst2 = input("Notati elementele listei 2 si separati-le prin virgula: ")
    lst2_separata = lst2.split(",")
    for n in lst2_separata:
        lista2.append(int(n))
    return lista2


def check_list_for_equal_even_nr(lst1, lst2):
    """
Determinam daca listele 1 si 2 au acelasi numar de elemente pare
    :param lst1: lista 1
    :param lst2: lista 2
    :return: True daca au acelasi numar de elemente pare, False daca nu
    """
    count1 = 0
    count2 = 0
    for element in lst1:
        if element % 2 == 0:
            count1 += 1
    for element in lst2:
        if element % 2 == 0:
            count2 += 1
    if count1 == count2:
        return True
    return False


def test_check_list_for_equal_even_nr():
    assert check_list_for_equal_even_nr([1, 2, 3], [1, 4, 5]) is True
    assert check_list_for_equal_even_nr([2, 4, 6], [1, 3, 5]) is False
    assert check_list_for_equal_even_nr([1, 2, 3], [1, 3, 5]) is False


def list_intersection(lst1, lst2):
    """
Intersectia listelor
    :param lst1: lista 1
    :param lst2: lista 2
    :return: lista intersectata cu elementele care se afla si in lista 1 si in lista 2
    """
    lista_intersectata = []
    if len(lst1) > len(lst2):
        for element in lst1:
            if element in lst2:
                lista_intersectata.append(element)
    else:
        for element in lst2:
            if element in lst1:
                lista_intersectata.append(element)
    return lista_intersectata


def test_list_intersection():
    assert list_intersection([12, 22, 36, 424], [22, 23, 36, 55, 424]) == [22, 36, 424]
    assert list_intersection([1, 2, 3, 4], [5, 6, 7]) == []
    assert list_intersection([12, 23, 25], [12, 23, 25]) == [12, 23, 25]


def palindrom_concatenare(lst1, lst2):
    """
Determinam palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste.
    :param lst1: lista 1
    :param lst2: lista 2
    :return: lista cu palindroamele concatenate
    """
    lista_concatenata = []
    if len(lst1) < len(lst2):
        limita = len(lst1)
    else:
        limita = len(lst2)
    for i in range(limita):
        numar = str(lst1[i]) + str(lst2[i])
        if numar == numar[::-1]:
            lista_concatenata.append(int(numar))
    return lista_concatenata


def test_palindrom_concatenare():
    assert palindrom_concatenare([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert palindrom_concatenare([1, 12, 2], [1, 3]) == [11]


def get_list_mirror_if_all_elements_divisible(lst1, lst2, lst3):
    """
Citiți o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite la punctul 1 a
tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile
cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.
    :param lst1: lista 1
    :param lst2: lista 2
    :param lst3: lista 3
    :return: doua liste finale
    """
    lista_finala1 = []
    lista_finala2 = []
    for element in lst1:
        div = True
        for i in lst3:
            if element % i == 0:
                div = False
                break
            if div == True:
                lista_finala1.append(str(element)[::-1])
            else:
                lista_finala1.append(str(element))
    for element in lst2:
        div = True
        for i in lst3:
            if element % i == 0:
                div = False
                break
            if div == True:
                lista_finala2.append(str(element)[::-1])
            else:
                lista_finala2.append(str(element))
    return [lista_finala1, lista_finala2]


def test_get_list_mirror_if_all_elements_divisible():
    assert get_list_mirror_if_all_elements_divisible([12, 22, 36, 363], [22, 23, 36, 55, 363], [1, 2, 3, 4]) == [[21, 22, 63, 363], [22, 23, 63, 55, 363]]


def main():
    test_check_list_for_equal_even_nr()
    test_list_intersection()
    test_palindrom_concatenare()
    test_get_list_mirror_if_all_elements_divisible()
    lst1 = []
    lst2 = []
    while True:
        print("1.Citirea a două mulțimi de numere întregi de la tastatura sub forma a două liste.")
        print("2.Afișați dacă cele două liste au același număr de elemente pare.")
        print("3.Afișați o listă reprezentând intersecția listelor citite de la tastatură.")
        print("4.Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste.")
        print("5.Citiți o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.")
        print("x.Iesire")
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            lst1 = citire_date1()
            lst2 = citire_date2()
        elif optiune == "2":
            print(check_list_for_equal_even_nr(lst1, lst2))
        elif optiune == "3":
            print("Intersectia listelor 1 si 2 este: ")
            print(list_intersection(lst1, lst2))
        elif optiune == "4":
            print("Palindroamele concatenate sunt: ")
            print(palindrom_concatenare(lst1, lst2))
        elif optiune == "5":
            print()
        elif optiune == "x":
            lst3 = input("Alegeti lista 3").split(",")
            get_list_mirror_if_all_elements_divisible(lst1, lst2, lst3)
        else:
            print("Reincercati!")


if __name__ == "__main__":

    main()
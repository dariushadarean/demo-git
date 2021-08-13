def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Retuneaza stringul
    :param string: un string care va fi structurat
    :returns: stringul fara spatii si cu prima litera mare
    """
    new_string = string.strip()  # elimina spatiile de la inceput si sfarsit
    new_string = new_string.capitalize()
    return new_string


def add(first, second):
    """Adds two values
    Parameters:
        first: primu parametru care va fi adunat
        second: al doilea parametru care va fi adunat
    Returns:
        suma celor doi parametri
    """
    return first + second


print(cleanup("   text de transformat "))
print(cleanup('teST'))
print(cleanup(" un Text"))
print(cleanup("  un text de schimbat in functia cleanup"))
print(cleanup.__doc__)
help(cleanup)
help(add)
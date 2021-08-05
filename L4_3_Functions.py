def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Retuneaza stringul
    """
    new_string = string.strip()
    new_string = new_string.capitalize()
    return new_string


print(cleanup("   text de transformat "))
print(cleanup('teST'))
print(cleanup(" un Text"))

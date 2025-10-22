from operators import operateurs

nombre = [str(x) for x in range(0,10)]

def is_correct(saisie):
    if saisie == "":
        return False
    if len(saisie) >= 2 and saisie[0] == '-':
        saisie = saisie[1:]
    is_int = True
    for char in saisie:
        if not char in nombre:
            is_int = False
    if is_int:
        return True
    elif saisie in operateurs:
        return True
    elif saisie == 'q':
        return True
    else:
        return False
    
if "__main__" == __name__:
    print("---------------- Saisie Correctes ----------------")
    saisie = "123"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "x"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "+"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "-"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = ":"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "q"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "abc"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "bv67"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "-123"
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = ""
    print(f"{saisie} : {is_correct(saisie)}")
    saisie = "12-3"
    print(f"{saisie} : {is_correct(saisie)}")

def translation(phrase):
    import random
    slova = phrase.split()
    vysledok = []
    vowels = "aeiouy"
    for slovo in slova:
        preklad = ""
        for znak in slovo:
            if znak in vowels:
                preklad+=znak*3
            else:
                preklad+=znak+random.choice("aeiouy")
        vysledok.append(preklad)
    return " ".join(vysledok)
print(translation("sos aaa"))

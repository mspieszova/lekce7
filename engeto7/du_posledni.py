from pprint import pprint
from collections import namedtuple

Klient = namedtuple('Klienti', field_names=['krestni_jmeno',
                                            'prijmeni',
                                            'email',
                                            'vek'])
vsichni_klienti = (
    Klient(krestni_jmeno='Matouš', prijmeni='Holinka', email='matous@holinka.com', vek=30),
    Klient(krestni_jmeno='Lukáš', prijmeni='Holinka', email='lukas.holinka@gmail.com', vek=20),
    Klient(krestni_jmeno='Petr', prijmeni='Svetr', email='psvetr@email.cz', vek=16),
    Klient(krestni_jmeno='Marek', prijmeni='Párek', email='parekm@seznam.cz', vek=14)
    )
print(type(vsichni_klienti))
def vyber_plnolete_klienty(klient):
    """funkce vybírá pouze plnoleté klienty
    :parametr klient:tuple s klienty
    :type klient: tuple
    :return:tuple s plnoletými klienty
    rtype:tuple
    """
    vybrany_klient=[]
    for klient in klient:
        if klient.vek > 18:
            vybrany_klient.append(klient.krestni_jmeno+klient.prijmeni)
    vybrany_klient=tuple(vybrany_klient)
    return vybrany_klient
print(vyber_plnolete_klienty(vsichni_klienti))

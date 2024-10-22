krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)

def XYZ(udaje):
    udaje_ocistene=list(udaje)
    for udaj in udaje_ocistene:
        if udaj is None:
            udaje_ocistene.remove(udaj)
    udaje_ocistene_tuple=tuple(udaje_ocistene)        
    return(udaje_ocistene_tuple)
print(XYZ(krestni_jmena))
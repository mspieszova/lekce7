#%% md


byty_k_prevodu="""
byt0001,Olomouc,ul.Heyrovského,
byt0003,Olomouc,ul.Novosadský_dvůr,
"""
#zadáno uživatelem
def prevod_byty(byty):
    """

    :param byty: string s parametry bytů
    :type byty: str
    :return: string s byty dopněnými o dispozice
    :rtype: str
    """
    vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }
    byty_k_prevodu_split = byty.splitlines()
    byty_k_prevodu = [byt.strip(",") for byt in byty_k_prevodu_split if byt.strip()]
    byty_list = [byt.split(",") for byt in byty_k_prevodu]
    byty_list_updated = [[vzor.get(byty[0], byty[0])] + byty[1:] for byty in byty_list]
    return "\n".join([", ".join(byt) for byt in byty_list_updated])
print(prevod_byty(byty_k_prevodu))

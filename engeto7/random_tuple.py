def vyskyt_slova(veta):
    vyskyt=dict()
    for slovo in veta:
        vyskyt[slovo]=vyskyt.setdefault(slovo,0)+1
    return(vyskyt)
print(vyskyt_slova("ahoj mami a tati"))    




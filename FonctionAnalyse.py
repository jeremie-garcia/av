#Diverse fonctions pour l'analyse du Signal
def ListeNormalisée(L):
    '''retourne une liste de grandeur normalisée entre 0 et 1 si L ne contient que des grandeurs positives'''
    maximum = (max(L))
    minimum = (min(L))
    n = len(L)
    F = [] #on initialise la liste finale
    for i in range(L):
        F.append((L[i] - minimum) / (maximum - minimum)) #normalise entre 0 et 1
    return F
#
def PasseBas(L, fc):
    '''L doit être une liste où chaque instant i contient un dictionnaire avec une clé freq pour fréquence et rms
    fc est la fréquence de coupure et on donne un rms nul à toute fréquence supérieure'''
    n = len(L)
    F = [] #on intialise la liste finale
    for i in range(n):
        F.append(L[i])
        if L[i]['freq'] > fc :
            F[i]['rms'] == 0 #on annule la puissance
    return F
#
def PasseHaut(L, fc):
    '''L doit être une liste où chaque instant i contient un dictionnaire avec une clé freq pour fréquence et rms
    fc est la fréquence de coupure et on donne un rms nul à toute fréquence inférieur'''
    n = len(L)
    F = [] #on intialise la liste finale
    for i in range(n):
        F.append(L[i])
        if L[i]['freq'] < fc :
            F[i]['rms'] == 0 #on annule la puissance
    return F
#

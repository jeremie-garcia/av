#Diverse fonctions pour l'analyse du Signal
def ListeNormalisée(M):
    '''retourne une liste de grandeur normalisée entre 0 et 1 si L ne contient que des grandeurs positives'''
    L = M[0]
    maximum = (max(L))
    minimum = (min(L))
    n = len(L)
    F = [] #on initialise la liste finale
    for i in range(n):
        F.append((L[i] - minimum) / (maximum - minimum)) #normalise entre 0 et 1
    return F
#
def PasseBas(L, fc):
    '''L doit être une liste où chaque instant i contient un dictionnaire avec une clé freq pour fréquence et rms
    fc est la fréquence de coupure et on donne un rms nul à toute fréquence supérieure sans détruire L'''
    n = len(L)
    F = [] #on intialise la liste finale
    for i in range(n):
        F.append(L[i])
        if L[i]['freq'] > fc :
            F[i]['rms'] = 0 #on annule la puissance
    return F
#
def PasseHaut(L, fc):
    '''L doit être une liste où chaque instant i contient un dictionnaire avec une clé freq pour fréquence et rms
    fc est la fréquence de coupure et on donne un rms nul à toute fréquence inférieur sans détruire L'''
    n = len(L)
    F = [] #on intialise la liste finale
    for i in range(n):
        F.append(L[i])
        if L[i]['freq'] < fc :
            F[i]['rms'] = 0 #on annule la puissance
    return F
#
if __name__ == '__main__':
    L = [[1, 25, 44, 56, 75, 98, 46, 57]]
    M = ListeNormalisée(L)
    print(M)
    T = [{'rms' : 1, 'freq' : 100 * i} for i in range(10)] #On créé une liste de fréq allant de 0 à 900
    print('T=',T)
    S = PasseBas(T, 500)
    print('S=',S)
    S = PasseHaut(T, 500)
    print('S=',S)
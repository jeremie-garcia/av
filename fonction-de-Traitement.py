
def Traitement(L,l):

    '''L est la liste contenant pour chaque instant i un dictionnaire( envoyée par Maxence) et l est le dictionnaire de configuration(envoyé par Laurent).
        La fonction crée une liste de dictionnaires qui associent à chaque clé de l (gradation, color) les valeurs correspondantes  pour tous les temps'''

    traducteur= {}

    for cle,valeur in l.items():
        traducteur[valeur]=cle

    sortie = []

    for i in range(len(L)): #On parcourt L pour s'occuper des dictionnaires un par un

        dico_i =L[i] #Correspond à chaque dictionnaire pour tous les temps i
        dico_i_bis = {} # Correpond aux nouveaux dictionnaires ajoutés dans la nouvelle liste sortie


        for cle1, valeur in dico_i.items():
            cle2 = traducteur[cle1]
            dico_i_bis[cle2]= valeur
        sortie.append(dico_i_bis)

    return(sortie)

L=[{"centroide":3 , "rms":7 } , {"centroide":3, "rms":6} ]
l={"color": "centroide" , "size":"rms"}


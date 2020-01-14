import main, config
import numpy as np

def Traitement(L,l):

    '''L est la liste contenant un dictionnaire de valeurs pour chaque instant i (envoyé par Maxence) et l est le dictionnaire de configuration(envoyé par Laurent).
        La fonction crée une liste de dictionnaires qui associent à chaque clé de l (gradation, color) les valeurs correspondantes  pour tous les temps'''

    sortie = []
    main.debug("L : " + str(L))
    main.debug("l : " + str(l))

    for i in range(len(L['rms'])): #On parcourt L pour s'occuper des dictionnaires un par un
        dico_i = {x:L[x][i] for x in L.keys()} #Correspond à chaque dictionnaire pour tous les temps i
        dico_i_bis = {} # Correpond aux nouveaux dictionnaires ajoutés dans la nouvelle liste sortie
        modifiedValues = {}

        for cle, valeur in l.assiDict.items():
            if cle != "errors" and valeur not in config.SOUND_INPUTS:
                main.debug("should be a formula : {}, {}".format(cle, valeur))
                modifiedValues[cle] = formulaApplicator(valeur, L)

        for cle, valeur in l.assiDict.items():
            if cle != "errors":
                if valeur not in config.SOUND_INPUTS: #si formule -> modifiedValues
                    dico_i_bis[cle] = modifiedValues[cle][i]
                else:
                    dico_i_bis[cle] = dico_i[valeur]
        sortie.append(dico_i_bis)
    return(sortie)

def formulaApplicator(formula, L):
    main.debug("We're called to apply {} to {}".format(formula, L))
    for x in config.SOUND_INPUTS: #création des variables
        vars()[x] = np.array(L[x])
        main.debug(x, vars()[x])
    exec("a = {}".format(formula), globals(), locals()) #application formule
    result = locals()['a']
    return result.tolist()

if __name__ == "__main__":
    SOUND_INPUTS = ["sp_centroid", "rms"]
    L={'sp_centroid':[0,0.5,0.8,0.1,0.2,0.3], 'rms':[0.1,0.5,0.2,0.3,0.4,0.6], 'sp_flatness':[0,0.1,0.2,0.1,0.1,0]}
    l={'errors': [], "rect": "sp_centroid+5", "ellipse":"3*rms"}
    print(Traitement(L, l))

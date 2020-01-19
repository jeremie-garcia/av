import main, config
import numpy as np

def Traitement(donnees, configuration):

    '''donnees est la liste contenant un dictionnaire de valeurs pour chaque instant i (envoyé par Maxence) et configuration est la configuration(envoyé par Laurent).
        La fonction crée une liste de dictionnaires qui associent à chaque clé de configuration (gradation, color) les valeurs correspondantes  pour tous les temps'''

    sortie = []
    main.debug(2,"donnees : " + str(donnees))
    main.debug(2,"configuration : " + str(configuration))
    modifiedValues = {}

    for i in range(len(donnees[[x for x in donnees.keys()][0]])): #On parcourt donnees pour s'occuper des dictionnaires un par un
        dico_i = {x:donnees[x][i] for x in donnees.keys()} #Correspond à chaque dictionnaire pour tous les temps i
        dico_i_bis = {} # Correpond aux nouveaux dictionnaires ajoutés dans la nouvelle liste sortie

        for cle, valeur in configuration.assiDict.items():
            if cle != "errors":
                if valeur in configuration.varDict.keys():
                    if type(configuration.varDict[valeur]).__name__ == "Value": #si variable valeur
                        dico_i_bis[cle] = float(configuration.varDict[valeur].getValue())
                    elif type(configuration.varDict[valeur]).__name__ == "Color":
                        dico_i_bis[cle] = configuration.varDict[valeur].rgba
                elif valeur not in config.SOUND_INPUTS:
                    if cle not in modifiedValues:
                        modifiedValues[cle] = formulaApplicator(valeur, donnees, configuration)
                    dico_i_bis[cle] = modifiedValues[cle][i]
                else:
                    dico_i_bis[cle] = dico_i[valeur]
        sortie.append(dico_i_bis)
    return(sortie)

def formulaApplicator(formula, donnees, configuration):
    main.debug(2,"We're called to apply {} to {}".format(formula, donnees))

    for x in configuration.varDict:
        vars()[x] = configuration.varDict[x]

    for x in config.SOUND_INPUTS: #création des variables
        vars()[x] = np.array(donnees[x])

    exec("_ = {}".format(formula), globals(), locals()) #application formule
    result = locals()['_']
    return result.tolist()

def grad(gradation, donnee):
    Ar, Ag, Ab, Aa = gradation.A.rgba
    Br, Bg, Bb, Ba = gradation.B.rgba
    r = Ar + (Br - Ar) * donnee
    g = Ag + (Bg - Ag) * donnee
    b = Ab + (Bb - Ab) * donnee
    a = Aa + (Ba - Aa) * donnee

    return np.array([(r[i], g[i], b[i], a[i]) for i in range(len(donnee))])


if __name__ == "__main__":
    SOUND_INPUTS = ["sp_centroid", "rms"]
    donnees={'sp_centroid':[0,0.5,0.8,0.1,0.2,0.3], 'rms':[0.1,0.5,0.2,0.3,0.4,0.6], 'sp_fconfigurationatness':[0,0.1,0.2,0.1,0.1,0]}
    l={'errors': [], "rect": "sp_centroid+5", "ellipse":"3*rms"}
    print(Traitement(donnees, configuration))

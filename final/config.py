import main, config_ui, sys, random

SOUND_INPUTS = ["rms", "sp_centroid", "sp_flatness", "chroma", "zero_crossing"]
configFolder = "configs"
configExtension = ".conf"
configFileName = configFolder + "/{}" + configExtension

class Color(): #couleur
    """
    Objet de type couleur
    Trois attributs : r, g, b (valeurs de 0 à 255 en RGB)
    """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return "Color {},{},{}".format(self.r, self.g, self.b)

    def getValue(self):
        return "{},{},{}".format(self.r, self.g, self.b)

class Gradation(): #dégradé
    """
    Objet de type dégradé
    Deux attributs : A, B, deux couleurs (objets de classe color) entre lesquels on fera un dégradé linéaire
    """
    def __init__(self,  A, B):
        self.A = A
        self.B = B

    def __repr__(self):
        return "Gradation from {} to {}".format(self.A, self.B)

    def getValue(self):
        return "{},{}".format(self.A, self.B)

class Configuration():
    def __init__(self, id, name, assiDict = {}, varDict = {}):
        self.id = id
        self.name = name
        self.assiDict = assiDict
        self.varDict = varDict

    def __repr__(self):
        return "Configuration {}: {} ; {}".format(self.name, self.assiDict, self.varDict)

def readfile(file):
    """
            file (str) : chemin du fichier de configuration que l'on souhaite ouvrir
            retourne :
                - binds : dictionnaire tel que binds[sortie] = entree ou binds[sortie] = formule
                - variables : dictionnaire tel que variables[nom] = objet ou valeur
        """
    binds = {"errors": []}
    variables = {}

    try:
        id = int(file.split("/")[-1].split(".")[0])
    except:
        return "Uncompatible file : {}".format(file)

    with open(file) as f:
        for i, l in enumerate(f):
            if i == 0:
                confName = l[:-1]
            else:
                words = l.split()
                if words[0] == "assign": #assignation
                    try: binds[words[-1]] = "".join(words[1:words.index("to")])
                    except:
                        main.debug("LINE ERROR (assi) : {}".format(l))
                        binds["errors"].append(i+1)
                elif words[0] == "var": #délaration var
                    if "color" in l: #déclaration de couleur
                        r, g, b = words[-1].split("(")[-1][:-1].split(",") #récupération des trois couleurs
                        r, g, b = int(r), int(g), int(b)
                        if not(0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                            main.debug("LINE ERROR (var color): {}".format(l))
                            binds["errors"].append(i+1)
                        variables[words[1]] = Color(r,g,b)

                    elif "grad" in l: #déclaration de dégradé
                        A, B = words[-1].split("(")[-1][:-1].split(",") #récupération deux couleurs
                        if not(A in variables.keys() and B in variables.keys()):
                            main.debug("LINE ERROR (var deg) : {}".format(l))
                            main.debug(variables)
                            binds["errors"].append(i+1)
                        variables[words[1]] = Gradation(A,B)

    return Configuration(id, confName, binds, variables)

def save(window, IOConfig):
    conf = winToConf(window, IOConfig)

    with open(configFileName.format(conf.id), "w") as f:
        f.write(conf.name+"\n")
        for v in conf.varDict:
            if conf.varDict[v][0] == "value" and conf.varDict[v][0] != "":
                f.write("var {} = {}\n".format(v, conf.varDict[v][1]))
            else:
                f.write("var {} = {}({})\n".format(v, conf.varDict[v][0], conf.varDict[v][1]))
        for a in conf.assiDict:
            f.write("assign {} to {}\n".format(a, conf.assiDict[a]))

    main.debug(conf.assiDict)
    main.debug(conf.varDict)

def winToConf(window, IOConfig):
    conf = Configuration(IOConfig.currentConf, window.nomConfLine.text())

    assignations, vars = {}, {}

    for line in IOConfig.assiLines: # sortie: source
        if line.contents[1].__class__.__name__ == "QComboBox":
            assignations[line.contents[2].currentText()] = line.contents[1].currentText()
            main.debug("combo")
        else:
            assignations[line.contents[2].currentText()] = line.contents[1].displayText()
    for line in IOConfig.varLines: # nom: (type, valeur)
        name = line.contents[0].displayText()
        value = line.contents[2].displayText()
        if name != "" and value != "":
            vars[name] = (line.contents[1].currentText(), line.contents[2].displayText())

    conf.assiDict = assignations
    conf.varDict = vars

    return conf

def valider(IOConfig):
    save(IOConfig)
    main.debug("Goodbye, human")
    IOConfig.close()

if __name__ == "__main__":
    config_ui.openWindow()

import main, config_ui, sys, random

SOUND_INPUTS = ["rms", "sp_centroid", "sp_flatness", "chroma", "zero_crossing"]
configFolder = "configs"
configExtension = ".conf"
configFileName = configFolder + "/{}" + configExtension

soundsFolder = "sounds"
soundsExtension = ".wav"

class Color(): #couleur
    """
    Objet de type couleur
    Trois attributs : r, g, b (valeurs de 0 à 255 en RGB)
    """
    def __init__(self, name, r, g, b, a):
        self.name = name
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.rgba = (r,g,b,a)

    def __repr__(self):
        return "Color {},{},{},{}".format(self.r, self.g, self.b, self.a)

    def getValue(self):
        return "{},{},{},{}".format(self.r, self.g, self.b, self.a)

class Gradation(): #dégradé
    """
    Objet de type dégradé
    Deux attributs : A, B, deux couleurs (objets de classe color) entre lesquels on fera un dégradé linéaire
    """
    def __init__(self,  name, A, B):
        self.A = A
        self.B = B
        self.name = name

    def __repr__(self):
        return "Gradation from {} to {}".format(self.A, self.B)

    def getValue(self):
        return "{},{}".format(self.A.name, self.B.name)

class Value(): #valeur
    """
    Objet de type valeur
    Un attribut : name (str), value (float)
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "Value {} = {}".format(self.name, self.value)

    def getValue(self):
        return self.value

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
        print("Uncompatible file : {}".format(file))
        return None

    with open(file) as f:
        for i, l in enumerate(f):
            if i == 0:
                confName = l[:-1]
            else:
                words = l.split()
                if words[0] == "assign": #assignation
                    try: binds[words[-1]] = "".join(words[1:words.index("to")])
                    except:
                        main.debug(1,"LINE ERROR (assi) : {}".format(l))
                        binds["errors"].append(i+1)
                elif words[0] == "var": #délaration var
                    if "color" in l: #déclaration de couleur
                        r, g, b, a = words[-1].split("(")[-1][:-1].split(",") #récupération des trois couleurs
                        r, g, b, a = int(r), int(g), int(b), int(a)
                        if not(0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                            main.debug(1,"LINE ERROR (var color): {}".format(l))
                            binds["errors"].append(i+1)
                        variables[words[1]] = Color(words[1], r, g, b, a)

                    elif "grad" in l: #déclaration de dégradé
                        A, B = words[-1].split("(")[-1][:-1].split(",") #récupération deux couleurs
                        if not(A in variables and B in variables):
                            main.debug(1,"LINE ERROR (var deg) : {}".format(l))
                            main.debug(2,variables)
                            binds["errors"].append(i+1)
                        variables[words[1]] = Gradation(words[1], variables[A], variables[B])

                    else: #déclaration valeur
                        variables[words[1]] = Value(words[1], words[-1])

    return Configuration(id, confName, binds, variables)

def save(window, conf, IOConfig):
    main.debug(2,"Saving configuration #{} : {}".format(conf.id, conf))

    with open(configFileName.format(conf.id), "w") as f:
        f.write(conf.name+"\n")
        for v in conf.varDict:
            typeName = type(conf.varDict[v]).__name__
            if typeName == "Value" and conf.varDict[v].name != "":
                f.write("var {} = {}\n".format(v, conf.varDict[v].value))
            elif typeName in ["Color", 'Gradation'] and conf.varDict[v].name != "":
                _ = 'grad' if typeName == "Gradation" else 'color'
                f.write("var {} = {}({})\n".format(v, _, conf.varDict[v].getValue()))
        for a in conf.assiDict:
            f.write("assign {} to {}\n".format(conf.assiDict[a], a))

    window.confCombo.setItemText(conf.id, conf.name)
    main.initConf()
    IOConfig.configs = window.updateConfig()
    window.showConfig(IOConfig, conf.id)

    oldConfID = IOConfig.mainWindow.comboBox_2.currentIndex()
    IOConfig.mainWindow.configs = main.initConf()
    main.fillConfig(IOConfig.mainWindow)
    IOConfig.mainWindow.comboBox_2.setCurrentIndex(oldConfID)

    main.debug(2,conf.assiDict)
    main.debug(2,conf.varDict)

def winToConf(window, IOConfig):
    conf = Configuration(IOConfig.currentConf, window.nomConfLine.text())

    assignations, vars = {}, {}

    for line in IOConfig.assiLines: # sortie: source
        if line.contents[1].__class__.__name__ == "QComboBox":
            assignations[line.contents[2].currentText()] = line.contents[1].currentText()
            main.debug(2,"combo")
        else:
            assignations[line.contents[2].currentText()] = line.contents[1].displayText()
    for line in IOConfig.varLines: # nom: (type, valeur)
        name = line.contents[0].displayText()
        value = line.contents[2].displayText()
        if name != "" and value != "":
            main.debug(2, 'vars are : {}'.format(vars))
            if line.contents[1].currentText() == "value":
                vars[name] = Value(name, value)
            elif line.contents[1].currentText() == "grad":
                A, B = value.split(",")
                vars[name] = Gradation(name, vars[A], vars[B])
            elif line.contents[1].currentText() == "color":
                r, g, b, a = value.split(",")
                vars[name] = Color(name, r, g, b, a)

    conf.assiDict = assignations
    conf.varDict = vars

    return conf

def valider(win, IOConfig):
    save(win, winToConf(win, IOConfig), IOConfig)
    main.debug(1,"Saved")
    IOConfig.close()

if __name__ == "__main__":
    config_ui.openWindow()

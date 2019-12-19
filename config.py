import config_ui, sys, random

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

"""class readError():
    def __init__(self, line, error):
        self.line = line
        self.error = error

    def __repr__(self):
        return "Line {}: {}".format(self.line, self.error)"""

SOUND_INPUTS = ["rms", "sp_centroid", "sp_flatness", "sp_contrast", "sp_bandwidth", "sp_rolloff", "beat"]

def readfile(file):
    """
            file (str) : chemin du fichier de configuration que l'on souhaite ouvrir
            retourne :
                - binds : dictionnaire tel que binds[sortie] = entree ou binds[sortie] = formule
                - variables : dictionnaire tel que variables[nom] = objet ou valeur
        """
    binds = {"errors": []}
    variables = {}
    with open(file) as f:
        for i, l in enumerate(f):
            words = l.split()
            if words[0] == "assign" or words[0] == "on": #assignation ou assignation event
                try: binds[words[-1]] = "".join(words[1:words.index("to")])
                except: binds["errors"].append(i+1)
            elif words[0] == "var": #délaration var
                if "color" in l: #déclaration de couleur
                    r, g, b = words[-1].split("(")[-1][:-1].split(",") #récupération des trois couleurs
                    r, g, b = int(r), int(g), int(b)
                    if not(0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                        binds["errors"].append(i+1)
                    variables[words[1]] =  Color(r,g,b)

                elif "grad" in l: #déclaration de dégradé
                    A, B = words[-1].split("(")[-1][:-1].split(",") #récupération deux couleurs
                    if not(A in variables.keys() and B in variables.keys()):
                        binds["errors"].append(i+1)
                    variables[words[1]] = Gradation(A,B)
    return binds, variables

def save(window):
    assignations = {}
    vars = {}
    for line in window.assiLines: # sortie: source
        if line.contents[1].__class__.__name__ == "QComboBox":
            assignations[line.contents[2].currentText()] = line.contents[1].currentText()
            config_ui.debug("combo")
        else:
            assignations[line.contents[2].currentText()] = line.contents[1].displayText()
    for line in window.varLines: # nom: (type, valeur)
        name = line.contents[0].displayText()
        value = line.contents[2].displayText()
        if name != "" and value != "":
            vars[name] = (line.contents[1].currentText(), line.contents[2].displayText())

    with open("av.conf", "w") as f:
        for v in vars:
            if vars[v][0] == "value" and vars[v][0] != "":
                f.write("var {} = {}\n".format(v, vars[v][1]))
            else:
                f.write("var {} = {}({})\n".format(v, vars[v][0], vars[v][1]))
        for a in assignations:
            f.write("assign {} to {}\n".format(a, assignations[a]))

    config_ui.debug(assignations)
    config_ui.debug(vars)

def valider(IOConfig):
    save(IOConfig)
    config_ui.debug("Goodbye, human")
    IOConfig.close()

if __name__ == "__main__":
    config_ui.openWindow()

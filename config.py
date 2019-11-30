class Color(): #couleur
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return "Color {},{},{}".format(self.r, self.g, self.b)

class Gradation(): #dégradé
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

INPUTS = ["rms", "sp_centroid", "sp_flatness", "sp_contrast", "sp_bandwidth", "sp_rolloff"]
OUTPUTS = ["size", "px", "py", "vibration"]

def readfile(file):
    binds = {"errors":[]}
    variables = {}
    with open(file) as f:
        for i,l in enumerate(f):
            words = l.split()

            # reconnaissance assignation -> a to b
            # si a est une formule, on save le texte de la formule pour plus tard, à utiliser avec exec(a)
            try:
                indexto = words.index("to")

                if indexto:
                    binds[words[-1]] = "".join(words[:indexto])
                else:
                        #binds["errors"].append(readError(l, "incorrect input or output"))
                    raise NameError

            except ValueError: #si pas de to, déclaration variable
                try:
                    if l.split()[-1].split("(")[:-1][0] == "color": #déclaration de couleur
                        r, g, b = words[-1].split("(")[-1][:-1].split(",") #récupération des trois couleurs
                        r, g, b = int(r), int(g), int(b)
                        if not(0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                            #binds["errors"].append(readError(l, "out of range values for color"))
                            raise ValueError
                        variables[words[0]] =  Color(r,g,b)

                    if l.split()[-1].split("(")[:-1][0] == "grad": #déclaration de dégradé
                        A, B = words[-1].split("(")[-1][:-1].split(",") #récupération deux couleurs
                        if not(A in variables.keys() and B in variables.keys()):
                            #binds["errors"].append(readError(l, "color doesn't exist"))
                            raise ValueError
                        variables[words[0]] = Gradation(A,B)

                except ValueError:
                    binds["errors"].append(i+1) # si ligne non reconnue

            except NameError:
                binds["errors"].append(i+1) # si ligne non reconnue


    return binds, variables

if __name__ == "__main__":
    b, v = readfile("conf.ig")
    print(b)
    print(v)
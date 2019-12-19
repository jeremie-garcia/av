import main_ui, os, config

DEBUG = True

def initConf():
    try :
        confFiles = os.listdir(config.configFolder+"/")
    except:
        confFiles = None

    configs = {}

    for i,f in enumerate(confFiles):
        tmp = config.readfile(config.configFolder + "/" + f)
        try : configs[tmp.id] = tmp
        except : debug(tmp)

    return configs

def debug(*args):
    if DEBUG: print(*args)

if __name__ == "__main__":
    configs = initConf()
    main_ui.openWindow()
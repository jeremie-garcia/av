# Version modifiée d'av réorganisant les données en liste de dictionnaire
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa
import main_ui, config_interpreter, config, config_ui, FonctionAnalyse

DEBUG = 2 #0 : no message; 1: announce messages; 2: all
SYNCHRO = 0
SCALE = 300
WIDTH_SCALE = int(SCALE / 4)

class analyzedSound():
    def __init__(self, name, link, donnee_brute):
        self.name = name
        self.donnee_brute = donnee_brute
        self.link = link

    def analyzed(self):
        return True

    def getDonnee(self):
        return self.donnee_brute

class Sound():
    def __init__(self, ui, name, link):
        self.name = name
        self.link = link
        self.ui = ui

    def analyzed(self):
        return False

    def analyze(self):
        self.waveform, self.sr = librosa.load(self.link)
        debug(1,"Loaded sound")
        new = analyzedSound(self.name, self.link, normalization(extractFeatures(self.ui, self)))
        debug(1,"Finished analyze")
        return new

def showConfig(ui):
    for combo in ui.configCombos:
        config_ui.fillCombo(combo, [ui.configs[i].name for i in range(len(ui.configs.keys()))])

def initConf():
    try:
        confFiles = os.listdir(config.configFolder + "/")
    except:
        confFiles = []

    configs = {}

    for i, f in enumerate(confFiles):
        tmp = config.readfile(config.configFolder + "/" + f)
        try:
            configs[tmp.id] = tmp
        except:
            debug(1,"Erreur {}".format(tmp))

    return configs

def initSounds(ui):
    try:
        soundFiles = os.listdir("sounds/")
    except:
        soundFiles = []

    soundsObjects = {x: Sound(ui, x, config.soundsFolder + "/" + x) for x in soundFiles}

    config_ui.fillCombo(ui.comboBox, sorted(soundFiles))
    return soundsObjects


def debug(i, *args):
    if DEBUG >= i: print(*args)


def loadSound(ui, file):
    debug(1,"Loading sound {}".format(file.name))

    if file.link.split(".")[-1] != "wav":
        raise ValueError

    ui.currentSound = file

    debug(1,"Analyzing sound")
    if not file.analyzed():
        ui.currentSound = ui.currentSound.analyze()

    debug(1,"Generating movements")
    ui.movements = []
    for combo in ui.configCombos:
        conf = ui.configs[combo.currentIndex()]
        ui.movements.append(config_interpreter.Traitement(ui.currentSound.donnee_brute, conf))
    debug(1,"Movements generated")

    pygame.mixer.music.load(file.link)

    ui.timer = QtCore.QTimer()
    ui.timer.timeout.connect(lambda: timer_update(ui))

def extractFeatures(ui, sound):
    waveform, sr = sound.waveform, sound.sr
    features_frame_length = 4096
    ui.frame_duration_ms = 1000 * (512 / sr)
    rms_frames = librosa.feature.rms(y=waveform, S=None, frame_length=features_frame_length)
    spectral_centroid_frames = librosa.feature.spectral_centroid(y=waveform, sr=sr, S=None, n_fft=features_frame_length)
    spectral_flatness_frames = librosa.feature.spectral_flatness(y=waveform, S=None, n_fft=features_frame_length)
    chroma_stft_frames = librosa.feature.chroma_stft(y=waveform, S=None, n_fft=features_frame_length)
    zero_crossing_rate_frames = librosa.feature.zero_crossing_rate(y=waveform, frame_length=features_frame_length)

    return {'rms': rms_frames, 'sp_centroid': spectral_centroid_frames, \
            'sp_flatness': spectral_flatness_frames, \
            'zero_crossing': zero_crossing_rate_frames, 'chroma': chroma_stft_frames}

def normalization(donnee_brute):
    for key in donnee_brute.keys():
        donnee_brute[key] = FonctionAnalyse.ListeNormalisée(donnee_brute[key])
    return donnee_brute

def timer_update(ui):
    if (pygame.mixer.music.get_busy()):
        current_time = pygame.mixer.music.get_pos()
        # find closest frame in descriptors
        index = current_time // ui.frame_duration_ms
        index = round(min(index, len(ui.movements[0]) - 1)) + ui.horizontalSlider.value()

        for f in ui.figures:
            ui.figures[f].draw(ui.movements[int(f)][index])

    else:
        if ui.checkBox.checkState():  # si mode boucle
            ui.soundRewind()
        else:
            ui.pushButton.clicked.disconnect()
            ui.pushButton.clicked.connect(lambda: ui.soundLoadPlay())
            ui.pushButton.setText("|>")
            #for f in ui.figures:
            #    ui.figures[f].draw('reset')
            ui.timer.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = main_ui.Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    ui.configs = initConf()
    ui.configCombos = [ui.comboBox_2, ui.comboBox_3, ui.comboBox_4, ui.comboBox_5]
    showConfig(ui)
    ui.sounds = initSounds(ui)
    ui.updateSoundFile()
    pygame.mixer.init()

    filename = config.soundsFolder + "/" + ui.currentSound.name

    ui.currentConf = [ui.configs[ui.configCombos[i].currentIndex()] for i in range(len(ui.configCombos))]


    sys.exit(app.exec_())

#Version modifiée d'av réorganisant les données en liste de dictionnaire
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa
import main_ui, config_interpreter, config, config_ui, FonctionAnalyse

DEBUG = False
SYNCHRO = 0
SCALE = 300
WIDTH_SCALE = int(SCALE/4)

def showConfig(ui):
    config_ui.fillCombo(ui.comboBox_2, [ui.configs[i].name for i in range(len(ui.configs.keys()))])

def initConf():
    try :
        confFiles = os.listdir(config.configFolder+"/")
    except:
        confFiles = []

    configs = {}

    for i,f in enumerate(confFiles):
        tmp = config.readfile(config.configFolder + "/" + f)
        try :
            configs[tmp.id] = tmp
        except : debug("Erreur {}".format(tmp))

    return configs

def initSounds(ui):
    try:
        soundFiles = os.listdir("sounds/")
    except:
        soundFiles = []

    config_ui.fillCombo(ui.comboBox, sorted(soundFiles))
    return soundFiles

def debug(*args):
    if DEBUG: print(*args)

def loadSound(ui, file, conf):
    ui.pushButton.setText("Loading sound")

    if file.split(".")[-1] != "wav":
        return None

    waveform, sr = librosa.load(file)

    features_frame_length = 4096
    ui.frame_duration_ms = 1000 * (512 / sr)
    rms_frames = librosa.feature.rms(y=waveform, S=None, frame_length=features_frame_length)
    spectral_centroid_frames = librosa.feature.spectral_centroid(y=waveform, sr=sr, S=None, n_fft=features_frame_length)
    spectral_flatness_frames = librosa.feature.spectral_flatness(y=waveform, S=None, n_fft=features_frame_length)
    chroma_stft_frames = librosa.feature.chroma_stft(y=waveform, S=None, n_fft=features_frame_length)
    zero_crossing_rate_frames = librosa.feature.zero_crossing_rate(y=waveform, frame_length=features_frame_length)

    # Normalisation
    rms_frames_N = FonctionAnalyse.ListeNormalisée(rms_frames)
    spectral_centroid_frames_N = FonctionAnalyse.ListeNormalisée(spectral_centroid_frames)
    spectral_flatness_frames_N = FonctionAnalyse.ListeNormalisée(spectral_flatness_frames)
    chroma_stft_frames_N = FonctionAnalyse.ListeNormalisée(chroma_stft_frames)
    zero_crossing_rate_frames_N = FonctionAnalyse.ListeNormalisée(zero_crossing_rate_frames)

    donnee_brute = []  # on va réunir toutes les données en une seule liste
    n = len(rms_frames[0])  # peut poser problèmes si les tableaux sont de taille différentes
    for i in range(n):
        _rms = rms_frames[0][i]
        _spectral = spectral_centroid_frames_N[i]
        _flat = spectral_flatness_frames_N[i]
        _chroma = chroma_stft_frames_N[i]
        _zero = zero_crossing_rate_frames_N[i]
        donnee_brute.append(
            {'rms': _rms, 'sp_centroid': _spectral, 'sp_flatness': _flat, 'zero': _zero, 'chroma': _chroma})

    movements = {'rms':rms_frames_N, 'sp_centroid':spectral_centroid_frames_N, 'sp_flatness': spectral_flatness_frames_N,\
                 'zero_crossing': zero_crossing_rate_frames_N, 'chroma': chroma_stft_frames_N} #pour formules
    movements = config_interpreter.Traitement(movements, conf)
    debug(movements)

    pygame.mixer.music.load(file)

    ui.timer = QtCore.QTimer()
    ui.timer.timeout.connect(lambda: timer_update(ui, movements))

    return movements

def timer_update(ui, movements):
    if (pygame.mixer.music.get_busy()):
        current_time = pygame.mixer.music.get_pos()
        # find closest frame in descriptors
        index = current_time // ui.frame_duration_ms
        index = round(min(index, len(movements) - 1)) + ui.horizontalSlider.value()

        for out in config_ui.OUTPUTS:
            if out in movements[index].keys():
                if out in ["rect", "ellipse"]:
                    donnee_utile = movements[index][out]
                    dim = donnee_utile * SCALE
                    ui.OBJECTS[out].setRect(-dim,-dim, dim*2, dim*2) #A ETOFFER
                elif out in ["rect_border", "ellipse_border"]:
                    donnee_utile = movements[index][out]
                    objName = out.split("_")[0]
                    dim = donnee_utile * WIDTH_SCALE
                    pen = QtGui.QPen(QtCore.Qt.red if objName == "ellipse" else QtCore.Qt.blue, dim)
                    ui.OBJECTS[objName].setPen(pen)

    else:
        if ui.checkBox.checkState(): #si mode boucle
            ui.soundTimeControl(3)
        else:
            ui.pushButton.clicked.disconnect()
            ui.pushButton.clicked.connect(lambda: ui.soundTimeControl(2))
            ui.pushButton.setText("|>")
            for x in ui.OBJECTS.keys(): ui.OBJECTS[x].setRect(0,0,0,0)
            ui.timer.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = main_ui.Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    ui.configs = initConf()
    showConfig(ui)
    ui.sounds = initSounds(ui)
    pygame.mixer.init()

    filename = config.soundsFolder + "/" + ui.sounds[0]

    confID = ui.comboBox_2.currentIndex()
    ui.currentConf = config.readfile(config.configFolder + "/" + str(confID) + config.configExtension)
    ui.currentSound = config.soundsFolder + "/" + ui.comboBox.currentText()

    sys.exit(app.exec_())
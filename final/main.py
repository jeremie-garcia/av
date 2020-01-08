#Version modifiée d'av réorganisant les données en liste de dictionnaire
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa
import main_ui, config_interpreter, config, FonctionAnalyse
DEBUG = True

def initConf():
    try :
        confFiles = os.listdir(config.configFolder+"/")
    except:
        confFiles = []

    configs = {}

    for i,f in enumerate(confFiles):
        tmp = config.readfile(config.configFolder + "/" + f)
        try : configs[tmp.id] = tmp
        except : debug("Erreur {}".format(tmp))

    return configs

def debug(*args):
    if DEBUG: print(*args)

if __name__ == '__main__':

    configs = initConf()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = main_ui.Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    # 0. select a sound file to open
    filename = 'sounds/s1.wav'
    #filename = 'sounds/s2.wav'

    # 1. extract descriptors from the audiofile using librosa
    # Load the audio as a waveform `waveform`
    # Store the sampling rate as `sr`
    waveform, sr = librosa.load(filename)

    # 2. Extract features (rms, spectral centroid, spectral flatness)
    features_frame_length =  4096
    frame_duration_ms = 1000 * (512 / sr)
    rms_frames = librosa.feature.rms(y=waveform, S=None, frame_length=features_frame_length)
    spectral_centroid_frames = librosa.feature.spectral_centroid(y=waveform,sr=sr, S= None, n_fft=features_frame_length )
    spectral_flatness_frames = librosa.feature.spectral_flatness(y=waveform, S= None, n_fft=features_frame_length )
    chroma_stft_frames = librosa.feature.chroma_stft(y=waveform, S= None, n_fft=features_frame_length)
    zero_crossing_rate_frames = librosa.feature.zero_crossing_rate(y = waveform, frame_length = features_frame_length)

    #Normalisation
    rms_frames_N = FonctionAnalyse.ListeNormalisée(rms_frames)
    spectral_centroid_frames_N = FonctionAnalyse.ListeNormalisée(spectral_centroid_frames)
    spectral_flatness_frames_N = FonctionAnalyse.ListeNormalisée(spectral_flatness_frames)
    chroma_stft_frames_N = FonctionAnalyse.ListeNormalisée(chroma_stft_frames_)
    zero_crossing_rate_frames_N = FonctionAnalyse.ListeNormalisée(zero_crossing_rate_frames)

    # on va réunir toutes les données en une seule liste
    donnee_brute = []
    n = len(rms_frames[0]) #peut poser problèmes si les tableaux sont de taille différentes
    for i in range(n):
        _rms = rms_frames[0][i]
        _spectral = spectral_centroid_frames_N[0][i]
        _flat = spectral_flatness_frames_N[0][i]
        _chroma = chroma_stft_frames_N[0][i]
        _zero = zero_crossing_rate_frames_N[0][i]
        donnee_brute.append({'rms' : _rms, 'sp_centroid' : _spectral, 'sp_flatness' : _flat,'zero' : _zero, 'chroma' : _chroma})
    debug(donnee_brute)

    #3 init pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)

    conf = config.readfile("configs/0.conf")
    movements = config_interpreter.Traitement(donnee_brute, conf)
    print(movements)

    def timer_update(ui, movements):
        if (pygame.mixer.music.get_busy()):
            current_time = pygame.mixer.music.get_pos()
            # find closest frame in descriptors
            index = current_time // frame_duration_ms
            index = round(min(index, rms_frames[0].size - 1))
            if 'largeur' in movements[index]:
                donné_utile = movements[index]['largeur']
                dim = donné_utile*250
                ui.ellipse.setRect(-dim,-dim, dim*2, dim*2)
            if 'rect' in movements[index]:
                donnee_utile = movements[index]['rect']
                dim = donnee_utile/50
                ui.rectangle.setRect(-dim, -dim, dim * 2, dim * 2)
            # if... etc

        else:
            timer.stop()

    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: timer_update(ui, movements))

    pygame.mixer.music.play(0)
    timer.start(frame_duration_ms)

    sys.exit(app.exec_())
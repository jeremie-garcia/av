
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa


#Qt Designer File
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(736, 688)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(160, 110, 400, 400))
        self.frame.setStyleSheet("image: url(:/fichier/C:/Users/gabth/Desktop/Enac.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(13)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
#Av
if __name__ == '__main__':

    # 0. select a sound file to open
    filename = 'C:\\Users\\gabth\\Downloads\\s1.wav'
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

    #3 init pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)

    #4 call-back each frameduration

    #4 create a PyQtApp to use pyQtTimer
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #5 added function

    ind_largeur = None

    # Aude renvoie un dictionnaire, qui a chaque clé (géométrie), renvoie la liste déjà normalisée des données a rentrer directement dans timer_update
    def interpreteur_dico_qt(dico):
        nb_param = len(dico)  # nombre de paramètre du qt à faire varier
        for param, indice in enumerate dico:  # On parcourt ces parametres, que l'on identifie
            if param == 'largeur':
                ind_largeur = indice
            #if ... etc

    interpreteur_dico_qt(dico) #Mise a jour des indices

    def timer_update(uiform):
        if (pygame.mixer.music.get_busy()):
            current_time = pygame.mixer.music.get_pos()
            # find closest frame in descriptors
            index = current_time // frame_duration_ms
            index = round(min(index, rms_frames[0].size - 1))
            if 'largeur' in dico:
                donné_utile = dico[ind_largeur][index]
                uiform.frame.setLineWidth(donné_utile)
            #if... etc

        else:
            timer.stop()


    pygame.mixer.music.get_pos()
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda : timer_update(ui))

    pygame.mixer.music.play(0)
    timer.start(frame_duration_ms)
    sys.exit(app.exec_())


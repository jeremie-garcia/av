import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import view
import librosa

class Sound(object):
    def __init__(self):
        self.filename='sounds/s1.wav'
        self.rms_frames=None
        self.spectral_centroid_frames=None
        self.spectral_flatness_frames=None

    def change(self,new_sound):
        self.filename='sounds/'+new_sound+'.wav'

    def analyze(self):
        self.waveform, self.sr = librosa.load(self.filename)
        self.analyse_parameters = {"features_frame_length":4096, "frame_duration_ms":1000*(512/self.sr)}
        self.rms_frames=librosa.feature.rms(y=self.waveform, S=None, frame_length=self.analyse_parameters["features_frame_length"])
        self.spectral_centroid_frames = librosa.feature.spectral_centroid(y=self.waveform, sr=self.sr, S=None, n_fft=self.analyse_parameters["features_frame_length"])
        self.spectral_flatness_frames = librosa.feature.spectral_flatness(y=self.waveform, S=None, n_fft=self.analyse_parameters["features_frame_length"])



         
    
    



"""


    #3 init pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)

    #4 call-back each frameduration
    #4 create a PyQtApp to use pyQtTimer
    app = QtWidgets.QApplication(sys.argv)
    
    def timer_update():
        if (pygame.mixer.music.get_busy()):
            current_time = pygame.mixer.music.get_pos()
            # find closest frame in descriptors
            index = current_time // frame_duration_ms
            index = round(min(index, rms_frames[0].size - 1))
            rms = rms_frames[0][index]
            spectral_centroid = spectral_centroid_frames[0][index]
            spectral_flatness = spectral_flatness_frames[0][index]
            print(rms, spectral_flatness, spectral_centroid)
        else:
            timer.stop()

    timer = QtCore.QTimer()
    timer.timeout.connect(timer_update)

    pygame.mixer.music.play(0)
    timer.start(frame_duration_ms)

    sys.exit(app.exec_())
"""
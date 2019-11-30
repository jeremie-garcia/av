import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa

if __name__ == '__main__':

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

    #3 init pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)

    #4 call-back each frameduration

    # 4 create a PyQtApp to use pyQtTimer
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel("Hello World")
    label.show()

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



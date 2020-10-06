import os
import sys
import pygame
import librosa

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsItem, \
    QGraphicsEllipseItem

pygame.init()
pygame.mixer.init()


class QAVAlarmItem(QGraphicsEllipseItem):
    def __init__(self, sound_file):
        super().__init__(None)
        # instance variables
        self.sound_file = sound_file
        self.wave_form = []
        self.pen = QPen()
        self.brush = QBrush(Qt.SolidPattern)
        self.data = []
        self.is_congruent = True
        self.setRect(0,0, 20,20)

        #process audio data
        self.features_frame_length = 1024
        self.analyse_audio()

        #load audio in pygame
        self.sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),self.sound_file ))


    def analyse_audio(self):
        # 1. extract descriptors from the audiofile using librosa
        # Load the audio as a waveform `waveform`
        # Store the sampling rate as `sr`
        self.waveform, self.sr = librosa.load(self.sound_file)
        print('samplerate', self.sr)

        # 2. Extract features (rms, spectral centroid, spectral flatness)
        self.frame_duration_ms = 1000 * (512 / self.sr)
        print('frameduration for sound', self.sound_file, self.frame_duration_ms)

        self.rms_frames = librosa.feature.rms(y=self.waveform, S=None, frame_length=self.features_frame_length)[0]
        self.spectral_centroid_frames = librosa.feature.spectral_centroid(y=self.waveform, sr=self.sr, S=None,
                                                                     n_fft=self.features_frame_length)[0]

        # retrieve data
    def set_congruent(self, is_congruent):
        self.is_congruent = is_congruent

    def start(self):
        print('playing sound', self.sound)
        self.channel = pygame.mixer.find_channel()
        left, right = 1.0, 1.0
        if self.pos().x() <0 :
            right = 0.
        else:
            left = 0

        self.channel.set_volume(left, right)
        self.channel.play(self.sound)

    def stop(self):
        self.channel.stop(self.sound)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(200,200,500,500)
    layout = QHBoxLayout()
    widget.setLayout(layout)

    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)

    layout.addWidget(view)
    #create alarms widgets

    al1 = QAVAlarmItem("alarms/al-6.wav")
    scene.addItem(al1)
    al2 = QAVAlarmItem("sounds/s1.wav")
    scene.addItem(al2)

    al1.setPos(-20, 10)
    al2.setPos(100,80)

    view.setRenderHint(QPainter.Antialiasing)
    #view.fitInView(view.sceneRect(), Qt.KeepAspectRatio)

    def start_animations(event):
        al1.start()
        al2.start()


    scene.mousePressEvent = start_animations


    widget.show()
    sys.exit(app.exec_())
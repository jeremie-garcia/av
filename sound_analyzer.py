import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import view
import librosa

class Sound(object):
    def __init__(self):
        self.filename='sounds/franceGall.wav'
        self.dictionnaire_sounds={'Sound 1': 'sounds/s1.wav', 'Sound 2': 'sounds/s2.wav', 'Sound 3': 'sounds/s3.wav',
                                  'Sound 4': 'sounds/s4.wav', 'Sound 5': 'sounds/s5.wav', 'Sound 6': 'sounds/s6.wav',
                                  'Sound 7': 'sounds/s7.wav', 'Sound 8': 'sounds/s8.wav', 'Sound 9': 'sounds/s9.wav',
                                  'Sound 10': 'sounds/s10.wav', 'Sound 11': 'sounds/s11.wav',
                                  'La Moulaga': 'sounds/moulaga.wav', 'France Gall': 'sounds/franceGall.wav',
                                  'Dire Straits': 'sounds/dire_straits.wav', 'Numb': 'sounds/Numb.wav',
                                  'Djadja': 'sounds/djadja.wav', 'TNT': 'sounds/acdc-tnt.wav', 'Da Ba Dee': 'sounds/dabadee.wav'}
        self.rms_frames=None
        self.spectral_centroid_frames=None
        self.spectral_flatness_frames=None

    #def change(self,new_sound):
    #    self.filename='sounds/'+new_sound+'.wav'

    def analyze(self):
        self.waveform, self.sr = librosa.load(self.filename)
        self.analyse_parameters = {"features_frame_length":4096, "frame_duration_ms":1000*(512/self.sr)}
        self.rms_frames=librosa.feature.rms(y=self.waveform, S=None, frame_length=self.analyse_parameters["features_frame_length"])
        self.spectral_centroid_frames = librosa.feature.spectral_centroid(y=self.waveform, sr=self.sr, S=None, n_fft=self.analyse_parameters["features_frame_length"])
        self.spectral_flatness_frames = librosa.feature.spectral_flatness(y=self.waveform, S=None, n_fft=self.analyse_parameters["features_frame_length"])


    def normalize(self):
        maxi_rms=max(self.rms_frames[0])
        for i in range(len(self.rms_frames[0])):
            self.rms_frames[0][i]/=maxi_rms

        maxi_spectral_centroid = max(self.spectral_centroid_frames[0])
        for i in range(len(self.spectral_centroid_frames[0])):
            self.spectral_centroid_frames[0][i] /= maxi_spectral_centroid

        maxi_spectral_flatness = max(self.spectral_flatness_frames[0])
        for i in range(len(self.spectral_flatness_frames[0])):
            self.spectral_flatness_frames[0][i] /= maxi_spectral_flatness


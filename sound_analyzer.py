"""This module allows to analyze sounds and to normalize its parameters"""

import librosa
import numpy as np


class Sound(object):
    """Sound information"""

    def __init__(self):
        self.filename = 'sounds/s1.wav'

        # dictionary of sounds
        self.sounds_dictionary = {'Sound 1': 'sounds/s1.wav', 'Sound 2': 'sounds/s2.wav', 'Sound 3': 'sounds/s3.wav',
                                  'Sound 4': 'sounds/s4.wav', 'Sound 5': 'sounds/s5.wav', 'Sound 6': 'sounds/s6.wav',
                                  'Sound 7': 'sounds/s7.wav', 'Sound 8': 'sounds/s8.wav', 'Sound 9': 'sounds/s9.wav',
                                  'Sound 10': 'sounds/s10.wav', 'Sound 11': 'sounds/s11.wav',
                                  'France Gall': 'sounds/s12.wav', 'Djadja': 'sounds/s13.wav',
                                  'TNT': 'sounds/s14.wav', 'Da Ba Dee': 'sounds/s15.wav'}

        # sounds parameters
        self.rms_frames = None
        self.spectral_centroid_frames = None
        self.spectral_flatness_frames = None
        self.waveform = None
        self.sr = None
        self.analyse_parameters = None

    def analyze(self):
        """Analyzes sounds and gives three of its characteristics : rms, spectral flatness and spectral centroid"""

        print("load '{}'".format(self.filename))
        self.waveform, self.sr = librosa.load(self.filename)
        self.analyse_parameters = {"features_frame_length": 4096, "frame_duration_ms": 1000*(512/self.sr)}
        self.rms_frames = librosa.feature.rms(y=self.waveform, S=None,
                                              frame_length=self.analyse_parameters["features_frame_length"])
        self.spectral_centroid_frames =\
            librosa.feature.spectral_centroid(y=self.waveform, sr=self.sr, S=None,
                                              n_fft=self.analyse_parameters["features_frame_length"])
        self.spectral_flatness_frames =\
            librosa.feature.spectral_flatness(y=self.waveform, S=None,
                                              n_fft=self.analyse_parameters["features_frame_length"])
        print("'{}' loaded".format(self.filename))

    def normalize_figures(self):
        """Normalizes sounds parameters"""

        def normalize(frames, norm):
            for i in range(len(frames[0])):
                frames[0][i] /= norm
                if frames[0][i] >= 1:
                    frames[0][i] = 1

        norm_rms = max(self.rms_frames[0])
        norm_spectral_centroid = 1.2 * np.median(self.spectral_centroid_frames[0])
        norm_spectral_flatness = (20 + np.std(self.spectral_flatness_frames[0])) * np.median(self.spectral_flatness_frames[0])
        normalize(self.rms_frames, norm_rms)
        normalize(self.spectral_flatness_frames, norm_spectral_flatness)
        normalize(self.spectral_centroid_frames, norm_spectral_centroid)






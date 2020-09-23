import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import librosa
import random

if __name__ == '__main__':

    sounds = ['alarms/al-1.mp3', 'alarms/al-2.mp3', 'alarms/al-4.mp3', 'alarms/al-5.mp3',
              'alarms/al-7.wav']

    data_1 = []
    circle_1 = QtWidgets.QGraphicsEllipseItem()
    pen_1 = QtGui.QPen()
    brush_1 = QtGui.QBrush(QtCore.Qt.SolidPattern)

    data_2 = []
    circle_2 = QtWidgets.QGraphicsEllipseItem()
    pen_2 = QtGui.QPen()
    brush_2 = QtGui.QBrush(QtCore.Qt.SolidPattern)

    # 4 create a PyQtApp to use pyQtTimer
    app = QtWidgets.QApplication(sys.argv)


    def process_snd(data, current_time, circle, id):
        # retrieve data
        frame_duration_ms = data[0]
        rms_frames = data[1]
        spectral_centroid_frames = data[2]
        spectral_flatness_frames = data[3]

        # find closest frame in descriptors
        index = current_time // frame_duration_ms
        index = round(min(index, rms_frames.size - 1))

        # extract data
        rms = rms_frames[index]
        spectral_centroid = spectral_centroid_frames[index]
        spectral_flatness = spectral_flatness_frames[index]
        # print(rms, spectral_flatness, spectral_centroid)

        # map to visual parameters
        width = rms * 100

        if id == 1:
            #left
            x = -150 - width / 2
        if id == 2:
            x = 150 - width / 2

        circle.setRect(x, -width/2, width, width)


    def timer_update():
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos()
            process_snd(data_1, current_time, circle_1, 1)
            process_snd(data_2, current_time, circle_2, 2)
        else:
            timer.stop()


    timer = QtCore.QTimer()
    timer.timeout.connect(timer_update)

    # 5 create a view and a scene
    view = QtWidgets.QGraphicsView()
    view.setWindowTitle("Congruent or Not ?")
    view.setRenderHint(QtGui.QPainter.Antialiasing)
    scene = QtWidgets.QGraphicsScene()
    view.setScene(scene)

    # setup circles Item with default size / colors / positions
    circle_1 = QtWidgets.QGraphicsEllipseItem(-200, -50, 100, 100)
    pen_1.setColor(QtGui.QColor('gray'))
    circle_1.setPen(pen_1)
    brush_1.setColor(QtGui.QColor('gray'))
    circle_1.setBrush(brush_1)
    circle_2 = QtWidgets.QGraphicsEllipseItem(100, -50, 100, 100)
    pen_2.setColor(QtGui.QColor('gray'))
    circle_2.setPen(pen_2)
    brush_2.setColor(QtGui.QColor('gray'))
    circle_2.setBrush(brush_2)

    scene.addItem(circle_1)
    scene.addItem(circle_2)

    view.fitInView(view.sceneRect(), QtCore.Qt.KeepAspectRatio)
    view.resize(800, 600)
    view.show()


    def normalize_list(list):
        max_value = max(list)
        min_value = min(list)
        for i in range(0, len(list)):
            list[i] = (list[i] - min_value) / (max_value - min_value)
        return list


    def analyse_sound_file(filename):

        # 1. extract descriptors from the audiofile using librosa
        # Load the audio as a waveform `waveform`
        # Store the sampling rate as `sr`
        waveform, sr = librosa.load(filename)

        # 2. Extract features (rms, spectral centroid, spectral flatness)
        features_frame_length = 2048
        frame_duration_ms = 1000 * (512 / sr)
        print('frameduration for sound', filename, frame_duration_ms)
        rms_frames = librosa.feature.rms(y=waveform, S=None, frame_length=features_frame_length)[0]
        spectral_centroid_frames = librosa.feature.spectral_centroid(y=waveform, sr=sr, S=None,
                                                                     n_fft=features_frame_length)[0]
        spectral_flatness_frames = librosa.feature.spectral_flatness(y=waveform, S=None, n_fft=features_frame_length)[0]
        return [frame_duration_ms, normalize_list(rms_frames), spectral_centroid_frames, spectral_flatness_frames]


    def start_animation(event):
        global data_1, data_2
        # stop Audio and reset visual

        # find two sounds (randomly)
        sound_1, sound_2 = random.sample(sounds, 2)
        print('selected', sound_1, sound_2)

        # extract data for each
        data_1 = analyse_sound_file(sound_1)
        # print(data_1)
        data_2 = analyse_sound_file(sound_2)
        # print(data_2)

        # play one of the sounds and draw both shape
        to_play = random.choice([sound_1, sound_2])
        print('playing', to_play)

        # 3 init pygame
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(to_play)

            pygame.mixer.music.play(0)
            # TODO need to use matching data instead
            timer.start(data_1[0] / 2)
        except pygame.error:
            print('error')

    scene.mousePressEvent = start_animation

    sys.exit(app.exec_())

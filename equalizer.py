from PyQt5.QtWidgets import (QMainWindow, 
                              QFileDialog, QApplication)
from pyqtgraph.Qt import QtCore
from scipy import signal
import sys
import simpleaudio as sa
import math
import pyqtgraph as pg
import matplotlib.pyplot as plt
import numpy as np
import wavio
from copy import copy
from scipy.io import wavfile
from IPython.display import Audio 
from popup import Ui_Dialog as Form
from PyQt5 import QtCore, QtGui, QtWidgets

from newguiTest import Ui_MainWindow

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time = []
        self.Scales = [self.ui.s1,self.ui.s2,self.ui.s3,self.ui.s4,self.ui.s5,self.ui.s6,self.ui.s7,self.ui.s8,self.ui.s9,self.ui.s10]
        self.EQLabels = [self.ui.band1, self.ui.band2,self.ui.band3,self.ui.band4,self.ui.band5,self.ui.band6,self.ui.band7,self.ui.band8,self.ui.band9,self.ui.band10]
        self.newFreqMagnitude = [[], []]
        self.newFreq= [[], []]
        self.band = [[], []]
        #self.gains = [[10], [10]]
        self.gains =[[1]*10, [1]*10] 
        self.gain = [1, 1]
        self.scaledMag = [[], []]
        self.bandsDivided = [[],[],[],[],[],[],[],[],[],[]]
        self.scaledMagDicided = [[],[],[],[],[],[],[],[],[],[]]
        self.dectionary = {}

        self.initUI()

    def initUI(self):

        self.ui.actionopen.triggered.connect(self.open_audio)
        self.show()

    
                
    def open_audio(self):
        
        self.fname = QFileDialog().getOpenFileName(self, 'Open file', '/home',"signals(*.wav )")
        self.select_equalizer()
        self.ui.comboBox.currentIndexChanged.connect(self.select_equalizer)


    def checked_window(self):

        for i in range(3) :
            self.windowList[i].clicked.connect(lambda ch , i=i: self.get_window(self.windowList[i].text()))
    

    def get_window(self,EQNumber):
        if self.ui.comboBox_2.currentText() != "":
            for scale in range(10) :
                self.Scales[scale].setEnabled(True) 
        else:
            self.ui.graphicsView.clear()
            self.ui.graphicsView_2.clear()
            for scale in range(10) :
                self.Scales[scale].setEnabled(False) 
        
        if self.ui.comboBox_2.currentText() == "Rectangular" :
            self.Equalizer(EQNumber , self.ui.comboBox_2.currentText() )
            self.slider_changed(EQNumber , self.ui.comboBox_2.currentText() )


        elif self.ui.comboBox_2.currentText() == "Hanning" :
            self.Equalizer(EQNumber , self.ui.comboBox_2.currentText() )
        elif self.ui.comboBox_2.currentText() == "Hamming" :
            self.Equalizer(EQNumber , self.ui.comboBox_2.currentText() )


    def select_equalizer(self):
        if self.ui.comboBox.currentText() == "Original" :
            self.plotAudio()

            self.plotFourier() 
            for scale in range(10) :
                self.Scales[scale].setEnabled(False)  
            self.ui.comboBox_2.setEnabled(False)
        elif self.ui.comboBox.currentText() == "EQ1" or "EQ2" :
            self.ui.comboBox_2.setEnabled(True)
            self.ui.label.setEnabled(True)
            
            self.ui.pushButton_3.clicked.connect(lambda: self.showDifference(self.audio, self.timeWaveReal, abs(self.fourier), self.totalMag))            
            if self.ui.comboBox.currentText() == "EQ1":
                self.EQNum = 0
                
            else :
                
                self.EQNum = 1

            if self.ui.comboBox_2.currentText() == "":
                self.ui.graphicsView.clear()
                self.ui.graphicsView_2.clear()
            else:
                
                self.Equalizer(self.EQNum, self.ui.comboBox_2.currentText())
                for sliderNum in range(10):
                    self.Scales[sliderNum].setValue(self.gains[self.EQNum][sliderNum])
                    
                
            self.ui.comboBox_2.currentIndexChanged.connect(lambda: self.get_window(self.EQNum))

    def plotAudio(self):

        Audio (str(self.fname[0]))    
        self.rate, self.audio = wavfile.read(str(self.fname[0]))  

        self.audio = np.mean(self.audio, axis=1)
        self.dataSize= self.audio.shape[0]          
        self.totalTime = self.dataSize/ self.rate           
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.ui.graphicsView.addLegend()
        self.time = np.arange(self.dataSize) / self.rate
        self.plotting(self.ui.graphicsView, self.time, self.audio, "sound waveform")
        self.ui.pushButton.clicked.connect(lambda: self.playChoice())

    def plotFourier(self):

        self.fourier = np.fft.rfft(self.audio)
        self.length = len(self.fourier)
        self.bandwidth = self.length//10
        self.freq = np.fft.rfftfreq(self.dataSize,    d= 1/ self.rate)
        print (self.length, len(self.fourier))
        for bandNumber in range(10):
            self.EQLabels[bandNumber].setText(str(math.ceil(bandNumber * self.bandwidth/100.0)/20.0) + "-" + str(math.ceil(self.bandwidth * (1 + bandNumber)/100.0)/20.0) + " KHZ")
        
        for i in range(len(self.fourier)):
            self.dectionary[i] = self.fourier[i]

        self.plotting(self.ui.graphicsView_2, self.freq, abs(self.fourier), "fourier")


    def Equalizer(self ,EQNum, window):
        bandNumber=0
        
        if window == "Rectangular":
            self.newFreq[EQNum] = []
            self.band[EQNum] = []
            while bandNumber<10 :
                if bandNumber == 9:
                    self.band[EQNum] = self.fourier[bandNumber*self.bandwidth : ] 
                    self.bandsDivided[bandNumber] = self.fourier[bandNumber*self.bandwidth : ] 

                else:
                    self.band[EQNum] = self.fourier[bandNumber*self.bandwidth : bandNumber*self.bandwidth + (self.bandwidth)]
                    self.bandsDivided[bandNumber] = self.fourier[bandNumber*self.bandwidth : bandNumber*self.bandwidth + (self.bandwidth)]

                bandWindow = self.band[EQNum] * self.gain[EQNum]
                self.newFreq[EQNum] = np.append(self.newFreq[EQNum], bandWindow)
                for i in range(10) :
                    self.scaledMagDicided[i] =  np.abs(self.bandsDivided[i])
                bandNumber += 1
            self.newFreqMagnitude[EQNum] = np.abs(self.newFreq[EQNum])
        
        else:
            self.newFreq[EQNum]= copy(self.fourier)
            windowing = self.HamHan(window)
            bandCentralFreq = self.bandwidth//2 + self.bandwidth * bandNumber
            if bandNumber== 0:
                self.newFreq[EQNum][: math.floor(1.5 * self.bandwidth)] *= windowing[len(self.newFreq[EQNum][: math.floor(1.5 * self.bandwidth)])] * self.gain[EQNum]
            elif bandNumber== 9:
                self.newFreq[EQNum][bandCentralFreq - self.bandwidth :] *= windowing[: math.floor(1.5*self.bandwidth)]* self.gain[EQNum]
            else:
                self.newFreq[EQNum][bandCentralFreq - self.bandwidth : bandCentralFreq + self.bandwidth] *= windowing * self.gain[EQNum]
            self.newFreqMagnitude[EQNum]= np.abs(self.newFreq[EQNum])
 
        self.plotting(self.ui.graphicsView_2, self.freq, self.newFreqMagnitude[EQNum], "scaled fourier")
        
        self.showIFFT(self.ui.graphicsView, EQNum , self.newFreq[EQNum] , self.newFreqMagnitude[EQNum])

        
                
    def plotting(self, obj, x , y, Name):
        obj.clear()
        
        obj.plot(x, y, name = Name, pen= self.pen)

            
    def showIFFT(self , IFFTplot, EQNum , fftData, totalMag):
        timeWave = np.fft.irfft(fftData , n = len(self.audio))
        self.timeWaveReal = np.real(timeWave)
        self.plotting(IFFTplot, self.time, self.timeWaveReal, "sound with EQ")
        
        self.ui.actionSave_EQ1.triggered.connect(lambda: self.Save_audio(str(self.fname[0])))
        
    def Save_audio(self, name):
        wavio.write( name[:-4] + "Equalized_version.wav", self.timeWaveReal, self.rate, sampwidth = 2)

    def Save_audioEQ2(self, name):
        wavio.write( name[:-4] + "Equalized_versionEQ2.wav", self.timeWaveReal, self.rate, sampwidth = 2)


    def showDifference(self , audio_1, audio_2, fftaudio_1, fftaudio_2) :
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        dialog.ui.graphicsView.plot(self.time ,audio_1-audio_2)
        dialog.ui.graphicsView_2.plot(self.freq, abs(fftaudio_1-fftaudio_2))

        dialog.exec_()
        dialog.show()


    def getGain (self, EQNum, bandNumber):
        
        self.gain[EQNum] = self.Scales[bandNumber].value()
        self.gains[EQNum][bandNumber] = self.gain[EQNum]
        if self.gain[EQNum] < 0:
            self.gain[EQNum] = -1/self.gain[EQNum]
        self.Scale(EQNum, self.ui.comboBox_2.currentText(), bandNumber)
        return self.gains, self.gain
    
    def slider_changed(self, EQ , Window):
        for sliderNum in range(10) :
            self.Scales[sliderNum].valueChanged.connect(lambda ch, sliderNum=sliderNum: self.getGain(self.EQNum, sliderNum))

    def Scale(self,EQNumber, window, bandNumber):
        scaledbandfft = [[],[],[],[],[],[],[],[],[],[]]
        if window == "Rectangular":
            scaledbandfft[bandNumber] = self.bandsDivided[bandNumber] * self.gain[EQNumber]
            j = 0 


            if bandNumber == 9:
                for i in range(bandNumber*self.bandwidth , len(self.fourier)) :
                    self.dectionary[i] = scaledbandfft[bandNumber][j]
                    j = j + 1 

            else:
                for i in range(bandNumber*self.bandwidth , bandNumber*self.bandwidth + (self.bandwidth)) :
                    self.dectionary[i] = scaledbandfft[bandNumber][j]
                    j = j + 1 
                
        else:
            self.Equalizer(EQNumber, window)

        totalScaled = list()

        for key in self.dectionary.keys():
            totalScaled.append(self.dectionary[key])
        
        self.totalMag = abs(np.array(totalScaled))
        self.ui.pushButton_3.setEnabled(True)
        self.plotting(self.ui.graphicsView_2, self.freq, self.totalMag, "scaled fourier")    
        self.showIFFT(self.ui.graphicsView , EQNumber , totalScaled , self.totalMag)
    


    def HamHan(self, window):
        if window == "hanning":
            windowing = np.hanning(self.bandwidth*2)
        else:
            windowing = signal.hamming(self.bandwidth*2)
        return windowing


    def playChoice(self):
        if self.ui.comboBox.currentText() == "Original":
            self.play(self.audio, self.rate, self.ui.pushButton_2, self.ui.pushButton)
        else:
            self.play(self.timeWaveReal, self.rate, self.ui.pushButton_2, self.ui.pushButton)
            
    def play(self, Audio,rate , pushButton, playButton):
        Audio *= 32767 / np.max(np.abs(Audio))
        Audio = Audio.astype(np.int16)
        
        self.play_obj = sa.play_buffer(Audio, 1, 2, rate)
        
        if self.play_obj.is_playing() :
            playButton.setEnabled(False)
            QtCore.QTimer.singleShot(self.totalTime *1000, lambda: playButton.setDisabled(False))

        pushButton.clicked.connect(lambda: self.stop(playButton))

        
    def stop(self,playButton ):
        self.play_obj.stop()
        playButton.setDisabled(False)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    ex = Example()
    sys.exit(app.exec_())
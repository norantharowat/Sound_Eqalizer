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

from gui import Ui_MainWindow

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time = []
        self.Scales = [self.ui.s1,self.ui.s2,self.ui.s3,self.ui.s4,self.ui.s5,self.ui.s6,self.ui.s7,self.ui.s8,self.ui.s9,self.ui.s10]
        self.EQLabels = [self.ui.band1, self.ui.band2,self.ui.band3,self.ui.band4,self.ui.band5,self.ui.band6,self.ui.band7,self.ui.band8,self.ui.band9,self.ui.band10]
        self.newFreqMagnitude = []
        self.newFreq= []
        self.band = []
        self.Save_gains =[[1]*10, [1]*10] 
        print(self.Save_gains)
        self.Save_window =  ["",""]

        self.scaledMag = [[], []]
        self.bandsDivided = [[],[],[],[],[],[],[],[],[],[]]
        self.scaledMagDicided = [[],[],[],[],[],[],[],[],[],[]]
        self.dectionary = {}
        self.ui.comboBox_2.currentTextChanged.connect(self.eq_changes)
        self.ui.comboBox.currentTextChanged.connect(self.eq_changes)


        self.initUI()

    def initUI(self):

        self.ui.actionopen.triggered.connect(self.open_audio)
        self.ui.actionSave_EQ1_2.triggered.connect(lambda: self.Save_EQData(0 , self.ui.comboBox_2.currentText()))
        self.ui.actionGet_EQ1.triggered.connect(lambda : self.Get_EQData(0 , self.Save_window[0]))
        self.ui.actionSave_EQ2_2.triggered.connect(lambda: self.Save_EQData(1 , self.ui.comboBox_2.currentText()))
        self.ui.actionGet_EQ2.triggered.connect(lambda : self.Get_EQData(1 , self.Save_window[1]))
        self.show()

    def Save_EQData(self, EQNUM, Window):

        for i in range(10) :
            self.Save_gains[EQNUM][i] =  self.Scales[i].value()
        self.Save_window[EQNUM] = Window
    def Get_EQData(self, EQNUM, Window ):
        for i in range(10):
            self.Scales[i].setValue(self.Save_gains[EQNUM][i])

        self.ui.comboBox_2.setCurrentText(Window)
        if EQNUM == 0 :
            self.ui.comboBox.setCurrentText("EQ1")
        else :
            self.ui.comboBox.setCurrentText("EQ2")


        self.Equalizer(Window )


    def label_changes(self,result):
        if str(self.ui.comboBox_2.currentText()) =="Rectangular" and (str(self.ui.comboBox.currentText() =="EQ1") or str(self.ui.comboBox.currentText()) == "EQ2"):
            self.ui.label_2.setText("Rectangular res_"+str(result))
            self.ui.label_3.setText("Rectangular_fourier res_"+str(result))
        elif str(self.ui.comboBox_2.currentText())=="Hanning" and (str(self.ui.comboBox.currentText()) =="EQ1" or str(self.ui.comboBox.currentText()) == "EQ2"):
            self.ui.label_2.setText("Hanning res_"+str(result))
            self.ui.label_3.setText("Haning_fourier res_"+str(result))
        elif str(self.ui.comboBox_2.currentText())=="Hamming" and (str(self.ui.comboBox.currentText()) =="EQ1" or str(self.ui.comboBox.currentText()) == "EQ2"):
            self.ui.label_2.setText("Hamming res_"+str(result))
            self.ui.label_3.setText("Hamming_fourier res_"+str(result))
        
    def eq_changes(self):
        res=0
        if str(self.ui.comboBox.currentText()) =="EQ1" :
            res=1
            self.label_changes(res)
        elif str(self.ui.comboBox.currentText()) == "EQ2" :
            res=2
            self.label_changes(res)   
        elif str(self.ui.comboBox.currentText()) == "Original":
             self.ui.label_2.setText("Original")
             self.ui.label_3.setText("Fourier")       

                
    def open_audio(self):

        
        
        self.fname = QFileDialog().getOpenFileName(self, 'Open file', '/home',"signals(*.wav )")
        

        if self.fname[0]!='':
            self.ui.comboBox.setCurrentText("Original")
            self.ui.comboBox_2.setCurrentText("")
            self.ui.comboBox_2.setDisabled(True)
            self.select_equalizer()
            self.ui.pushButton_3.clicked.connect(lambda: self.showDifference(self.audio, self.timeWaveReal, abs(self.fourier), self.newFreqMagnitude))            

            self.ui.comboBox.currentIndexChanged.connect(self.select_equalizer)

        else:
            pass


        


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
            self.ui.pushButton_3.setDisabled(False)
            
            for scale in range(10) :
                self.Scales[scale].setEnabled(True)  
            
            if self.ui.comboBox.currentText() == "EQ1":
                self.EQNum = 0
                

                
            else :
                
                self.EQNum = 1


            if self.ui.comboBox_2.currentText() == "":
                self.ui.graphicsView.clear()
                self.ui.graphicsView_2.clear()
            else:
                
                self.Equalizer(self.ui.comboBox_2.currentText())
                
                    
                
            self.ui.comboBox_2.currentIndexChanged.connect(lambda: self.get_window(self.EQNum))





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
            self.Equalizer(self.ui.comboBox_2.currentText() )
            self.slider_changed(self.ui.comboBox_2.currentText() )



        elif self.ui.comboBox_2.currentText() == "Hanning" :
            self.Equalizer( self.ui.comboBox_2.currentText() )
            self.slider_changed(self.ui.comboBox_2.currentText() )


        elif self.ui.comboBox_2.currentText() == "Hamming" :
            self.Equalizer(self.ui.comboBox_2.currentText() )
            self.slider_changed(self.ui.comboBox_2.currentText() )



    def plotAudio(self):

        Audio (str(self.fname[0]))    
        self.rate, self.audio = wavfile.read(str(self.fname[0]))  

        self.audio = np.mean(self.audio, axis=1)
        self.dataSize= self.audio.shape[0]          
        self.totalTime = self.dataSize/ self.rate           
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.time = np.arange(self.dataSize) / self.rate
        self.plotting(self.ui.graphicsView, self.time, self.audio, "sound waveform")
        self.ui.pushButton.clicked.connect(lambda: self.playChoice())

    def plotFourier(self):

        self.fourier = np.fft.rfft(self.audio)
        self.length = len(self.fourier)
        self.bandwidth = self.length//10
        self.freq = np.fft.rfftfreq(self.dataSize,    d= 1/ self.rate)
        print(self.freq)

        for bandNumber in range(9):
            self.EQLabels[bandNumber].setText(str(self.freq[bandNumber*self.bandwidth]//1000) + "-" + str(self.freq[bandNumber * self.bandwidth + self.bandwidth]//1000) + " KHZ")
        self.EQLabels[9].setText(str(self.freq[9*self.bandwidth]//1000) + "-" + str(self.freq[-1]//1000) + " KHZ")
        
        for i in range(len(self.fourier)):
            self.dectionary[i] = self.fourier[i]

        self.plotting(self.ui.graphicsView_2, self.freq, abs(self.fourier), "fourier")


    def Equalizer(self , window):
        bandNumber=0
        
        if window == "Rectangular":
            self.newFreq= []
            self.band = []
            while bandNumber<10 :
                if bandNumber == 9:
                    self.band = self.fourier[bandNumber*self.bandwidth : ] 
                    self.bandsDivided[bandNumber] = self.fourier[bandNumber*self.bandwidth : ] 

                else:
                    self.band = self.fourier[bandNumber*self.bandwidth : bandNumber*self.bandwidth + (self.bandwidth)]
                    self.bandsDivided[bandNumber] = self.fourier[bandNumber*self.bandwidth : bandNumber*self.bandwidth + (self.bandwidth)]

                bandWindow = self.band * self.getGain( bandNumber )
                self.newFreq = np.append(self.newFreq, bandWindow)
                for i in range(10) :
                    self.scaledMagDicided[i] =  np.abs(self.bandsDivided[i])
                bandNumber += 1
            self.newFreqMagnitude = np.abs(self.newFreq)
        
        else:
            self.newFreq= copy(self.fourier)
            windowing = self.HamHan(window)
            while bandNumber <10 :
                bandCentralFreq = self.bandwidth//2 + self.bandwidth * bandNumber
                if bandNumber== 0:
                    self.newFreq[: math.floor(1.5 * self.bandwidth)] *= windowing[len(self.newFreq[: math.floor(1.5 * self.bandwidth)])] * self.getGain( bandNumber )
                elif bandNumber== 9:
                    self.newFreq[bandCentralFreq - self.bandwidth :] *= windowing[:len(self.newFreq[bandCentralFreq - self.bandwidth :] )]* self.getGain( bandNumber )
                else:
                    self.newFreq[bandCentralFreq - self.bandwidth : bandCentralFreq + self.bandwidth] *= windowing[len(windowing) - len(self.newFreq[bandCentralFreq - self.bandwidth : bandCentralFreq + self.bandwidth]):] * self.getGain( bandNumber )

                bandNumber += 1

            self.newFreqMagnitude= np.abs(self.newFreq)
 
        self.plotting(self.ui.graphicsView_2, self.freq, self.newFreqMagnitude, "scaled fourier")
        
        self.showIFFT(self.ui.graphicsView , self.newFreq , self.newFreqMagnitude)

        
                
    def plotting(self, obj, x , y, Name):
        obj.clear()
        
        obj.plot(x, y, name = Name, pen= self.pen)

            
    def showIFFT(self , IFFTplot  , fftData, totalMag):
        timeWave = np.fft.irfft(fftData , n = len(self.audio))
        self.timeWaveReal = np.real(timeWave)
        self.plotting(IFFTplot, self.time, self.timeWaveReal, "sound with EQ")
        
        self.ui.actionSave_EQ1.triggered.connect(lambda: self.Save_audio(str(self.fname[0])))
        self.ui.actionSave_EQ2.triggered.connect(lambda: self.Save_audioEQ2(str(self.fname[0])))
        
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


    def getGain (self, bandNumber):
        gain = self.Scales[bandNumber].value()

        if gain < 0:
            gain = -1/gain


        return gain


    def slider_changed(self , Window):
        for sliderNum in range(10) :
            self.Scales[sliderNum].valueChanged.connect(lambda ch, sliderNum=sliderNum: self.Scale( Window, sliderNum))


    def Scale(self, window, bandNumber):
        scaledbandfft = [[],[],[],[],[],[],[],[],[],[]]
        if window == "Rectangular":
            scaledbandfft[bandNumber] = self.bandsDivided[bandNumber] * self.getGain( bandNumber)
            j = 0 


            if bandNumber == 9:
                for i in range(bandNumber*self.bandwidth , len(self.fourier)) :
                    self.dectionary[i] = scaledbandfft[bandNumber][j]
                    j = j + 1 

            else:
                for i in range(bandNumber*self.bandwidth , bandNumber*self.bandwidth + (self.bandwidth)) :
                    self.dectionary[i] = scaledbandfft[bandNumber][j]
                    j = j + 1 

            totalScaled = list()

            for key in self.dectionary.keys():
                totalScaled.append(self.dectionary[key])
            
            self.totalMag = abs(np.array(totalScaled))
            self.newFreqMagnitude = copy(self.totalMag)

            self.plotting(self.ui.graphicsView_2, self.freq, self.totalMag, "scaled fourier")    
            self.showIFFT(self.ui.graphicsView , totalScaled , self.totalMag )
                

        else:
            self.Equalizer( window)

        #self.ui.pushButton_3.setEnabled(True)




    

    def HamHan(self, window):
        if window == "hanning":
            windowing = np.hanning(self.bandwidth*2)
        else:
            windowing = np.hamming(self.bandwidth*2)
        return windowing


    def playChoice(self):
        if self.ui.comboBox.currentText() == "Original":
            self.play(self.audio, self.rate, self.ui.pushButton_2, self.ui.pushButton )
        else:
            self.play(self.timeWaveReal, self.rate, self.ui.pushButton_2, self.ui.pushButton)
            
    def play(self, Audio,rate , pushButton, playButton):
        Audio *= 32767 / np.max(np.abs(Audio))
        Audio = Audio.astype(np.int16)

        self.play_obj = sa.play_buffer(Audio, 1, 2, rate)
        playButton.setEnabled(False)

        if self.play_obj.is_playing() :
            playButton.setEnabled(False)
            QtCore.QTimer.singleShot(self.totalTime *1000, lambda: playButton.setDisabled(False))
    
        print(self.play_obj)
        pushButton.clicked.connect(lambda: self.stop(playButton))
      
        


        
    def stop(self,playButton ):
        # self.play_obj.stop()
        sa.stop_all()
        

        

        
        playButton.setDisabled(False)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    ex = Example()
    sys.exit(app.exec_())
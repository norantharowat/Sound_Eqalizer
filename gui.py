# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newguiTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pyqt practice/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PngItem_2686305.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(9, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.s10 = QtWidgets.QSlider(self.centralwidget)
        self.s10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s10.sizePolicy().hasHeightForWidth())
        self.s10.setSizePolicy(sizePolicy)
        self.s10.setMinimum(-12)
        self.s10.setMaximum(12)
        self.s10.setProperty("value", 1)
        self.s10.setSliderPosition(1)
        self.s10.setOrientation(QtCore.Qt.Vertical)
        self.s10.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s10.setTickInterval(1)
        self.s10.setObjectName("s10")
        self.gridLayout_6.addWidget(self.s10, 0, 9, 1, 1)
        self.s9 = QtWidgets.QSlider(self.centralwidget)
        self.s9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s9.sizePolicy().hasHeightForWidth())
        self.s9.setSizePolicy(sizePolicy)
        self.s9.setMinimum(-12)
        self.s9.setMaximum(12)
        self.s9.setProperty("value", 1)
        self.s9.setSliderPosition(1)
        self.s9.setOrientation(QtCore.Qt.Vertical)
        self.s9.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s9.setTickInterval(1)
        self.s9.setObjectName("s9")
        self.gridLayout_6.addWidget(self.s9, 0, 8, 1, 1)
        self.s6 = QtWidgets.QSlider(self.centralwidget)
        self.s6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s6.sizePolicy().hasHeightForWidth())
        self.s6.setSizePolicy(sizePolicy)
        self.s6.setMinimum(-12)
        self.s6.setMaximum(12)
        self.s6.setProperty("value", 1)
        self.s6.setOrientation(QtCore.Qt.Vertical)
        self.s6.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s6.setTickInterval(1)
        self.s6.setObjectName("s6")
        self.gridLayout_6.addWidget(self.s6, 0, 5, 1, 1)
        self.s5 = QtWidgets.QSlider(self.centralwidget)
        self.s5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s5.sizePolicy().hasHeightForWidth())
        self.s5.setSizePolicy(sizePolicy)
        self.s5.setMinimum(-12)
        self.s5.setMaximum(12)
        self.s5.setProperty("value", 1)
        self.s5.setOrientation(QtCore.Qt.Vertical)
        self.s5.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s5.setTickInterval(1)
        self.s5.setObjectName("s5")
        self.gridLayout_6.addWidget(self.s5, 0, 4, 1, 1)
        self.s4 = QtWidgets.QSlider(self.centralwidget)
        self.s4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s4.sizePolicy().hasHeightForWidth())
        self.s4.setSizePolicy(sizePolicy)
        self.s4.setMinimum(-12)
        self.s4.setMaximum(12)
        self.s4.setProperty("value", 1)
        self.s4.setOrientation(QtCore.Qt.Vertical)
        self.s4.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s4.setTickInterval(1)
        self.s4.setObjectName("s4")
        self.gridLayout_6.addWidget(self.s4, 0, 3, 1, 1)
        self.s3 = QtWidgets.QSlider(self.centralwidget)
        self.s3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s3.sizePolicy().hasHeightForWidth())
        self.s3.setSizePolicy(sizePolicy)
        self.s3.setMinimum(-12)
        self.s3.setMaximum(12)
        self.s3.setProperty("value", 1)
        self.s3.setOrientation(QtCore.Qt.Vertical)
        self.s3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s3.setTickInterval(1)
        self.s3.setObjectName("s3")
        self.gridLayout_6.addWidget(self.s3, 0, 2, 1, 1)
        self.s2 = QtWidgets.QSlider(self.centralwidget)
        self.s2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s2.sizePolicy().hasHeightForWidth())
        self.s2.setSizePolicy(sizePolicy)
        self.s2.setMinimum(-12)
        self.s2.setMaximum(12)
        self.s2.setProperty("value", 1)
        self.s2.setOrientation(QtCore.Qt.Vertical)
        self.s2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s2.setTickInterval(1)
        self.s2.setObjectName("s2")
        self.gridLayout_6.addWidget(self.s2, 0, 1, 1, 1)
        self.s1 = QtWidgets.QSlider(self.centralwidget)
        self.s1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s1.sizePolicy().hasHeightForWidth())
        self.s1.setSizePolicy(sizePolicy)
        self.s1.setMinimum(-12)
        self.s1.setMaximum(12)
        self.s1.setProperty("value", 1)
        self.s1.setOrientation(QtCore.Qt.Vertical)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s1.setTickInterval(1)
        self.s1.setObjectName("s1")
        self.gridLayout_6.addWidget(self.s1, 0, 0, 1, 1)
        self.s8 = QtWidgets.QSlider(self.centralwidget)
        self.s8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s8.sizePolicy().hasHeightForWidth())
        self.s8.setSizePolicy(sizePolicy)
        self.s8.setMinimum(-12)
        self.s8.setMaximum(12)
        self.s8.setProperty("value", 1)
        self.s8.setOrientation(QtCore.Qt.Vertical)
        self.s8.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s8.setTickInterval(1)
        self.s8.setObjectName("s8")
        self.gridLayout_6.addWidget(self.s8, 0, 7, 1, 1)
        self.s7 = QtWidgets.QSlider(self.centralwidget)
        self.s7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s7.sizePolicy().hasHeightForWidth())
        self.s7.setSizePolicy(sizePolicy)
        self.s7.setMinimum(-12)
        self.s7.setMaximum(12)
        self.s7.setProperty("value", 1)
        self.s7.setOrientation(QtCore.Qt.Vertical)
        self.s7.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.s7.setTickInterval(1)
        self.s7.setObjectName("s7")
        self.gridLayout_6.addWidget(self.s7, 0, 6, 1, 1)
        self.band1 = QtWidgets.QLabel(self.centralwidget)
        self.band1.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band1.setFont(font)
        self.band1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.band1.setText("")
        self.band1.setAlignment(QtCore.Qt.AlignCenter)
        self.band1.setObjectName("band1")
        self.gridLayout_6.addWidget(self.band1, 1, 0, 1, 1)
        self.band2 = QtWidgets.QLabel(self.centralwidget)
        self.band2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band2.setFont(font)
        self.band2.setText("")
        self.band2.setAlignment(QtCore.Qt.AlignCenter)
        self.band2.setObjectName("band2")
        self.gridLayout_6.addWidget(self.band2, 1, 1, 1, 1)
        self.band3 = QtWidgets.QLabel(self.centralwidget)
        self.band3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band3.setFont(font)
        self.band3.setText("")
        self.band3.setAlignment(QtCore.Qt.AlignCenter)
        self.band3.setObjectName("band3")
        self.gridLayout_6.addWidget(self.band3, 1, 2, 1, 1)
        self.band4 = QtWidgets.QLabel(self.centralwidget)
        self.band4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band4.setFont(font)
        self.band4.setText("")
        self.band4.setAlignment(QtCore.Qt.AlignCenter)
        self.band4.setObjectName("band4")
        self.gridLayout_6.addWidget(self.band4, 1, 3, 1, 1)
        self.band5 = QtWidgets.QLabel(self.centralwidget)
        self.band5.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band5.setFont(font)
        self.band5.setText("")
        self.band5.setAlignment(QtCore.Qt.AlignCenter)
        self.band5.setObjectName("band5")
        self.gridLayout_6.addWidget(self.band5, 1, 4, 1, 1)
        self.band6 = QtWidgets.QLabel(self.centralwidget)
        self.band6.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band6.setFont(font)
        self.band6.setText("")
        self.band6.setAlignment(QtCore.Qt.AlignCenter)
        self.band6.setObjectName("band6")
        self.gridLayout_6.addWidget(self.band6, 1, 5, 1, 1)
        self.band7 = QtWidgets.QLabel(self.centralwidget)
        self.band7.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band7.setFont(font)
        self.band7.setText("")
        self.band7.setAlignment(QtCore.Qt.AlignCenter)
        self.band7.setObjectName("band7")
        self.gridLayout_6.addWidget(self.band7, 1, 6, 1, 1)
        self.band8 = QtWidgets.QLabel(self.centralwidget)
        self.band8.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band8.setFont(font)
        self.band8.setText("")
        self.band8.setAlignment(QtCore.Qt.AlignCenter)
        self.band8.setObjectName("band8")
        self.gridLayout_6.addWidget(self.band8, 1, 7, 1, 1)
        self.band9 = QtWidgets.QLabel(self.centralwidget)
        self.band9.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band9.setFont(font)
        self.band9.setText("")
        self.band9.setAlignment(QtCore.Qt.AlignCenter)
        self.band9.setObjectName("band9")
        self.gridLayout_6.addWidget(self.band9, 1, 8, 1, 1)
        self.band10 = QtWidgets.QLabel(self.centralwidget)
        self.band10.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.band10.setFont(font)
        self.band10.setText("")
        self.band10.setAlignment(QtCore.Qt.AlignCenter)
        self.band10.setObjectName("band10")
        self.gridLayout_6.addWidget(self.band10, 1, 9, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 4, 0, 1, 1)
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_7.addWidget(self.graphicsView_2, 3, 0, 1, 1)
        self.graphicsView = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_7.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionSave_EQ1 = QtWidgets.QAction(MainWindow)
        self.actionSave_EQ1.setObjectName("actionSave_EQ1")
        self.actionSave_EQ2 = QtWidgets.QAction(MainWindow)
        self.actionSave_EQ2.setObjectName("actionSave_EQ2")
        self.SaveEdit = QtWidgets.QAction(MainWindow)
        self.SaveEdit.setObjectName("SaveEdit")
        self.actionSave_Difference = QtWidgets.QAction(MainWindow)
        self.actionSave_Difference.setObjectName("actionSave_Difference")
        self.actionSave_EQ1_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_EQ1_2.setObjectName("actionSave_EQ1_2")
        self.actionGet_EQ1 = QtWidgets.QAction(MainWindow)
        self.actionGet_EQ1.setObjectName("actionGet_EQ1")
        self.actionSave_EQ2_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_EQ2_2.setObjectName("actionSave_EQ2_2")
        self.actionGet_EQ2 = QtWidgets.QAction(MainWindow)
        self.actionGet_EQ2.setObjectName("actionGet_EQ2")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionSave_EQ1)
        self.menuFile.addAction(self.actionSave_EQ2)
        self.menuResults.addAction(self.actionSave_EQ1_2)
        self.menuResults.addAction(self.actionGet_EQ1)
        self.menuResults.addAction(self.actionSave_EQ2_2)
        self.menuResults.addAction(self.actionGet_EQ2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Original"))
        self.comboBox.setItemText(1, _translate("MainWindow", "EQ1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EQ2"))
        self.label.setText(_translate("MainWindow", "Window"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Rectangular"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Hamming"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Hanning"))
        self.pushButton_3.setText(_translate("MainWindow", "Difference"))
        self.label_2.setText(_translate("MainWindow", "Original"))
        self.label_3.setText(_translate("MainWindow", "Fourier"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_EQ1.setText(_translate("MainWindow", "Save EQ1"))
        self.actionSave_EQ1.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_EQ2.setText(_translate("MainWindow", "Save EQ2"))
        self.SaveEdit.setText(_translate("MainWindow", "Save Edit "))
        self.actionSave_Difference.setText(_translate("MainWindow", "Save Difference "))
        self.actionSave_EQ1_2.setText(_translate("MainWindow", "Save EQ1 data"))
        self.actionGet_EQ1.setText(_translate("MainWindow", "Get EQ1 data"))
        self.actionSave_EQ2_2.setText(_translate("MainWindow", "Save EQ2 data"))
        self.actionGet_EQ2.setText(_translate("MainWindow", "Get EQ2 data"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

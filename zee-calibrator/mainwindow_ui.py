# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Nov 22 08:41:35 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(743, 679)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.filenameLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameLabel.sizePolicy().hasHeightForWidth())
        self.filenameLabel.setSizePolicy(sizePolicy)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.verticalLayout.addWidget(self.filenameLabel)
        self.plotTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.plotTabWidget.setObjectName(_fromUtf8("plotTabWidget"))
        self.wxwyvzTab = QtGui.QWidget()
        self.wxwyvzTab.setObjectName(_fromUtf8("wxwyvzTab"))
        self.plotTabWidget.addTab(self.wxwyvzTab, _fromUtf8(""))
        self.wxvwyTab = QtGui.QWidget()
        self.wxvwyTab.setObjectName(_fromUtf8("wxvwyTab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.wxvwyTab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.wxvwyPlotWidget = QtGui.QWidget(self.wxvwyTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.wxvwyPlotWidget.sizePolicy().hasHeightForWidth())
        self.wxvwyPlotWidget.setSizePolicy(sizePolicy)
        self.wxvwyPlotWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.wxvwyPlotWidget.setAutoFillBackground(False)
        self.wxvwyPlotWidget.setObjectName(_fromUtf8("wxvwyPlotWidget"))
        self.horizontalLayout_2.addWidget(self.wxvwyPlotWidget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.plotTabWidget.addTab(self.wxvwyTab, _fromUtf8(""))
        self.stageTab = QtGui.QWidget()
        self.stageTab.setObjectName(_fromUtf8("stageTab"))
        self.plotTabWidget.addTab(self.stageTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.plotTabWidget)
        self.pixFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixFrame.sizePolicy().hasHeightForWidth())
        self.pixFrame.setSizePolicy(sizePolicy)
        self.pixFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pixFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.pixFrame.setObjectName(_fromUtf8("pixFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.pixFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.powerLabel = QtGui.QLabel(self.pixFrame)
        self.powerLabel.setObjectName(_fromUtf8("powerLabel"))
        self.horizontalLayout.addWidget(self.powerLabel)
        self.powerComboBox = QtGui.QComboBox(self.pixFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerComboBox.sizePolicy().hasHeightForWidth())
        self.powerComboBox.setSizePolicy(sizePolicy)
        self.powerComboBox.setMinimumSize(QtCore.QSize(40, 0))
        self.powerComboBox.setObjectName(_fromUtf8("powerComboBox"))
        self.horizontalLayout.addWidget(self.powerComboBox)
        self.pixelLabel = QtGui.QLabel(self.pixFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelLabel.sizePolicy().hasHeightForWidth())
        self.pixelLabel.setSizePolicy(sizePolicy)
        self.pixelLabel.setObjectName(_fromUtf8("pixelLabel"))
        self.horizontalLayout.addWidget(self.pixelLabel)
        self.pixelSpinBox = QtGui.QDoubleSpinBox(self.pixFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelSpinBox.sizePolicy().hasHeightForWidth())
        self.pixelSpinBox.setSizePolicy(sizePolicy)
        self.pixelSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.pixelSpinBox.setDecimals(1)
        self.pixelSpinBox.setMaximum(1000.0)
        self.pixelSpinBox.setSingleStep(0.1)
        self.pixelSpinBox.setObjectName(_fromUtf8("pixelSpinBox"))
        self.horizontalLayout.addWidget(self.pixelSpinBox)
        self.verticalLayout.addWidget(self.pixFrame)
        self.calLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.calLineEdit.setObjectName(_fromUtf8("calLineEdit"))
        self.verticalLayout.addWidget(self.calLineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Molecule_List = QtGui.QAction(MainWindow)
        self.actionLoad_Molecule_List.setObjectName(_fromUtf8("actionLoad_Molecule_List"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionRedo_Fit = QtGui.QAction(MainWindow)
        self.actionRedo_Fit.setObjectName(_fromUtf8("actionRedo_Fit"))
        self.actionSave_Calibration = QtGui.QAction(MainWindow)
        self.actionSave_Calibration.setObjectName(_fromUtf8("actionSave_Calibration"))
        self.actionLoad_Calibration = QtGui.QAction(MainWindow)
        self.actionLoad_Calibration.setObjectName(_fromUtf8("actionLoad_Calibration"))
        self.actionLoad_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Data.setObjectName(_fromUtf8("actionLoad_Data"))
        self.menuFile.addAction(self.actionLoad_Molecule_List)
        self.menuFile.addAction(self.actionRedo_Fit)
        self.menuFile.addAction(self.actionSave_Calibration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Calibration)
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.plotTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ZeeCalibrator", None))
        self.filenameLabel.setText(_translate("MainWindow", "None", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.wxwyvzTab), _translate("MainWindow", "Wx, Wy vs Z", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.wxvwyTab), _translate("MainWindow", "Wx vs Wy", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.stageTab), _translate("MainWindow", "Stage Calibration", None))
        self.powerLabel.setText(_translate("MainWindow", "Fit Power:", None))
        self.pixelLabel.setText(_translate("MainWindow", "Pixels Per Nanometer:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad_Molecule_List.setText(_translate("MainWindow", "Load Molecule List", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionRedo_Fit.setText(_translate("MainWindow", "Redo Fit", None))
        self.actionSave_Calibration.setText(_translate("MainWindow", "Save Calibration", None))
        self.actionLoad_Calibration.setText(_translate("MainWindow", "Load Calibration", None))
        self.actionLoad_Data.setText(_translate("MainWindow", "Load Data", None))

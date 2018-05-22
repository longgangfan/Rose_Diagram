# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rose_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow, col):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(927, 727)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(927, 727))
        MainWindow.setMaximumSize(QtCore.QSize(927, 727))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 591, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStatusTip("")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setToolTip('The rose Diagram will show here.')
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 10, 20, 689))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(10, 690, 610, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 530, 591, 160))
        self.textBrowser.setToolTip("The detailed report will be showed here!")
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 510, 610, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(610, 10, 20, 689))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(630, 185, 271, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(910, 0, 20, 1011))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 1, 901, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.Plot_bt = QtWidgets.QPushButton(self.centralwidget)
        self.Plot_bt.setGeometry(QtCore.QRect(830, 140, 71, 31))

        self.Plot_bt.setAutoFillBackground(True)
        self.Plot_bt.setObjectName("Plot_bt")
        self.Plot_bt.setToolTip("Plot the rose diagram!")
        self.Plot_bt.setFlat(False)
        self.Cal_bt = QtWidgets.QPushButton(self.centralwidget)
        self.Cal_bt.setGeometry(QtCore.QRect(830, 40, 71, 31))
        self.Cal_bt.setObjectName("Cal_bt")
        self.Cal_bt.setFlat(False)
        self.Cal_bt.setToolTip("Calibrate the Datas by rotating the strata to horizontal level!")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 20, 161, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 41, 27))
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip('Please input pure number from 0 to 360, degree character is not needed.')
        self.lineEdit.setValidator(QtGui.QDoubleValidator(0.0, 359.9, 1, self.lineEdit))
        self.lineEdit.setStyleSheet("color:red")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 60, 41, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setToolTip('Please input pure number from 0 to 90, degree character is not needed.')
        self.lineEdit_2.setValidator(QtGui.QDoubleValidator(0.1, 89.9, 1, self.lineEdit_2))
        self.lineEdit_2.setStyleSheet("color:red")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 90, 131, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setToolTip("Whether the Strata is overturned!")
        self.Clear_bt = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_bt.setGeometry(QtCore.QRect(830, 90, 71, 31))
        self.Clear_bt.setObjectName("Clear_bt")
        self.Clear_bt.setFlat(False)
        self.Clear_bt.setToolTip("Clear all the Panels and table for new start!")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(730, 150, 61, 27))
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(360)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setToolTip("Chose the interval for rose diagram pedal by degree!")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(810, 30, 20, 151))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 150, 68, 31))
        self.label_3.setObjectName("label_3")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(775, 200, 15, 30))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(630, 180, 271, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(800, 30, 20, 151))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(900, 30, 20, 151))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(630, 230, 281, 469))
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(col)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Azimuth', 'Dip', 'Azimuth', 'Dip'])
        self.tableWidget.horizontalHeader().resizeSection(0, 60)
        self.tableWidget.horizontalHeader().resizeSection(1, 54)
        self.tableWidget.horizontalHeader().resizeSection(2, 60)
        self.tableWidget.horizontalHeader().resizeSection(3, 54)
        self.tableWidget.verticalHeader().setDefaultSectionSize(18)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setObjectName("tableWidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 200, 110, 27))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip('Copy your datas to Clipboard by hand first ' +
                                   'and then click here, it will paste the datas ' +
                                   'to the first two columns below.\n *Note: the column ' + 
                                   'headers are not needed here, pure numbers are prefered.\n' + 
                                   'Maybe, you just see 1000 rows in the table, but you can paste ' + 
                                   'more rows than you saw.')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(793, 200, 110, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip('Export the Calibrated datas to StereoNet format, if you want.')
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 927, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
#        self.actionExport = QtWidgets.QAction(MainWindow)
#        self.actionExport.setObjectName("actionExport")
        self.actionSave_Figure = QtWidgets.QAction(MainWindow)
        self.actionSave_Figure.setObjectName("actionSave_Figure")
        self.actionSave_Report = QtWidgets.QAction(MainWindow)
        self.actionSave_Report.setObjectName("actionSave_Report")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.actionImport)
        self.menu_File.addAction(self.actionSave_Figure)
        self.menu_File.addAction(self.actionSave_Report)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        self.checkBox.stateChanged['int'].connect(self.Cal_bt.click)
        self.spinBox.valueChanged['int'].connect(self.Plot_bt.update)
        self.Plot_bt.clicked.connect(self.graphicsView.update)
        self.Plot_bt.clicked.connect(self.textBrowser.update)
        self.Clear_bt.clicked.connect(self.graphicsView.update)
        self.Clear_bt.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rose"))
        self.graphicsView.setWhatsThis(_translate("MainWindow", "Paste your measurements from clipboard"))
        self.Plot_bt.setText(_translate("MainWindow", "Plot"))
        self.Cal_bt.setText(_translate("MainWindow", "Cal"))
        self.groupBox.setTitle(_translate("MainWindow", "Strata Attitude"))
        self.label.setText(_translate("MainWindow", "Dip Direction"))
        self.label_2.setText(_translate("MainWindow", "Dip Angle"))
        self.checkBox.setText(_translate("MainWindow", "Overturned"))
        self.Clear_bt.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Intervals"))
        self.tableWidget.setSortingEnabled(False)
        self.pushButton.setText(_translate("MainWindow", "Paste Raw"))
        self.pushButton_2.setText(_translate("MainWindow", "Exp2Stere"))
        self.menu_File.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionSave_Figure.setText(_translate("MainWindow", "Save Figure"))
        self.actionSave_Report.setText(_translate("MainWindow", "Save Report"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    def browser(self, filetype):
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Picture',  
                                                             '', filetype)
            fname = filename[0]
            return fname


    def opener(self, filetype):
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'import file',  
                                                             '', filetype)
            fname = filename[0]
            return fname

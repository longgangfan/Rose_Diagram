import sys
import io
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from rose_mainwindow import Ui_MainWindow as win
import plots
import re
import calibrator
import shutil
from about import Ui_About


def clearfile():
    if os.path.exists('report.rose'):
        os.remove('report.rose')
    if os.path.exists('data.rose'):
        os.remove('data.rose')
    if os.path.exists('raw.rose'):
        os.remove('raw.rose')
    if os.path.exists('tmprose.pdf'):
        os.remove('tmprose.pdf')


clearfile()

global colu_cnt
colu_cnt = 9999
app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icon.png'))
window = QMainWindow()
ui = win()
ui.setupUi(window, colu_cnt)
window.show()


def isnumber(num):
    regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    if re.match(regex, num):
        return True
    else:
        return False


def checkdata(data1, data2):
    if (isnumber(data1) and isnumber(data2) and (0 <= float(data1) < 360) and
       (0 <= float(data2) <= 90)):
        return True
    else:
        return False


def pltpic0():
    if os.path.exists('data.rose'):
        pltpic(ui.spinBox.value())
    else:
        ui.statusbar.showMessage('Please Input and Calibrate first!')


def pltpic(interval):
    graphicscene = QtWidgets.QGraphicsScene()
    dr = plots.Figca()
    dr.plotpic(interval)
    graphicscene.addWidget(dr)
    ui.graphicsView.setScene(graphicscene)
    ui.statusbar.showMessage('Plot Done!')


def rmpic():
    graphicscene = QtWidgets.QGraphicsScene()
    dr = plots.Figca()
    dr.rm_pic()
    graphicscene.addWidget(dr)
    ui.graphicsView.setScene(graphicscene)


def rmreport():
    ui.textBrowser.clear()


def readreport():
    if os.path.exists('report.rose'):
        report = open(r'report.rose', 'r').read()
        ui.textBrowser.setPlainText(report)
    else:
        rmreport


def cleartable():
    ui.tableWidget.clearContents()


def clearlineedit():
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()


def PasteText():
    cleartable()
    rmreport()
    rmpic()
    clipboard = QApplication.clipboard()
    fpaste = io.StringIO('pastetmp')
    print(clipboard.text(), file=fpaste)
    fpaste.seek(0)
    pastelines = fpaste.readlines()
    pastelist = []
    rawfile = open(r'raw.rose', 'w')
    print(''.join(pastelines), file=rawfile)
    rawfile.close()
    for myline in pastelines:
        if myline != '\n':
            pastelist.append([i for i in myline.split()])
    fpaste.close()
    if len(pastelist) != 0:
        err = 0
        for i in range(len(pastelist)):
            if len(pastelist[i]) < 2:
                err = err + 1
        if err == 0:
            counts = 0
            invalid = 0
            mytable = ui.tableWidget
            ui.statusbar.showMessage('Waiting...')
            for i in range(len(pastelist)):
                if (checkdata(pastelist[i][0], pastelist[i][1])):
                    newItem = QTableWidgetItem(str(pastelist[i][0]))
                    mytable.setItem(i, 0, newItem)
                    mytable.item(i, 0).setTextAlignment(Qt.AlignHCenter |
                                                        Qt.AlignVCenter)
                    mytable.item(i, 0).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
                    newItem = QTableWidgetItem(str(pastelist[i][1]))
                    mytable.setItem(i, 1, newItem)
                    mytable.item(i, 1).setTextAlignment(Qt.AlignHCenter |
                                                        Qt.AlignVCenter)
                    mytable.item(i, 1).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
                    counts = counts + 1
                    ui.statusbar.showMessage(str(counts) + ' Datas Pasted!')
                else:
                    newItem = QTableWidgetItem('')
                    mytable.setItem(i, 0, newItem)
                    mytable.item(i, 0).setTextAlignment(Qt.AlignHCenter |
                                                        Qt.AlignVCenter)
                    newItem = QTableWidgetItem('')
                    mytable.setItem(i, 1, newItem)
                    mytable.item(i, 1).setTextAlignment(Qt.AlignHCenter |
                                                        Qt.AlignVCenter)
                    invalid = invalid + 1
            ui.statusbar.showMessage(str(counts) + ' Valid Datas were pasted and ' + str(invalid) + ' Invalid were not pasted')
        else:
            ui.statusbar.showMessage('Nothing to paste!')
    else:
        ui.statusbar.showMessage('Nothing to paste!')
    fpaste.close()
    del pastelist


def PasteText0():
    clearfile()
    clearlineedit()
    PasteText()


def Checkbox_0():
    if ui.checkBox.isChecked():
        return True
    else:
        return False


def lineeditfun(tmp):
    tmp.append(ui.lineEdit.text())
    tmp.append(ui.lineEdit_2.text())
    return tmp


def Calibrate():
    tmp = []
    tmp = lineeditfun(tmp)
    cnt = []
    invalid = []
    empty = []
    for i in range(colu_cnt):
        if (ui.tableWidget.item(i, 0) and ui.tableWidget.item(i, 1)):
            if checkdata(ui.tableWidget.item(i, 0).text(), ui.tableWidget.item(i, 1).text()): 
                cnt.append(i)
            else:
                invalid.append(i)
        else:
            empty.append(i)
    if (tmp[0] == '' or tmp[1] == '' or cnt == 0 or checkdata(tmp[0], tmp[1])==False):
        ui.statusbar.showMessage('Please input the strata attitudes '
                                 'and measurements!')
    else:
        mytable = ui.tableWidget
        ui.statusbar.showMessage('ready')
        fdata = open(r'data.rose', 'w')
        for i in cnt:
            cur0 = ui.tableWidget.item(i, 0)
            cur1 = ui.tableWidget.item(i, 1)
            cur0_t = cur0.text()
            cur1_t = cur1.text()
            cur0_n = float(cur0_t)
            cur1_n = float(cur1_t)
            stra0 = float(tmp[0])
            stra1 = float(tmp[1])
            state = Checkbox_0()
            caled = calibrator.rotate(cur0_n, cur1_n, stra0,
                                      stra1, state)
            print('%s    %s' % (str(caled[0]), str(caled[1])), file=fdata)
            newItem = QTableWidgetItem(str(caled[0]))
            mytable.setItem(i, 2, newItem)
            mytable.item(i, 2).setTextAlignment(Qt.AlignHCenter
                                                | Qt.AlignVCenter)
            mytable.item(i, 2).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))

            newItem = QTableWidgetItem(str(caled[1]))
            mytable.setItem(i, 3, newItem)
            mytable.item(i, 3).setTextAlignment(Qt.AlignHCenter
                                                | Qt.AlignVCenter)
            mytable.item(i, 3).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))

            ui.statusbar.showMessage('Working...')
        fdata.close()
        if len(cnt) >= 1:
            for i in invalid:
                newItem = QTableWidgetItem('')
                mytable.setItem(i, 2, newItem)
                mytable.item(i, 2).setTextAlignment(Qt.AlignHCenter
                                                    | Qt.AlignVCenter)
                newItem = QTableWidgetItem('')
                mytable.setItem(i, 3, newItem)
                mytable.item(i, 3).setTextAlignment(Qt.AlignHCenter
                                                    | Qt.AlignVCenter)
            for i in list(filter(lambda x: x<= max(cnt), empty)):
                newItem = QTableWidgetItem('')
                mytable.setItem(i, 2, newItem)
                mytable.item(i, 2).setTextAlignment(Qt.AlignHCenter
                                                    | Qt.AlignVCenter)
                newItem = QTableWidgetItem('')
                mytable.setItem(i, 3, newItem)
                mytable.item(i, 3).setTextAlignment(Qt.AlignHCenter
                                                    | Qt.AlignVCenter)           
        ui.statusbar.showMessage('Calibrate Done!')


def savepic():
    if os.path.exists('tmprose.pdf'):
        filename = ui.browser("Adobe Acrobat (*.pdf)")
        if filename != '':
            shutil.move('tmprose.pdf', filename)
            ui.statusbar.showMessage('Figure saved!')
    else:
        ui.statusbar.showMessage('Please plot first!')


def savereport():
    if os.path.exists('report.rose') and os.path.exists('data.rose') and os.path.exists('raw.rose'):
        filename = ui.browser("Text Files (*.txt)")
        if filename != '':
            resfile = open(filename, 'w')
            refile = open(r'report.rose', 'r')
            lines = refile.readlines()
            refile.close()
            resfile.writelines(lines)
            resfile.write("-----------Raw Datas------------\n\n")
            rawfile = open(r'raw.rose', 'r')
            lines = rawfile.readlines()
            rawfile.close()
            resfile.writelines(lines)
            resfile.write("-----------Calibrated Datas------------\n\n")
            calfile = open(r'data.rose', 'r')
            lines = calfile.readlines()
            calfile.close()
            resfile.writelines(lines)
            resfile.close()
            
            ui.statusbar.showMessage('report saved!')


def importfile():
    filename = ui.opener("All Files (*);;Text Files (*.txt)")
    if filename != '':
        imfile = open(filename, 'r')
        imlines = imfile.readlines()
        imfile.close()
        tmpclip = QApplication.clipboard()
        tmpclip.setText(''.join(imlines))
        PasteText0()

def export_ste():
    if os.path.exists('data.rose'):
        filename = ui.browser("Text Files (*.txt)")
        if filename != '':
            sterfile = open(filename, 'w')
            rosefile = open('data.rose', 'r')
            roselines = rosefile.readlines()
            tmptext =[]
            i = 0
            for line in roselines:
                tmptext.append(line.split())
                print(str(tmptext[i][0]) + '   ' + str(tmptext[i][1]) + 
                      '      P      {Cross	12	0	0	-1', file=sterfile)
                i = i + 1
            sterfile.close()
            rosefile.close()

def showabout():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_About()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
    dialog.show()


ui.Plot_bt.clicked.connect(pltpic0)
ui.Plot_bt.clicked.connect(readreport)
ui.Clear_bt.clicked.connect(rmpic)
ui.Clear_bt.clicked.connect(rmreport)
ui.Clear_bt.clicked.connect(cleartable)
ui.Clear_bt.clicked.connect(clearfile)
ui.Clear_bt.clicked.connect(clearlineedit)
ui.spinBox.valueChanged['int'].connect(pltpic0)
ui.spinBox.valueChanged['int'].connect(readreport)
ui.pushButton.clicked.connect(PasteText0)
ui.checkBox.stateChanged['int'].connect(Checkbox_0)
ui.Cal_bt.clicked.connect(Calibrate)
ui.lineEdit.editingFinished.connect(Calibrate)
ui.lineEdit_2.editingFinished.connect(Calibrate)
ui.actionSave_Figure.triggered.connect(savepic)
ui.actionSave_Report.triggered.connect(savereport)
ui.actionImport.triggered.connect(importfile)
ui.pushButton_2.clicked.connect(export_ste)
ui.actionAbout.triggered.connect(showabout)
sys.exit(app.exec_())

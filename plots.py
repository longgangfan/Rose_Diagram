import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.figure import Figure
import matplotlib.patches as pat
from itertools import groupby
import os
import re


def isnumber(num):
    regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    if re.match(regex, num):
        return True
    else:
        return False


class Figca(FigCanvas):
    # 通过继承FigureCanvas类，使得该类既是
    # 一个PyQt5的Qwidget，又是一个matplotli
    # b的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None):
        figure = Figure(figsize=(6.9, 6.9), dpi=72)
        FigCanvas.__init__(self, figure)  # 初始化父类
        self.setParent(parent)
        self.ax = figure.add_subplot(111)
        self.ax.axis('off')  # close the axis

    def plotpic(self, interd=10):
# Begin to draw circle and wedges

# plot all the wedges

         # first step read the data from the file
        if os.path.exists('data.rose'):
            f = open(r"data.rose", "r")  # open the file as a object
            lines = f.readlines()
            f.close()
            mylist0 = []             # creat an arrary

            peak = 0
            for line in lines:
                if line != '\n':
                    mylist0.append(line.split())  # read the
# contents to a numberic list, "extend" is perfect
            print(mylist0)
            total0 = len(mylist0)
            mylist=[]
            for i in range(total0):
                if (isnumber(mylist0[i][0])):
                    mylist.append(float(mylist0[i][0]))
            total = len(mylist)

            grpnum = 0              # group number
            petal = []  # group array, use the middle degree as the pedal
            petal_n = []
            for k, g in groupby(sorted(mylist), key=lambda x: x // (interd*1.0)):
                templist = list(g)  # Here is something strange, list(g) can only be used
# one time, when the second list(g) will return null
                petal.append(round(sum(templist)/len(templist), 1))
                petal_n.append(len(templist))
                grpnum = grpnum + 1
# Recalculate the number
            ratios = []
            for t in range(grpnum):
                ratios.append(round(petal_n[t] / total * 1.0 * 100, 1))
# Append all the list
            newlist = list(zip(petal, petal_n, ratios))
            del petal
            del petal_n
# get the average ratio
            avratio = sum(ratios) / grpnum
            del ratios
# Order by numbers
            for p in range(grpnum-1):
                maxone = newlist[p]
                flag = p
                for t in range(p+1, grpnum):
                    if newlist[t][1] > maxone[1]:
                       maxone = newlist[t]
                       flag = t
                bridge = newlist[p]
                newlist[p] = newlist[flag]
                newlist[flag] = bridge
            peaks = []
            for t in range(grpnum):
                if newlist[t][2] >= avratio:
                   peaks.append(newlist[t][2])
                   peak = peak + 1
            peak1 = 0
            for t in range(peak):
                if peaks[t] >= sum(peaks)/peak:
                   peak1 = peak1 + 1
            maxmeas = []
            maxnums = []
            maxratios = []
            for t in range(peak1):
                maxmeas.append(str(newlist[t][0]))
                maxnums.append(str(newlist[t][1]))
                maxratios.append(str(newlist[t][2]))
            maxmea = ' | '.join(maxmeas)
            maxnum = ' | '.join(maxnums)
            maxratio = '% | '.join(maxratios)

####

            pedalwedges = []
            for t in range(grpnum):
                if newlist[t][0] < 90:
                    startdeg = 90 - newlist[t][0] + interd / 2.0
                else:
                    startdeg = 450 - newlist[t][0] + interd / 2.0
                pedalwedges.append(pat.Wedge((0, 0), (newlist[t][2] * 100 / newlist[0][2]),
                           startdeg - interd, startdeg, linewidth=2, fill=True, color='b'))
                self.ax.add_patch(pedalwedges[t])
# First step plot a circle
            self.ax.add_patch(pat.Circle((0, 0), 100, fill=False, linewidth=2))
            self.ax.plot()
            del pedalwedges
# plot the North
            self.ax.plot([0, 0], [100.5, 102], color='black')
            self.ax.plot([0, 0], [-100.5, -102], color='black')
            self.ax.plot([-102, -100.5], [0, 0], color='black')
            self.ax.plot([100.5, 102], [0, 0], color='black')
            self.ax.text(0, 102.5, 'N', horizontalalignment='center', fontsize=10)
            self.ax.text(-140, -130, 'Total valid Measurements:' + ' ' + str(total) + '; and the'
                    ' Petal interval is: ' + str(interd) + ' Deg.', fontsize=10)
#            self.ax.text(-140, -123, 'Dominant ' + str(peak1) + ' Group(s) is/are ' + ' ' +
#            maxmea + ' Deg clockwise from the North.', fontsize=10)
#            self.ax.text(-140, -131, 'The Measurements is/are:' +
#                    str(maxnum) + ', and it/(they) take(s) ' + str(maxratio) + '%.',
#                    fontsize=10)
            self.ax.text(-140, 131, 'The Dominant ' + str(peak1) +
                    ' Group(s)', fontsize=10)
            self.ax.text(-140, 123, '(Direc, Mea, Ratio)', color='b', fontsize=10)
            y = 115
            for t in range(peak1):
                self.ax.text(-140, y, str(newlist[t]), fontsize=10)
                y = y - 8
            f2 = open(r'report.rose', 'w')
            ivalid = total0 - total
            print('\t\tThis is the Detailed report:\n', file=f2)
            print('The total valid Measurements:%8d\n' % total, file=f2)
            print('The total invalid Measurements:%6d\n' % ivalid, file=f2)
            print('The interval Degree:%17d\n' % interd, file=f2)
            print('The Group number:%20d\n' % grpnum, file=f2)
            print('     Group Direction     Measurements\tRatios\n',file= f2)

            for t in range(grpnum):
                for i in range(3):
                    if i == 0:
                        print('%15.1f,' % newlist[t][i], end='', file=f2)
                    if i == 1:
                        print('%15d,' % int(newlist[t][i]), end='', file=f2)
                    if i == 2:
                        print('%17.1f%%' % newlist[t][i], end='', file=f2)
                print('\n',file=f2)
            f2.close()
            del newlist
            self.figure.savefig('tmprose.pdf', dpi=150)
        else:
            pass
 
   
    def rm_pic(self):  # make a empty function and do nothing
        pass

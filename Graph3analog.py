import serial
import numpy
from pyqtgraph.Qt import QtGui, QtCore
import matplotlib.pyplot as plt
import pyqtgraph as pg
from drawnow import *

app = QtGui.QApplication([])

inputData = serial.Serial('/dev/ttyACM0',115200)
count=0
cnt=0
ana1=[]
ana2=[]

plt.ion()

p1 = pg.plot(title='3 analog')
curve = p1.plot(pen='y')
def makeFig():
    plt.ylim(0,1030)
    plt.xlim(0,50)
    plt.plot(ana1, 'bo-')
    plt.plot(ana2, 'ro-')

while True:
    while (inputData.inWaiting() == 0):
        pass
    while (count<2):
        string = inputData.readline()
        count=count+1

    string = inputData.readline()    
    stringData = string.split(b',')
    if(len(stringData)==3):
        analog1 = int(stringData[0])
        analog2 = int(stringData[1])
        analog3 = int(stringData[2].split(b'\r\n')[0])
        #ana1.append(analog1)
        #ana2.append(analog2)
        #ana01=numpy.array(ana1)
        #curve.setData(ana01)
        print(analog1,', ',analog2,', ',analog3)
        cnt=cnt+1
        if(cnt>50):
            ana1.pop(0)
            ana2.pop(0)
        
pg.QtGui.QApplication.instance().exec_()
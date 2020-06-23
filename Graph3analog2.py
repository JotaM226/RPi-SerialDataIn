import serial
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
count=0
inputData = serial.Serial('/dev/ttyACM0',9600)

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)


p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
if (inputData.inWaiting() != 0):
    if (count<2):
        string = inputData.readline()    
        stringData = string.split(b' , ')
        if(len(stringData)==2):
            analog1 = int(stringData[0])
            analog2 = int(stringData[1].split(b'\r\n')[0])
            
    else:
        string = inputData.readline()
        count=count+1
def update():
    global curve, p6
    curve.setData(analog1)
    
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

win.nextRow()


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
        
        
        
        
        
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
count =0

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="test")
win.resize(700,400)
win.setWindowTitle('pyqtgraph example: Plotting')
pg.setConfigOptions(antialias=True)

p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')

inputData = serial.Serial('/dev/ttyACM0',9600)


while True:
    while (inputData.inWaiting() == 0):
        pass
    while (count<2):
        string = inputData.readline()
        count=count+1

    string = inputData.readline()    
    stringData = string.split(b' , ')
    if(len(stringData)==2):
        analog1 = int(stringData[0])
        analog2 = int(stringData[1].split(b'\r\n')[0])
        data = analog1
        curve.setData(data)
    

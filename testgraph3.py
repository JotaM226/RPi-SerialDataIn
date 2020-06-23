# Import libraries
from numpy import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial

# Create object serial port

ser = serial.Serial('/dev/ttyACM0',9600)

### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)
####################

win = pg.GraphicsWindow(title="Gáfica de señal analógica") # creates a window
#win.resize(750,350)
p = win.addPlot(title="muestras cada 25ms")  # creates empty space for the plot in the window
p.setYRange(0,1050,padding=None,update=False)
curve = p.plot()                        # create an empty "plot" (a curve to plot)

windowWidth = 100                       # width of the window displaying the curve
Xm = linspace(0,0,windowWidth)          # create array that will contain the relevant time series     
ptr = 0                     # set first x position

# Realtime data plot. Each time this function is called, the data display is updated
def update():
    global curve, ptr, Xm    
    Xm[:-1] = Xm[1:]                      # shift data in the temporal mean 1 sample left
    string = ser.readline()                # read line (single value) from the serial port
    stringData = string.split(b',')
    if(len(stringData)==2):
        analog1 = int(stringData[0])
        analog2 = int(stringData[1].split(b'\r\n')[0])
        Xm[-1] = analog1                 # vector containing the instantaneous values      
        ptr += 1                              # update x position for displaying the curve
        curve.setData(Xm)                     # set the curve with this data
        curve.setPos(ptr,0)                   # set x position in the graph to 0
        QtGui.QApplication.processEvents()    # you MUST process the plot now

### MAIN PROGRAM #####    
# this is a brutal infinite loop calling your realtime data plot
while True: update()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################
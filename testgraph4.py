# Import libraries
from numpy import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial
import time

# Create object serial port

ser = serial.Serial('/dev/ttyACM0',115200)
global curve1, curve2, curve3, ptr1, ptr2, ptr3, Xm1, Xm2, Xm3 

### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)
####################

win = pg.GraphicsWindow(title="Gáfica de señales analógicas") # creates a window
#win.resize(750,350)
p1 = win.addPlot(title="señal 1",row=1, col=0)  # creates empty space for the plot in the window
p1.setYRange(0,1050,padding=None,update=False)
curve1 = p1.plot(pen=(0,128,255))                        # create an empty "plot" (a curve to plot)

p2 = win.addPlot(title="señal 2",row=2, col=0)  # creates empty space for the plot in the window
p2.setYRange(0,1050,padding=None,update=False)
curve2 = p2.plot(pen=(255,255,0))

p3 = win.addPlot(title="señal 3",row=3, col=0)  # creates empty space for the plot in the window
p3.setYRange(0,1050,padding=None,update=False)
curve3 = p3.plot(pen=(50,230,25))

graphWidth1 = 500                       # width of the window displaying the curve
Xm1 = linspace(0,0,graphWidth1)          # create array that will contain the relevant time series     
ptr1 = 0                     # set first x position

graphWidth2 = 500                       # width of the window displaying the curve
Xm2 = linspace(0,0,graphWidth2)          # create array that will contain the relevant time series     
ptr2 = 0                     # set first x position

graphWidth3 = 500                       # width of the window displaying the curve
Xm3 = linspace(0,0,graphWidth3)          # create array that will contain the relevant time series     
ptr3 = 0  

# Realtime data plot. Each time this function is called, the data display is updated
def update():
    start = time.time()
    if (ser.inWaiting()>0):
        Xm1[:-1] = Xm1[1:]                      # shift data in the temporal mean 1 sample left
        Xm2[:-1] = Xm2[1:]
        Xm3[:-1] = Xm3[1:]
        string = ser.readline()                # read line (single value) from the serial port
        stringData = string.split(b',')
        if(len(stringData)==3):
            analog1 = int(stringData[0])
            analog2 = int(stringData[1])
            analog3 = int(stringData[2].split(b'\r\n')[0])
            Xm1[-1] = analog1                 # vector containing the instantaneous values      
            Xm2[-1] = analog2 
            Xm3[-1] = analog3
            
            
            #ptr1 += 1                              # update x position for displaying the curve
            #ptr2 += 1 
            #ptr3 += 1 
            
            curve1.setData(Xm1)                     # set the curve with this data
            curve2.setData(Xm2)
            curve3.setData(Xm3)
            
            #curve1.setPos(ptr1,0)                   # set x position in the graph to 0
            #curve2.setPos(ptr2,0)  
            #curve2.setPos(ptr2,0)
            
            QtGui.QApplication.processEvents()    # you MUST process the plot now
            
            stop = time.time()
            time1 = stop - start
            print("execTime: ", time1)
### MAIN PROGRAM #####    
# this is a brutal infinite loop calling your realtime data plot
while True: update()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################
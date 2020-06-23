from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

p6 = pg.plot(title="Updating plot")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000))
ptr = 0
def update():
    global curve, data, ptr, p6
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

QtGui.QApplication.instance().exec_()
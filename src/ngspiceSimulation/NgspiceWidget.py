from PyQt4 import QtGui,QtCore
from configuration.Appconfig import Appconfig

class NgspiceWidget(QtGui.QWidget):
    """
    This Class creates NgSpice Window
    """
    def __init__(self,command):
        QtGui.QWidget.__init__(self)
        self.obj_appconfig = Appconfig()
        self.command = "ngspice "+command
        
        self.process = QtCore.QProcess(self)
        self.terminal = QtGui.QWidget(self)
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.terminal)
        
        #Creating argument for process
        self.args = ['-into', str(self.terminal.winId()),'-hold','-e', self.command]
        self.process.start('xterm', self.args)
               
        #Adding PID
        #self.obj_appconfig.procThread_list.append(self.process.pid())
        
        
        



import serial
import sys
import time
import thread
from PyQt4 import QtCore, QtGui, Qt
from gui import Ui_Calibrcao


port = '/dev/tty.HC-05-DevB'
arduino = serial.Serial(port, baudrate=9600)

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Calibrcao()
        self.ui.setupUi(self)
        self.threshold = 200

        self.ui.textEdit_threshold.setText(str(self.threshold))
        self.ui.pushButton_less.clicked.connect(self.less)
        self.ui.pushButton_more.clicked.connect(self.more)


        self.open()


    def more(self):
        self.threshold += 10
        self.ui.textEdit_threshold.setText(str(self.threshold))

    def less(self):
        self.threshold -= 10
        self.ui.textEdit_threshold.setText(str(self.threshold))

    def open(self):
        print "open"
        thread.start_new_thread(self.reading, ())

    def reading(self):
        while True:
            print 'reading'

            msg = arduino.read(1)
            time.sleep(0.01)
            msg += arduino.read(arduino.inWaiting())
            msg = msg.split()
            i = 1
            try:
                m = msg[0]
            except Exception:
                m = '0'
            # m = msg[0]
            while len(m) < 4 and i < len(msg):
                m = msg[i]
                i += 1
            print msg
            print m
            # self.ui.textEdit_accel.append(msg)
            try:
                self.ui.lineEdit.setText(m)
                accel = float(m)
            except Exception:
                m = '0'
                self.ui.lineEdit.setText(m)
                accel = 0
            if abs(accel)  > self.threshold:
                self.ui.checkBox.setChecked(True)
            else:
                self.ui.checkBox.setChecked(False)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Calibrcao(object):
    def setupUi(self, Calibrcao):
        Calibrcao.setObjectName(_fromUtf8("Calibrcao"))
        Calibrcao.resize(247, 174)
        self.textEdit_threshold = QtGui.QTextEdit(Calibrcao)
        self.textEdit_threshold.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.textEdit_threshold.setFont(font)
        self.textEdit_threshold.setObjectName(_fromUtf8("textEdit_threshold"))
        self.pushButton_more = QtGui.QPushButton(Calibrcao)
        self.pushButton_more.setGeometry(QtCore.QRect(10, 10, 110, 32))
        self.pushButton_more.setObjectName(_fromUtf8("pushButton_more"))
        self.pushButton_less = QtGui.QPushButton(Calibrcao)
        self.pushButton_less.setGeometry(QtCore.QRect(10, 90, 110, 32))
        self.pushButton_less.setObjectName(_fromUtf8("pushButton_less"))
        self.checkBox = QtGui.QCheckBox(Calibrcao)
        self.checkBox.setGeometry(QtCore.QRect(60, 130, 143, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit = QtGui.QLineEdit(Calibrcao)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Calibrcao)
        QtCore.QMetaObject.connectSlotsByName(Calibrcao)

    def retranslateUi(self, Calibrcao):
        Calibrcao.setWindowTitle(_translate("Calibrcao", "Form", None))
        self.textEdit_threshold.setHtml(_translate("Calibrcao", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:21pt;\">0</span></p></body></html>", None))
        self.pushButton_more.setText(_translate("Calibrcao", "+", None))
        self.pushButton_less.setText(_translate("Calibrcao", "-", None))
        self.checkBox.setText(_translate("Calibrcao", "Movimento", None))


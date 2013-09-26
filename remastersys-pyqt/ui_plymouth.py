# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plymouth.ui'
#
# Created: Wed Aug 28 20:37:36 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Plymouth(object):
    def setupUi(self, Plymouth):
        Plymouth.setObjectName(_fromUtf8("Plymouth"))
        Plymouth.resize(715, 580)
        Plymouth.setMinimumSize(QtCore.QSize(715, 580))
        Plymouth.setMaximumSize(QtCore.QSize(715, 580))
        self.label = QtGui.QLabel(Plymouth)
        self.label.setGeometry(QtCore.QRect(20, 10, 661, 141))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/remastersys-large.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Plymouth)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 391, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(Plymouth)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 520, 671, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.selectBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.selectBtn.setMaximumSize(QtCore.QSize(163, 35))
        self.selectBtn.setObjectName(_fromUtf8("selectBtn"))
        self.horizontalLayout.addWidget(self.selectBtn)
        self.newBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.newBtn.setMaximumSize(QtCore.QSize(163, 35))
        self.newBtn.setObjectName(_fromUtf8("newBtn"))
        self.horizontalLayout.addWidget(self.newBtn)
        self.previewBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.previewBtn.setMaximumSize(QtCore.QSize(163, 35))
        self.previewBtn.setObjectName(_fromUtf8("previewBtn"))
        self.horizontalLayout.addWidget(self.previewBtn)
        self.backBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.backBtn.setMaximumSize(QtCore.QSize(163, 35))
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.horizontalLayout.addWidget(self.backBtn)
        self.listWidget = QtGui.QListWidget(Plymouth)
        self.listWidget.setGeometry(QtCore.QRect(20, 190, 671, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Plymouth)
        QtCore.QMetaObject.connectSlotsByName(Plymouth)

    def retranslateUi(self, Plymouth):
        Plymouth.setWindowTitle(QtGui.QApplication.translate("Plymouth", "Plymouth Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Plymouth", "Select Default Plymouth Theme for System", None, QtGui.QApplication.UnicodeUTF8))
        self.selectBtn.setText(QtGui.QApplication.translate("Plymouth", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.newBtn.setText(QtGui.QApplication.translate("Plymouth", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.previewBtn.setText(QtGui.QApplication.translate("Plymouth", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.backBtn.setText(QtGui.QApplication.translate("Plymouth", "Back", None, QtGui.QApplication.UnicodeUTF8))

import remastersys_rc

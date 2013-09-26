# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usersetting.ui'
#
# Created: Wed Aug 28 20:39:54 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UserSetting(object):
    def setupUi(self, UserSetting):
        UserSetting.setObjectName(_fromUtf8("UserSetting"))
        UserSetting.resize(715, 580)
        UserSetting.setMinimumSize(QtCore.QSize(715, 580))
        UserSetting.setMaximumSize(QtCore.QSize(715, 580))
        self.label = QtGui.QLabel(UserSetting)
        self.label.setGeometry(QtCore.QRect(20, 10, 661, 141))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/remastersys-large.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(UserSetting)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 451, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(UserSetting)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 520, 671, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.selectBtn.setMinimumSize(QtCore.QSize(163, 35))
        self.selectBtn.setMaximumSize(QtCore.QSize(163, 35))
        self.selectBtn.setObjectName(_fromUtf8("selectBtn"))
        self.horizontalLayout.addWidget(self.selectBtn)
        self.listWidget = QtGui.QListWidget(UserSetting)
        self.listWidget.setGeometry(QtCore.QRect(20, 190, 671, 331))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(UserSetting)
        QtCore.QMetaObject.connectSlotsByName(UserSetting)

    def retranslateUi(self, UserSetting):
        UserSetting.setWindowTitle(QtGui.QApplication.translate("UserSetting", "User Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("UserSetting", "Select User whose settings will be copied to /etc/skel", None, QtGui.QApplication.UnicodeUTF8))
        self.selectBtn.setText(QtGui.QApplication.translate("UserSetting", "Select", None, QtGui.QApplication.UnicodeUTF8))

import remastersys_rc

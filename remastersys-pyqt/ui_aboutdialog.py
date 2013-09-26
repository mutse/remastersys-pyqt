# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created: Thu Sep 26 22:21:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(450, 300)
        AboutDialog.setMinimumSize(QtCore.QSize(450, 300))
        AboutDialog.setMaximumSize(QtCore.QSize(450, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/remastersys.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 260, 431, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.thanksBtn = QtGui.QPushButton(AboutDialog)
        self.thanksBtn.setGeometry(QtCore.QRect(10, 260, 98, 27))
        self.thanksBtn.setCheckable(True)
        self.thanksBtn.setChecked(False)
        self.thanksBtn.setObjectName(_fromUtf8("thanksBtn"))
        self.logo = QtGui.QLabel(AboutDialog)
        self.logo.setGeometry(QtCore.QRect(190, 10, 61, 71))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/remastersys.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.title = QtGui.QLabel(AboutDialog)
        self.title.setGeometry(QtCore.QRect(80, 80, 291, 20))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.version = QtGui.QLabel(AboutDialog)
        self.version.setGeometry(QtCore.QRect(210, 110, 41, 21))
        self.version.setObjectName(_fromUtf8("version"))
        self.describe = QtGui.QLabel(AboutDialog)
        self.describe.setGeometry(QtCore.QRect(20, 140, 411, 20))
        self.describe.setObjectName(_fromUtf8("describe"))
        self.homepage = QtGui.QLabel(AboutDialog)
        self.homepage.setGeometry(QtCore.QRect(190, 160, 81, 21))
        self.homepage.setOpenExternalLinks(True)
        self.homepage.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.homepage.setObjectName(_fromUtf8("homepage"))
        self.copyright = QtGui.QLabel(AboutDialog)
        self.copyright.setGeometry(QtCore.QRect(120, 190, 221, 20))
        self.copyright.setObjectName(_fromUtf8("copyright"))
        self.license = QtGui.QLabel(AboutDialog)
        self.license.setGeometry(QtCore.QRect(10, 210, 431, 21))
        self.license.setOpenExternalLinks(True)
        self.license.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.license.setObjectName(_fromUtf8("license"))
        self.textEdit = QtGui.QTextEdit(AboutDialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 431, 141))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Remastersys", None, QtGui.QApplication.UnicodeUTF8))
        self.thanksBtn.setText(QtGui.QApplication.translate("AboutDialog", "Thanks", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p>Remastersys GUI Based on PyQt4</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.version.setText(QtGui.QApplication.translate("AboutDialog", "0.1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.describe.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p align=\"center\">Backup your Ubuntu system &amp; create a custom LiveCD</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.homepage.setText(QtGui.QApplication.translate("AboutDialog", "<a href=\"https://github.com/mutse/remastersys-qt\">Homepage</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.copyright.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p>Copyright &copy;2013 Mutse Young</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.license.setText(QtGui.QApplication.translate("AboutDialog", "For detail <a href=\"http://www.gnu.org/licenses/old-licenses/gpl-2.0.html\">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">Authors:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">    Mutse Young &lt;</span><a href=\"yyhoo2.young@gmail.com\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; text-decoration: underline; color:#0000ff;\">yyhoo2.young@gmail.com</span></a><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">Translators:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt;\">Artists:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import remastersys_rc

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from aboutdialog import AboutDialog
from ui.ui_remastersys import Ui_Remastersys
from configdialog import ConfigDialog
from plymouth import Plymouth
from usersetting import UserSetting
import remastersys_rc
import sys
import os

class Remastersys(QMainWindow, Ui_Remastersys):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

        self.setupUi(self)
        self.vecBtn = []
        self.initUi()

        desktop = QDesktopWidget()
        w = desktop.screenGeometry().width();
        h = desktop.screenGeometry().height();

        self.move((w - self.width()) / 2, (h - self.height()) / 2)

    def initUi(self):
        self.vecBtn.append(self.backupBtn)
        self.vecBtn.append(self.distBtn)
        self.vecBtn.append(self.customBtn)
        self.vecBtn.append(self.clearBtn)
        self.vecBtn.append(self.checklogBtn)

        for i in range(0, len(self.vecBtn)):
            self.vecBtn[i].setCheckable(True);
            self.vecBtn[i].setAutoExclusive(True);
            self.vecBtn[i].clicked.connect(self.setCurrentWidget)

        self.console1.hide()
        self.console2.hide()
        self.mainImg.show()

        self.aboutDlg = AboutDialog()
        self.quitBtn.clicked.connect(qApp.quit)
        self.aboutBtn.clicked.connect(self.aboutDlg.show)

        self.configDlg = ConfigDialog()
        self.configDlg.showMainWin.connect(self.show)

        self.plymouth = Plymouth()
        self.plymouth.showMainWin.connect(self.show)

        self.userSetting = UserSetting()
        self.userSetting.showMainWin.connect(self.show)

    def setCurrentWidget(self):
        for i in range(0, len(self.vecBtn)):
            if self.vecBtn[i].isChecked():
                self.stackedWidget.setCurrentIndex(i)

                if i == 0: # for Backup mode
                    if self.console1.isHidden():
                        self.mainImg.hide()
                        self.console1.StartProcess(QString("pwd")) #remastersys backup
                        self.console1.show()
                elif i == 1: # for Dist mode
                    if self.console2.isHidden():
                        self.console2.StartProcess(QString("ls")) #remastersys dist
                        self.console2.show();
                elif i == 2: # for Custom mode
                    self.splashImgBtn.clicked.connect(self.pickSplash)
                    self.grubImgBtn.clicked.connect(self.pickGrubImg)
                    self.plymouthBtn.clicked.connect(self.showPlymouth)
                    self.userSettingBtn.clicked.connect(self.showUserSetting)
                    self.configureBtn.clicked.connect(self.showConfigDialog)
                elif i == 3:
                    self.clearLog()
                    QMessageBox.information(self, self.tr("Success"), self.tr("Working Folder cleared"))
                elif i == 4:
                    self.checkLog()

    def pickSplash(self):
        fileName = QFileDialog.getOpenFileName(self,
                    self.tr("Choose a 640x480 png file for the live background"),
                    QDir.homePath(), self.tr("Image Files (*.png)"))

        if not fileName.isEmpty():
            QMessageBox.information(self, "Splash", fileName)
            cmd = "cp -f " + fileName + "/etc/remastersys/isolinux/splash.png"
            #os.system(cmd.toUtf8().data())

    def pickGrubImg(self):
        fileName = QFileDialog.getOpenFileName(self,
                    self.tr("Choose a png file for grub background"),
                    QDir.homePath(), self.tr("Image Files (*.png)"))

        if not fileName.isEmpty():
            QMessageBox.information(self, "Grub image", fileName)
            #os.system("sed -i -e '/^GRUB_BACKGROUND/d' /etc/default/grub")
            cmd = "echo 'GRUB_BACKGROUND=" + fileName + "' >> /etc/default/grub"
            #os.system(cmd.toUtf8().data())
            #os.system("update-grub")

    def showPlymouth(self):
        self.hide()
        self.plymouth.show()

    def showUserSetting(self):
        self.hide()
        self.userSetting.show()

    def showConfigDialog(self):
        self.hide()
        self.configDlg.show()

    def clearLog(self):
        os.system("remastersys clean")

    def checkLog(self):
        file = QFile("/home/remastersys/remastersys/remastersys.log")
        if not file.exists():
            self.textEdit.setText("Logfile remastersys.log not found")
            return

        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return

        input = QTextStream(file)
        lines = ""
        while not input.atEnd():
            lines += input.readLine() + "\n"

        file.close()
        self.textEdit.setText(lines)

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("./i18n/remastersys-qt_" + QLocale.system().name())
    app.installTranslator(translator)

    transQt = QTranslator()
    qtTrPath = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    qtTrFile = "qt_" + QLocale.system().name()
    transQt.load(qtTrFile, qtTrPath)
    app.installTranslator(transQt)
    app.setProperty("qtc_locale", QLocale.system().name())

    win = Remastersys()
    win.setWindowIcon(QIcon(QPixmap(":/images/remastersys.png")))
    win.show()

    sys.exit(app.exec_())


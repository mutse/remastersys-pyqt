#!/usr/bin/evn python
#

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.ui_configdialog import Ui_ConfigDialog
import sys

class ConfigDialog(QDialog, Ui_ConfigDialog):

    """
    signal showMainWin
    """
    showMainWin = pyqtSignal()

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)

        self.readConfig()

    def accept(self):
        self.writeConfig()
        self.close()
        self.showMainWin.emit()

    def readConfig(self):
        workDir = "/home/remastersys"
        liveUser = "custom"
        liveLabel = "Custom Live CD"
        customIso = "custom$1.iso"
        opts = "-no-recovery -always-use-fragments -b 1M -no-duplicates"
        backupShow = "1"
        url = "https://github.com/mutse/remastersys-pyqt"
        
        file = QFile("./remastersys.conf")
        if file.exists():
            if not file.open(QIODevice.ReadOnly | QIODevice.Text):
                return

            in1 = QTextStream(file)
            str = QString("")
            while not in1.atEnd():
                str = in1.readLine()
                str.remove("\"")
                if str.left(1) != "#" or str != "":
                    strList = str.split("=")
                    if len(strList) == 2:
                        item = strList[0]
                        item.trimmed()
                        if item == "WORKDIR":
                            workDir = strList[1]
                        elif item == "EXCLUDES":
                            exclude = strList[1]
                        elif item == "LIVEUSER":
                            liveUser = strList[1]
                        elif item == "LIVECDLABEL":
                            liveLabel = strList[1]
                        elif item == "CUSTOMISO":
                            customIso = strList[1]
                        elif item == "SQUASHFSOPTS":
                            opts = strList[1]
                        elif item == "BACKUPSHOWINSTALL":
                            backupShow = strList[1]
                        elif item == "LIVECDURL":
                            url = strList[1]

            file.close()

        self.lineEdit_1.setText(workDir)
        self.lineEdit_2.setText(exclude)
        self.lineEdit_3.setText(liveUser)
        self.lineEdit_4.setText(liveLabel)
        self.lineEdit_5.setText(customIso)
        self.lineEdit_6.setText(opts)
        self.lineEdit_7.setText(backupShow)
        self.lineEdit_8.setText(url)

    def writeConfig(self):
        file = QFile("./remastersys.conf")
        if file.open(QFile.WriteOnly | QFile.Truncate):
            out = QTextStream(file)
            out << "#Remastersys Global Configuration File\n"
            out << "\n"
            out << "# This is the temporary working directory and won't be included on the cd/dvd\n"
            out << "WORKDIR=" <<  self.lineEdit_1.text() << "\n"
            out << "\n"
            out << "# Here you can add any other files or directories to be excluded from the live filesystem\n"
            out << "# Separate each entry with a space\n"
            out << "EXCLUDES=" << self.lineEdit_2.text() << "\n"
            out << "\n"
            out << "# Here you can change the livecd/dvd username\n"
            out << "LIVEUSER=" << self.lineEdit_3.text() << "\n"
            out << "\n"
            out << "# Here you can change the name of the livecd/dvd label\n"
            out << "LIVECDLABEL=" << self.lineEdit_4.text() << "\n"
            out << "\n"
            out << "# Here you can change the name of the ISO file that is created\n"
            out << "CUSTOMISO=" << self.lineEdit_5.text() << "\n"
            out << "\n"
            out << "# Here you can change the mksquashfs options\n"
            out << "SQUASHFSOPTS=" << self.lineEdit_6.text() << "\n"
            out << "\n"
            out << "# Here you can prevent the Install icon from showing up on the desktop in backup mode. 0 - to not show 1 - to show\n"
            out << "BACKUPSHOWINSTALL=" << self.lineEdit_7.text() << "\n"
            out << "\n"
            out << "# Here you can change the url for the usb-creator info\n"
            out << "LIVECDURL=" << self.lineEdit_8.text() << "\n"

            file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = ConfigDialog()
    config.show()
    
    sys.exit(app.exec_())


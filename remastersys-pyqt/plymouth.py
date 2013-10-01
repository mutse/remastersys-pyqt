#!/usr/bin/env python
#

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.ui_plymouth import Ui_Plymouth
import os
import sys

class Plymouth(QDialog, Ui_Plymouth):

    """
    signal showMainWin
    """
    showMainWin = pyqtSignal()

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.process = QProcess()
        self.process.start("update-alternatives --list default.plymouth")
        self.process.readyReadStandardOutput.connect(self.readFromStdout)

        self.selectBtn.clicked.connect(self.slotSelect)
        self.previewBtn.clicked.connect(self.slotPreview)
        self.backBtn.clicked.connect(self.slotBack)

    def readFromStdout(self):
        output = QString(self.process.readAllStandardOutput())
        self.listWidget.addItem(output)

    def slotSelect(self):
        # added sync here
        if self.listWidget.currentItem() != None:
            str = self.listWidget.currentItem().text()
            cmd = "update-alternatives --set default.plymouth " + str
            #os.system(cmd.toUtf8().data())
            #os.system("update-initramfs -u")
        else:
            QMessageBox.information(self, self.tr("select error"), self.tr("please select item"))

    def slotPreview(self):
        os.system("plymouth-preview")

    def slotBack(self):
        self.close()
        self.showMainWin.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    plymouth = Plymouth()
    plymouth.show()

    sys.exit(app.exec_())


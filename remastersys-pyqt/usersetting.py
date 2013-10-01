#!/usr/bin/env python
#

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.ui_usersetting import Ui_UserSetting
import os
import sys

class UserSetting(QDialog, Ui_UserSetting):
    """
    signal showMainWin
    """
    showMainWin = pyqtSignal()

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.process = QProcess()
        self.process.start("python list_user.py")
        self.process.readyReadStandardOutput.connect(self.readFromStdout)

        self.selectBtn.clicked.connect(self.slotSelect)

    def readFromStdout(self):
        output = self.process.readAllStandardOutput()
        self.listWidget.addItem(QString(output))

    def slotSelect(self):
        # added sync here
        if self.listWidget.currentItem() != None:
            str = self.listWidget.currentItem().text()
            QMessageBox.information(self, "select", QString(str))
            cmd = "remastersys-skelcopy " + str;
            #os.system(cmd.toUtf8().data());

        self.close()
        self.showMainWin.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    userset = UserSetting()
    userset.show()

    sys.exit(app.exec_())


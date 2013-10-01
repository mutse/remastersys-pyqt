#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.ui_aboutdialog import Ui_AboutDialog
import sys

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        
        self.setupUi(self)

        self.setModal(True)

        self.textEdit.hide()
        self.thanksBtn.clicked.connect(self.showOrHideThanks)

    def showOrHideThanks(self):
        if self.thanksBtn.isChecked():
            self.version.hide()
            self.describe.hide()
            self.homepage.hide()
            self.copyright.hide()
            self.license.hide()
            self.textEdit.show()
        else:
            self.version.show()
            self.describe.show()
            self.homepage.show()
            self.copyright.show()
            self.license.show()
            self.textEdit.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    about = AboutDialog()
    about.show()

    sys.exit(app.exec_())


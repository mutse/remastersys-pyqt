#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
# This program is portted from https://code.google.com/p/qterminal/
#

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from redirect import Redirect
import sys

class QConsoleWidget(QTextEdit):
    def __init__(self, parent = None):
        QTextEdit.__init__(self, parent)

        self.setUndoRedoEnabled(False)
        self.setCursorWidth(5)
        self.setTextColor(QColor("white"))

        p = self.palette()
        p.setColor(QPalette.Base, QColor("#000000"))
        self.setPalette(p)

        self.fixedPosition = 0
        self.redirect = Redirect()

        self.redirect.OnChildStdOutWrite.connect(self.OnChildStdOutWrite)
        self.redirect.OnChildStarted.connect(self.OnChildStarted)
        self.redirect.OnChildStdErrWrite.connect(self.OnChildStdErrWrite)
        self.redirect.OnChildTerminate.connect(self.OnChildTerminate)

        #self.redirect.StartChildProcess(False)

    def StartProcess(self, strCmd):
        self.redirect.StartChildProcess(False, strCmd)

    def OnChildStarted(self):
        pass

    def OnChildStdOutWrite(self, szOutput):
        self.insertPlainText(szOutput)
        self.fixedPosition = self.textCursor().position()

    def OnChildStdErrWrite(self, szOutput):
        self.append(szOutput)
        self.fixedPosition = self.textCursor().position()

    def OnChildTerminate(self):
        self.redirect.TerminateChildProcess()

    def keyPressEvent(self, event):
        accept = False
        key = event.key()
        if key == Qt.Key_Backspace or event.key() == Qt.Key_Left:
            accept = self.textCursor().position() > self.fixedPosition
        elif key == Qt.Key_Return:
            accept = False
            count = self.toPlainText().count() - self.fixedPosition
            cmd = self.toPlainText().right(count)
            self.redirect.WriteChildStdIn(cmd + "\n")
        elif key == Qt.Key_Up:
            accept = False
        else:
            accept = self.textCursor().position() >= self.fixedPosition

        if accept:
            QTextEdit.keyPressEvent(self, event)

    def cursorPositionChanged(self):
        if self.textCursor().position() < self.fixedPosition:
            self.textCursor().setPosition(self.fixedPosition)

    def closeEvent(self, event):
        self.redirect.TerminateChildProcess()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    console = QConsoleWidget()
    console.setWindowTitle("PyQt4 Terminal")
    console.resize(600, 400)
    console.StartProcess(QString("pwd"))
    console.show()

    sys.exit(app.exec_())


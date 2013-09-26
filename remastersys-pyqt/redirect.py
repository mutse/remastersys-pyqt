#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
# This program is portted from https://code.google.com/p/qterminal/
#

from PyQt4.QtCore import *

class Redirect(QObject):

    """
    customized signals definitions
    """
    OnChildStarted = pyqtSignal()
    OnChildStdOutWrite = pyqtSignal(str)
    OnChildStdErrWrite = pyqtSignal(str)
    OnChildTerminate = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        self.process = None

    def StartChildProcess(self, bShowChildWindow, strCmd):
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)

        self.process.readyReadStandardError.connect(self.readyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.readyReadStandardOutput)
        
        self.process.start("sh")
        cmd = strCmd + "\n"
        self.process.write(cmd.toUtf8().data())

        return True

    def IsChildRunning(self):
        return True

    def TerminateChildProcess(self):
        self.process.terminate()
        self.process.waitForFinished()

    def ProcessThread(self):
        return 0

    def WriteChildStdIn(self, szInput):
        self.process.write(szInput.toLatin1())
        self.process.write("pwd\n")

    def readyReadStandardOutput(self):
        str = self.process.readAllStandardOutput()
        self.OnChildStdOutWrite.emit(QString(str))

    def readyReadStandardError(self):
        self.OnChildStdErrWrite.emit(self.process.readAllStandardError)
 

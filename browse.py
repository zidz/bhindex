#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore, QtDeclarative
from PySide.QtCore import Qt

import os, os.path as path, sys, time, signal
from ConfigParser import ConfigParser
from optparse import OptionParser
from threading import Thread
from time import sleep

HERE = path.dirname(__file__)
sys.path.append(HERE)

import db, config, magnet
config = config.read()

from ui.filter import FilterList
from ui.results import ResultsView

import bithorde

if __name__=='__main__':
    parser = OptionParser(usage="usage: %prog [options] <PATH>")

    (options, args) = parser.parse_args()
    if len(args)>1:
        parser.error("Only one path-argument supported")
    elif args:
        path=db.path_str2lst(args[0])
    else:
        path=[]

    thisdb = db.open(config)

    QtGui.QApplication.setGraphicsSystem('raster')
    app = QtGui.QApplication(sys.argv)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    mainwindow = QtGui.QMainWindow()
    mainwindow.resize(600,400)
    mainwindow.setWindowTitle("BitHorde Index")
    mainwindow.show()

    def onFilterChanged():
        f = filter.criteria()
        results.refresh(f)

    filter = FilterList(mainwindow, thisdb)
    filter.onChanged.connect(onFilterChanged)
    mainwindow.addToolBar(filter)

    results = ResultsView(mainwindow, thisdb)

    results.refresh(None)
    results.show()

    mainwindow.setCentralWidget(results)

    #vlayout.addWidget(preview)
    sys.exit(app.exec_())


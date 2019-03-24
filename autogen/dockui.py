# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dock.ui',
# licensing of 'ui/dock.ui' applies.
#
# Created: Sun Mar 24 11:47:44 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(687, 455)
        self.contents = QtWidgets.QWidget()
        self.contents.setObjectName("contents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.contents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.contents)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.LoaderPage = QtWidgets.QWidget()
        self.LoaderPage.setObjectName("LoaderPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LoaderPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loader = QtWidgets.QLabel(self.LoaderPage)
        self.loader.setCursor(QtCore.Qt.PointingHandCursor)
        self.loader.setAcceptDrops(True)
        self.loader.setStyleSheet("")
        self.loader.setObjectName("loader")
        self.gridLayout_2.addWidget(self.loader, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.LoaderPage)
        self.CovTablePage = QtWidgets.QWidget()
        self.CovTablePage.setObjectName("CovTablePage")
        self.gridLayout = QtWidgets.QGridLayout(self.CovTablePage)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close = QtWidgets.QToolButton(self.CovTablePage)
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.reload = QtWidgets.QToolButton(self.CovTablePage)
        self.reload.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/reload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon1)
        self.reload.setObjectName("reload")
        self.horizontalLayout.addWidget(self.reload)
        self.selectColor = QtWidgets.QToolButton(self.CovTablePage)
        self.selectColor.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon/brush.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectColor.setIcon(icon2)
        self.selectColor.setObjectName("selectColor")
        self.horizontalLayout.addWidget(self.selectColor)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(540, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.colorize = QtWidgets.QCheckBox(self.CovTablePage)
        self.colorize.setChecked(True)
        self.colorize.setObjectName("colorize")
        self.gridLayout.addWidget(self.colorize, 0, 2, 1, 1)
        self.covTable = QtWidgets.QTableWidget(self.CovTablePage)
        self.covTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.covTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.covTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.covTable.setAlternatingRowColors(True)
        self.covTable.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.covTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.covTable.setShowGrid(False)
        self.covTable.setObjectName("covTable")
        self.covTable.setColumnCount(5)
        self.covTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.covTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.covTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.covTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.covTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.covTable.setHorizontalHeaderItem(4, item)
        self.covTable.horizontalHeader().setDefaultSectionSize(118)
        self.covTable.horizontalHeader().setStretchLastSection(True)
        self.covTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.covTable, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.CovTablePage)
        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)
        DockWidget.setWidget(self.contents)

        self.retranslateUi(DockWidget)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtWidgets.QApplication.translate("DockWidget", "Cutter DynamoRIO Coverage", None, -1))
        self.loader.setText(QtWidgets.QApplication.translate("DockWidget", "<html><head/><body><p align=\"center\"><img src=\":/icons/icon/data-transfer-download.svg\"/></p><p align=\"center\">Click to <span style=\" font-weight:600;\">Open drcov file</span> or drag it here.</p></body></html>", None, -1))
        self.colorize.setText(QtWidgets.QApplication.translate("DockWidget", "Colorize (On / OFF)", None, -1))
        self.covTable.setSortingEnabled(True)
        self.covTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("DockWidget", "Coverage", None, -1))
        self.covTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("DockWidget", "Function Name", None, -1))
        self.covTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("DockWidget", "Address", None, -1))
        self.covTable.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("DockWidget", "Instructions Hits", None, -1))
        self.covTable.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("DockWidget", "Basic Block Hits", None, -1))

from . import icon_rc

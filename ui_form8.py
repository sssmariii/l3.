# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form8.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelStep = QLabel(self.centralwidget)
        self.labelStep.setObjectName(u"labelStep")
        self.labelStep.setGeometry(QRect(350, 60, 58, 16))
        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(450, 30, 250, 16))
        self.canvasLabel = QLabel(self.centralwidget)
        self.canvasLabel.setObjectName(u"canvasLabel")
        self.canvasLabel.setGeometry(QRect(20, 100, 700, 500))
        self.sliderStep = QSlider(self.centralwidget)
        self.sliderStep.setObjectName(u"sliderStep")
        self.sliderStep.setGeometry(QRect(20, 20, 160, 25))
        self.sliderStep.setMaximum(5)
        self.sliderStep.setOrientation(Qt.Orientation.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelStep.setText("")
        self.labelName.setText("")
        self.canvasLabel.setText("")
    # retranslateUi


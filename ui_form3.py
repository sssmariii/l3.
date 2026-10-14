# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form3.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(40, 20, 400, 400))
        self.btnRed = QPushButton(self.centralwidget)
        self.btnRed.setObjectName(u"btnRed")
        self.btnRed.setGeometry(QRect(150, 480, 100, 32))
        self.btnGreen = QPushButton(self.centralwidget)
        self.btnGreen.setObjectName(u"btnGreen")
        self.btnGreen.setGeometry(QRect(30, 480, 100, 32))
        self.btnBlue = QPushButton(self.centralwidget)
        self.btnBlue.setObjectName(u"btnBlue")
        self.btnBlue.setGeometry(QRect(270, 440, 100, 32))
        self.btnRotateLeft = QPushButton(self.centralwidget)
        self.btnRotateLeft.setObjectName(u"btnRotateLeft")
        self.btnRotateLeft.setGeometry(QRect(30, 440, 100, 32))
        self.btnRotateRight = QPushButton(self.centralwidget)
        self.btnRotateRight.setObjectName(u"btnRotateRight")
        self.btnRotateRight.setGeometry(QRect(150, 440, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imageLabel.setText("")
        self.btnRed.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e R", None))
        self.btnGreen.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e G", None))
        self.btnBlue.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e B", None))
        self.btnRotateLeft.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0435\u0432\u043e", None))
        self.btnRotateRight.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0440\u0430\u0432\u043e", None))
    # retranslateUi


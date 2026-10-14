# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form7.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnA = QPushButton(self.centralwidget)
        self.btnA.setObjectName(u"btnA")
        self.btnA.setGeometry(QRect(20, 10, 100, 32))
        self.btnB = QPushButton(self.centralwidget)
        self.btnB.setObjectName(u"btnB")
        self.btnB.setGeometry(QRect(20, 60, 100, 32))
        self.btnD = QPushButton(self.centralwidget)
        self.btnD.setObjectName(u"btnD")
        self.btnD.setGeometry(QRect(20, 140, 100, 32))
        self.btnE = QPushButton(self.centralwidget)
        self.btnE.setObjectName(u"btnE")
        self.btnE.setGeometry(QRect(20, 190, 100, 32))
        self.btnF = QPushButton(self.centralwidget)
        self.btnF.setObjectName(u"btnF")
        self.btnF.setGeometry(QRect(20, 230, 100, 32))
        self.btnG = QPushButton(self.centralwidget)
        self.btnG.setObjectName(u"btnG")
        self.btnG.setGeometry(QRect(20, 280, 100, 32))
        self.btnC = QPushButton(self.centralwidget)
        self.btnC.setObjectName(u"btnC")
        self.btnC.setGeometry(QRect(20, 100, 100, 32))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 36))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.btnA.setText(QCoreApplication.translate("mainWindow", u"\u0414\u043e", None))
        self.btnB.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0435", None))
        self.btnD.setText(QCoreApplication.translate("mainWindow", u"\u0424\u0430", None))
        self.btnE.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u043b\u044c", None))
        self.btnF.setText(QCoreApplication.translate("mainWindow", u"\u041b\u044f", None))
        self.btnG.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0438", None))
        self.btnC.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0438", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form6.ui'
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
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.smileLabel = QLabel(self.centralwidget)
        self.smileLabel.setObjectName(u"smileLabel")
        self.smileLabel.setGeometry(QRect(40, 20, 500, 400))
        self.sliderScale = QSlider(self.centralwidget)
        self.sliderScale.setObjectName(u"sliderScale")
        self.sliderScale.setGeometry(QRect(180, 460, 160, 25))
        self.sliderScale.setMinimum(10)
        self.sliderScale.setMaximum(200)
        self.sliderScale.setValue(100)
        self.sliderScale.setOrientation(Qt.Orientation.Horizontal)
        self.btnColor = QPushButton(self.centralwidget)
        self.btnColor.setObjectName(u"btnColor")
        self.btnColor.setGeometry(QRect(30, 450, 100, 32))
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
        self.smileLabel.setText("")
        self.btnColor.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0446\u0432\u0435\u0442", None))
    # retranslateUi


import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QColorDialog
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen, QBrush
from ui_form6 import Ui_MainWindow


class SmileApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.smile_color = QColor(255, 220, 0)

        
        self.ui.sliderScale.setMinimum(10)
        self.ui.sliderScale.setMaximum(200)
        self.ui.sliderScale.setValue(100)
        self.ui.sliderScale.valueChanged.connect(self.draw_smile)

        
        self.ui.btnColor.clicked.connect(self.choose_color)

        
        QtCore.QTimer.singleShot(100, self.choose_color)

    
    def choose_color(self):
        color = QColorDialog.getColor(self.smile_color, self, "Цвет смайлика")
        if color.isValid():
            self.smile_color = color
            self.draw_smile()

    
    def draw_smile(self):
        
        w = self.ui.smileLabel.width()
        h = self.ui.smileLabel.height()

        
        pixmap = QPixmap(w, h)
        pixmap.fill(QtCore.Qt.white)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)  

        
        scale = self.ui.sliderScale.value() / 100.0

        
        base_r = min(w, h) * 0.35
        r = base_r * scale

        cx = w / 2
        cy = h / 2

        
        pen = QPen(QtCore.Qt.black, 3)
        painter.setPen(pen)
        painter.setBrush(QBrush(self.smile_color))
        painter.drawEllipse(QtCore.QPointF(cx, cy), r, r)

        
        eye_r = r * 0.12
        eye_offset_x = r * 0.35
        eye_offset_y = r * 0.30

        painter.setBrush(QBrush(QtCore.Qt.black))
        painter.setPen(QtCore.Qt.NoPen)

        painter.drawEllipse(
            QtCore.QPointF(cx - eye_offset_x, cy - eye_offset_y),
            eye_r, eye_r
        )
        painter.drawEllipse(
            QtCore.QPointF(cx + eye_offset_x, cy - eye_offset_y),
            eye_r, eye_r
        )

        
        smile_rect = QtCore.QRectF(
            cx - r * 0.55,  
            cy - r * 0.10,   
            r * 1.10,       
            r * 0.90       
        )

        pen = QPen(QtCore.Qt.black, max(2, int(r * 0.05)))
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)

        
        painter.drawArc(smile_rect, 200 * 16, 140 * 16)

        painter.end()

        self.ui.smileLabel.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmileApp()
    window.show()
    sys.exit(app.exec())
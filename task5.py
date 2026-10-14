import sys
import random
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QInputDialog, QMessageBox
from PySide6.QtGui import QPixmap, QPainter, QColor
from ui_form5 import Ui_MainWindow


class FlagGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        try:
            self.ui.btnAgain.clicked.connect(self.generate_flag)
        except AttributeError:
            pass  

        
        QtCore.QTimer.singleShot(100, self.ask_count_and_generate)

    
    def ask_count_and_generate(self):
        count, ok = QInputDialog.getInt(
            self,
            "Количество цветов",
            "Сколько полос на флаге?",
            5,      
            2,      
            20      
        )
        if not ok:
            return

        self.draw_flag(count)

    
    def draw_flag(self, count):
        w = self.ui.flagLabel.width()
        h = self.ui.flagLabel.height()

       
        pixmap = QPixmap(w, h)
        pixmap.fill(QtCore.Qt.white)

        painter = QPainter(pixmap)

        
        stripe_h = h / count

        for i in range(count):
            
            color = QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            painter.setBrush(color)
            painter.setPen(QtCore.Qt.NoPen)

            
            y = int(i * stripe_h)
            painter.drawRect(0, y, w, int(stripe_h) + 1)  

        painter.end()

        self.ui.flagLabel.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FlagGenerator()
    window.show()
    sys.exit(app.exec())
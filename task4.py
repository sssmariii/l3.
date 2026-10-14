import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from ui_form4 import Ui_MainWindow


class AlphaEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.original_pixmap = None  

        
        self.ui.sliderAlpha.setMinimum(0)
        self.ui.sliderAlpha.setMaximum(100)
        self.ui.sliderAlpha.setValue(100)
        self.ui.sliderAlpha.valueChanged.connect(self.update_alpha)

        
        QtCore.QTimer.singleShot(100, self.load_image_at_start)

    
    def load_image_at_start(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите изображение", "",
            "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )
        if not path:
            QMessageBox.warning(self, "Внимание", "Изображение не выбрано")
            return

        img = QImage(path)
        if img.isNull():
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить картинку")
            return

        self.original_pixmap = QPixmap.fromImage(img)
        self.update_alpha()

    
    def update_alpha(self):
        if self.original_pixmap is None:
            return

        value = self.ui.sliderAlpha.value()  
        alpha = value / 100.0                

        self.ui.labelValue.setText(str(value))

        
        pix = self.original_pixmap.copy()

       
        pix = pix.scaled(
            self.ui.imageLabel.width(),
            self.ui.imageLabel.height(),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )

       
        transparent = QPixmap(pix.size())
        transparent.fill(QtCore.Qt.transparent)

        painter = QtGui.QPainter(transparent)
        painter.setOpacity(alpha)
        painter.drawPixmap(0, 0, pix)
        painter.end()

        self.ui.imageLabel.setPixmap(transparent)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AlphaEditor()
    window.show()
    sys.exit(app.exec())
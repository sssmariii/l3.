import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QPixmap, QImage, QTransform
from ui_form3 import Ui_MainWindow


class ImageEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.original_image = None

        self.ui.btnRed.clicked.connect(lambda: self.keep_channel("R"))
        self.ui.btnGreen.clicked.connect(lambda: self.keep_channel("G"))
        self.ui.btnBlue.clicked.connect(lambda: self.keep_channel("B"))
        self.ui.btnRotateLeft.clicked.connect(lambda: self.rotate(-90))
        self.ui.btnRotateRight.clicked.connect(lambda: self.rotate(90))

        
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

        
        self.original_image = img.convertToFormat(QImage.Format_RGB32)
        self.show_image(self.original_image)

    def show_image(self, qimage):
        pix = QPixmap.fromImage(qimage)
        
        pix = pix.scaled(
            self.ui.imageLabel.width(),
            self.ui.imageLabel.height(),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.ui.imageLabel.setPixmap(pix)

    
    def keep_channel(self, channel):
        if self.original_image is None:
            return

        img = self.original_image.copy()
        w, h = img.width(), img.height()

        for y in range(h):
            for x in range(w):
                pixel = img.pixel(x, y)  # QRgb
                r = (pixel >> 16) & 0xFF
                g = (pixel >> 8) & 0xFF
                b = pixel & 0xFF

                if channel == "R":
                    new_pixel = QtGui.qRgb(r, 0, 0)
                elif channel == "G":
                    new_pixel = QtGui.qRgb(0, g, 0)
                else:  # B
                    new_pixel = QtGui.qRgb(0, 0, b)

                img.setPixel(x, y, new_pixel)

        self.show_image(img)


    def rotate(self, angle):
        if self.original_image is None:
            return

        transform = QTransform().rotate(angle)
        rotated = self.original_image.transformed(transform)

        
        self.original_image = rotated
        self.show_image(rotated)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec())
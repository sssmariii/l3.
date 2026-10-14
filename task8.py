import sys
import os
import math
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QPainter, QPen
from ui_form8 import Ui_MainWindow


class LSystemApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

       
        self.name = ""
        self.angle = 90          
        self.axiom = ""          
        self.rules = {}       
        self.max_step = 5        

        
        self.ui.sliderStep.setMinimum(0)
        self.ui.sliderStep.setMaximum(self.max_step)
        self.ui.sliderStep.setValue(0)
        self.ui.sliderStep.valueChanged.connect(self.on_step_changed)

        
        QtCore.QTimer.singleShot(100, self.load_system_at_start)

    
    def load_system_at_start(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл L-системы", "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not path:
            QMessageBox.warning(self, "Внимание", "Файл не выбран")
            return

        try:
            self.parse_file(path)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка чтения", str(e))
            return

        self.ui.labelName.setText(self.name)
        self.ui.sliderStep.setMaximum(self.max_step)
        self.ui.sliderStep.setValue(0)
        self.draw_step(0)

    def parse_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip() != ""]

        if len(lines) < 4:
            raise ValueError("Файл слишком короткий (нужно минимум 4 строки)")

        self.name = lines[0]

        try:
            n = int(lines[1])
        except ValueError:
            raise ValueError("Вторая строка должна быть целым числом")
        if n == 0:
            raise ValueError("Число углов не может быть 0")

        self.angle = 360.0 / n
        self.axiom = lines[2]

        
        self.rules = {}
        for line in lines[3:]:
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue  
            sym, replacement = parts
            self.rules[sym] = replacement

   
    def build_string(self, steps):
        """Возвращает строку после N применений правил."""
        current = self.axiom
        for _ in range(steps):
            new = []
            for ch in current:
                new.append(self.rules.get(ch, ch))
            current = "".join(new)
        return current

   
    def draw_step(self, step):
        self.ui.labelStep.setText(f"Шаг: {step}")

        s = self.build_string(step)

        w = self.ui.canvasLabel.width()
        h = self.ui.canvasLabel.height()

        pixmap = QPixmap(w, h)
        pixmap.fill(QtCore.Qt.white)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QtCore.Qt.black, 1.5)
        painter.setPen(pen)

        
        x = w / 2
        y = h * 0.9
        direction = -90.0   


        
        
        step_len = min(w, h) / (3 * (1.7 ** step)) / 4
        if step_len < 1:
            step_len = 1

        for ch in s:
            if ch == "F" or ch == "f":
                
                rad = math.radians(direction)
                nx = x + step_len * math.cos(rad)
                ny = y + step_len * math.sin(rad)
                if ch == "F":
                    painter.drawLine(QtCore.QPointF(x, y), QtCore.QPointF(nx, ny))
                x, y = nx, ny
            elif ch == "+":
                direction += self.angle
            elif ch == "-":
                direction -= self.angle
            

        painter.end()
        self.ui.canvasLabel.setPixmap(pixmap)

    def on_step_changed(self, value):
        self.draw_step(value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LSystemApp()
    window.show()
    sys.exit(app.exec())
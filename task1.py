import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox
from ui_form import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnLoad.clicked.connect(self.load_file)
        self.ui.btnSave.clicked.connect(self.save_file)

        self.ui.lineMax.setReadOnly(True)
        self.ui.lineMin.setReadOnly(True)
        self.ui.lineAvg.setReadOnly(True)

        self.stats = None

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите текстовый файл", "", "Текстовые файлы (*.txt)"
        )
        if not path:
            return

        try:
            numbers = self.read_numbers(path)
            if not numbers:
                raise ValueError("Файл не содержит чисел")

            mx = max(numbers)
            mn = min(numbers)
            avg = sum(numbers) / len(numbers)

            self.stats = (mx, mn, avg)

            self.ui.lineMax.setText(str(mx))
            self.ui.lineMin.setText(str(mn))
            self.ui.lineAvg.setText(f"{avg:.4f}")

        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", f"Неверный формат данных:\n{e}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def read_numbers(self, path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        tokens = content.split()
        numbers = []
        for tok in tokens:
            try:
                numbers.append(int(tok))
            except ValueError:
                raise ValueError(f"'{tok}' не является целым числом")
        return numbers

    def save_file(self):
        if self.stats is None:
            QMessageBox.warning(self, "Внимание",
                                "Сначала загрузите файл с числами")
            return

        path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить результат", "", "Текстовые файлы (*.txt)"
        )
        if not path:
            return

        mx, mn, avg = self.stats
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"Максимум: {mx}\n")
                f.write(f"Минимум: {mn}\n")
                f.write(f"Среднее: {avg:.4f}\n")
            QMessageBox.information(self, "Готово", "Файл сохранён")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка записи", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
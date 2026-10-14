import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox
from ui_form2 import Ui_MainWindow


class TextEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnOpen.clicked.connect(self.open_file)
        self.ui.btnNew.clicked.connect(self.new_file)
        self.ui.btnSave.clicked.connect(self.save_file)

        self.current_path = None  

    
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.ui.textBrowser.setPlainText(content)
            self.current_path = path
            self.setWindowTitle(f"Редактор — {path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка открытия", str(e))

    
    def new_file(self):
        self.ui.textBrowser.clear()
        self.current_path = None
        self.setWindowTitle("Редактор — новый файл")

    
    def save_file(self):
        
        if self.current_path:
            path = self.current_path
        else:
            path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
            )
            if not path:
                return

        try:
            text = self.ui.textBrowser.toPlainText()
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            self.current_path = path
            self.setWindowTitle(f"Редактор — {path}")
            QMessageBox.information(self, "Готово", "Файл сохранён")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка сохранения", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
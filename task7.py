import sys
import os
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect
from ui_form7 import Ui_mainWindow


class Piano(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        base = os.path.dirname(os.path.abspath(__file__))
        sounds_dir = os.path.join(base, "sounds")

        self.notes = {
            "C": self.ui.btnC,
            "D": self.ui.btnD,
            "E": self.ui.btnE,
            "F": self.ui.btnF,
            "G": self.ui.btnG,
            "A": self.ui.btnA,
            "B": self.ui.btnB,
        }

        self.players = {}

        for note, button in self.notes.items():
            path = os.path.join(sounds_dir, f"{note}.mp3")

            effect = QSoundEffect()
            effect.setSource(QUrl.fromLocalFile(path))
            effect.setVolume(1.0)

            self.players[note] = effect
            button.clicked.connect(lambda checked=False, n=note: self.play(n))

    def play(self, note):
        effect = self.players.get(note)
        if effect is None:
            return

        if effect.source().isEmpty():
            print(f"Файл для ноты {note} не найден")
            return

        effect.play()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Piano()
    window.show()
    sys.exit(app.exec())
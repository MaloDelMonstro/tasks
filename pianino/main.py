import sys
import os
import threading
import shutil
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt, QTimer


def play_sound(filepath):
    if sys.platform == "win32":
        import winsound
        try:
            winsound.PlaySound(filepath, winsound.SND_ASYNC | winsound.SND_FILENAME)
        except Exception:
            pass
    else:
        for player in ["afplay", "paplay", "aplay", "ffplay", "mpg123"]:
            if shutil.which(player):
                subprocess.Popen([player, filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return


class PianoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фортепиано")
        self.setFixedSize(540, 320)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.buttons = {}
        self._setup_ui()
        self._setup_keymap()

    def _setup_ui(self):
        white_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        for i, note in enumerate(white_notes):
            btn = QPushButton(note)
            btn.setGeometry(i * 70 + 20, 40, 70, 220)
            btn.setStyleSheet("""
                QPushButton { background-color: white; border: 2px solid #333; border-radius: 5px;
                              font-size: 18px; font-weight: bold; color: #333; }
                QPushButton:pressed { background-color: #ddd; }
            """)
            btn.clicked.connect(lambda checked, n=note: self._handle_input(n))
            btn.setParent(self)
            self.buttons[note] = btn

        black_notes = [('C#', 45), ('D#', 115), ('F#', 255), ('G#', 325), ('A#', 395)]
        for note, x in black_notes:
            btn = QPushButton(note.replace('#', ''))
            btn.setGeometry(x, 40, 50, 140)
            btn.setStyleSheet("""
                QPushButton { background-color: #111; color: white; border: 2px solid #000;
                              border-radius: 4px; font-size: 14px; }
                QPushButton:pressed { background-color: #444; }
            """)
            btn.clicked.connect(lambda checked, n=note: self._handle_input(n))
            btn.raise_()
            btn.setParent(self)
            self.buttons[note] = btn

        hint = QLabel("Клавиши: A S D F G H J (белые) | W E T Y U (чёрные)", self)
        hint.setGeometry(20, 270, 500, 30)
        hint.setStyleSheet("color: #666; font-size: 12px;")

    def _setup_keymap(self):
        self.key_map = {
            Qt.Key.Key_A: 'C',  Qt.Key.Key_W: 'C#',
            Qt.Key.Key_S: 'D',  Qt.Key.Key_E: 'D#',
            Qt.Key.Key_D: 'E',
            Qt.Key.Key_F: 'F',  Qt.Key.Key_T: 'F#',
            Qt.Key.Key_G: 'G',  Qt.Key.Key_Y: 'G#',
            Qt.Key.Key_H: 'A',  Qt.Key.Key_U: 'A#',
            Qt.Key.Key_J: 'B'
        }

    def _handle_input(self, note):
        btn = self.buttons.get(note)
        if btn:
            btn.setDown(True)
            QTimer.singleShot(150, lambda b=btn: b.setDown(False))

        filename = f"sounds/{note.replace('#', 's')}.wav"
        if os.path.exists(filename):
            threading.Thread(target=play_sound, args=(filename,), daemon=True).start()
        else:
            print(f"Файл {filename} не найден.")

    def keyPressEvent(self, event):
        if event.key() in self.key_map:
            self._handle_input(self.key_map[event.key()])
        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    piano = PianoApp()
    piano.show()
    sys.exit(app.exec())
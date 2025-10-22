from PyQt5.QtWidgets import QApplication
from interface import NpiUI
from logic import NpiLogic
import sys

class NpiApp:
    def __init__(self):
        # Initialise l'interface et logic
        self.app = QApplication(sys.argv)
        self.ui = NpiUI()
        self.logic= NpiLogic()

        # Conexion des boutons chiffres
        self.ui.button_1.clicked.connect(lambda: self.logic.handle_input('1', self.ui))
        self.ui.button_2.clicked.connect(lambda: self.logic.handle_input('2', self.ui))
        self.ui.button_3.clicked.connect(lambda: self.logic.handle_input('3', self.ui))
        self.ui.button_4.clicked.connect(lambda: self.logic.handle_input('4', self.ui))
        self.ui.button_5.clicked.connect(lambda: self.logic.handle_input('5', self.ui))
        self.ui.button_6.clicked.connect(lambda: self.logic.handle_input('6', self.ui))
        self.ui.button_7.clicked.connect(lambda: self.logic.handle_input('7', self.ui))
        self.ui.button_8.clicked.connect(lambda: self.logic.handle_input('8', self.ui))
        self.ui.button_9.clicked.connect(lambda: self.logic.handle_input('9', self.ui))
        self.ui.button_0.clicked.connect(lambda: self.logic.handle_input('0', self.ui))
        # Connexions des boutons operateurs
        self.ui.button_add.clicked.connect(lambda: self.logic.handle_input('+', self.ui))
        self.ui.button_sub.clicked.connect(lambda: self.logic.handle_input('-', self.ui))
        self.ui.button_mul.clicked.connect(lambda: self.logic.handle_input('x', self.ui))
        self.ui.button_div.clicked.connect(lambda: self.logic.handle_input(':', self.ui))

    def run(self):
        self.ui.show()       # Affiche la fenêtre
        sys.exit(self.app.exec())  # Lance la boucle d’événements


if __name__ == "__main__":
    app = NpiApp()
    app.run()
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt


class NpiUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisation des buttons
        self.button_0 = QPushButton("0")
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")
        self.button_4 = QPushButton("4")
        self.button_5 = QPushButton("5")
        self.button_6 = QPushButton("6")
        self.button_7 = QPushButton("7")
        self.button_8 = QPushButton("8")
        self.button_9 = QPushButton("9")
        self.button_add = QPushButton("+")
        self.button_sub = QPushButton("-")
        self.button_mul = QPushButton("*")
        self.button_div = QPushButton("/")

        # Initialisation des labels
        self.stack_lab = QLabel()
        self.lastValue_lab = QLabel()

        # Fixe les tailles des Widgets
        self.setFixedSize(400, 500) # taille de la fenêtre
        self.stack_lab.setFixedSize(70,250) # taille des labels
        self.lastValue_lab.setFixedSize(250,150)
        for btn in [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, 
                    self.button_7, self.button_8, self.button_9, self.button_add, self.button_sub, self.button_mul, self.button_div]:
            btn.setFixedSize(60,60)

        # Layout (Grid)
        layout = QGridLayout()
        layout.addWidget(self.stack_lab, 0, 0, 5, 1, alignment=Qt.AlignLeft | Qt.AlignCenter) #TODO: Regler probleme alignement et faire un style.css simple 
        layout.addWidget(self.lastValue_lab, 0, 1, 1, 4, alignment=Qt.AlignBottom | Qt.AlignCenter)

        layout.addWidget(self.button_0, 5, 2, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_1, 2, 1, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_2, 2, 2, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_3, 2, 3, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_4, 3, 1, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_5, 3, 2, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_6, 3, 3, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_7, 4, 1, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_8, 4, 2, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_9, 4, 3, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_add, 2, 4, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_sub, 3, 4, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_mul, 4, 4, alignment=Qt.AlignBottom | Qt.AlignCenter)
        layout.addWidget(self.button_div, 5, 4, alignment=Qt.AlignBottom | Qt.AlignCenter)

        # Parametre des Widgets
        self.stack_lab.setProperty("class", "label")
        self.lastValue_lab.setProperty("class", "label")

        self.button_0.setProperty("class", "button")
        self.button_1.setProperty("class", "button")
        self.button_2.setProperty("class", "button")
        self.button_3.setProperty("class", "button")
        self.button_4.setProperty("class", "button")
        self.button_5.setProperty("class", "button")
        self.button_6.setProperty("class", "button")
        self.button_7.setProperty("class", "button")
        self.button_8.setProperty("class", "button")
        self.button_9.setProperty("class", "button")
        self.button_add.setProperty("class", "button")
        self.button_sub.setProperty("class", "button")
        self.button_mul.setProperty("class", "button")
        self.button_div.setProperty("class", "button")

        # Stretch pour redimensionnement
        for col in range(5):
            layout.setColumnStretch(col,1)
        for row in range(6):
            layout.setRowStretch(row,1)
        self.setLayout(layout)

        # Charge de fichier CSS
        try:
            with open("style.css", "r") as f:
                self.setStyleSheet(f.read())
        except:
            self.lastValue_lab.setText("Impossible de vharger le fichier CSS")

if "__main__" == __name__:
    print("good")
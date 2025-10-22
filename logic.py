from operators import operateurs
from stack import Stack
from is_correct import is_correct

class NpiLogic():
    def __init__(self):
        self.stack = Stack()

    # Une fonction pour tous les bontoon pour eviter repetison
    def handle_input(self, value, ui):
        if is_correct(value):
            if value not in operateurs:
                self.stack.push(int(value))
            else:
                if self.stack.size() >= 2:
                    a, b = self.stack.pop(), self.stack.pop()
                    if a == 0 and value == ':':
                        ui.lastValue_lab.setText("Error: Division by zero")
                        self.stack.push(b)
                        self.stack.push(a)
                    else:
                        res = int(operateurs[value](b, a))
                        ui.lastValue_lab.setText(f"{b} {value} {a} = {res}")
                        self.stack.push(res)
                else:
                    ui.lastValue_lab.setText("Erreur : pas assez de valeurs dans la pile")
        else:
            ui.lastValue_lab.setText("NotValideValueError")
        ui.stack_lab.setText(str(self.stack))
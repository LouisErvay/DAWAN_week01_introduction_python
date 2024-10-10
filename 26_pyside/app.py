# Dans PySide, il y a 2 classes à importer : QApplication, QWidget

# QApplication est pour créer l'app (on l'utilise une seule fois)
# QWidget est la classe mère de tous les widgets

from PySide6.QtWidgets import QApplication, QWidget

from main_ui import Ui_Form
class Main_Window(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        # Application du design généré via le designer
        self.setupUi(self)

        self.btnAddition.clicked.connect(self.somme)

    def somme(self):
        nb1 = float(self.lineInput1.text())
        nb2 = float(self.lineInput2.text())
        s = nb1+nb2
        self.labelResult.setText(str(s))

# Créer l'application
app = QApplication()

f = Main_Window()
f.show()

app.exec()
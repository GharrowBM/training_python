from PySide2 import QtWidgets
import  currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setup_ui()
        # self.setup_css()
        self.set_default_values()
        self.setup_connections()

    def setup_ui(self):
        self.setWindowTitle("Convertisseur de devises")
        self.layout = QtWidgets.QHBoxLayout(self)
        self.comboBox_devisesFrom = QtWidgets.QComboBox()
        self.spinBox_montant = QtWidgets.QSpinBox()
        self.comboBox_devisesTo = QtWidgets.QComboBox()
        self.spinBox_montantConverti = QtWidgets.QSpinBox()
        self.button_inverser = QtWidgets.QPushButton("Inverser devises")

        self.layout.addWidget(self.comboBox_devisesFrom)
        self.layout.addWidget(self.spinBox_montant)
        self.layout.addWidget(self.comboBox_devisesTo)
        self.layout.addWidget(self.spinBox_montantConverti)
        self.layout.addWidget(self.button_inverser)

    def set_default_values(self):
        self.comboBox_devisesFrom.addItems(sorted(self.c.currencies))
        self.comboBox_devisesFrom.setCurrentText("EUR")
        self.comboBox_devisesTo.addItems(sorted(self.c.currencies))
        self.comboBox_devisesTo.setCurrentText("EUR")

        self.spinBox_montant.setRange(1, 1000000000)
        self.spinBox_montant.setValue(100)
        self.spinBox_montantConverti.setRange(1, 1000000000)
        self.spinBox_montantConverti.setValue(100)

    def setup_connections(self):
        self.comboBox_devisesFrom.activated.connect(self.compute)
        self.comboBox_devisesTo.activated.connect(self.compute)
        self.spinBox_montant.valueChanged.connect(self.compute)
        self.button_inverser.clicked.connect(self.inverser_devises)

    # def setup_css(self):
    #     self.setStyleSheet("""
    #     background-color: #3D0839;
    #     color: #F0F0F0;
    #     border: none;
    #     """)

    def compute(self):
        montant = self.spinBox_montant.value()
        devise_from = self.comboBox_devisesFrom.currentText()
        devise_to = self.comboBox_devisesTo.currentText()

        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
        except currency_converter.RateNotFoundError:
            print("La conversion n'a pas fonctionné !")
        else:
            self.spinBox_montantConverti.setValue(int(resultat))


    def inverser_devises(self):
        devise_from = self.comboBox_devisesFrom.currentText()
        devise_to = self.comboBox_devisesTo.currentText()

        self.comboBox_devisesTo.setCurrentText(devise_from)
        self.comboBox_devisesFrom.setCurrentText(devise_to)

        self.compute()

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
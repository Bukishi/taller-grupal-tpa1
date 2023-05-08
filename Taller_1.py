import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,  QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel,QWidget,QGridLayout,QHBoxLayout,QLineEdit

class OtraVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        caja = QGridLayout()
        self.setWindowTitle("Editar Atributos")
        campo1=QLabel("Unidad")
        self.campo2=QLineEdit()
        self.campo2.setEchoMode(QLineEdit.EchoMode.Unidad)
        boton = QPushButton("Lanzar Dialog")
        caja.addWidget(campo1,0,0)
        caja.addWidget(campo2,0,1)

        self.setLayout(caja)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barriles/Onzas")
        self.setFixedSize(QSize(400,400))
        self.ventana_secundaria = OtraVentana()
        box = QVBoxLayout()
        bien=QLabel("Bienvenido al comparador")
        b_info=QLabel("como se usa")
        box.addWidget(bien)
        box.addWidget(b_info)
        self.setLayout(box)
        comp=QHBoxLayout()

        e="<"
        desig=QLabel(e)
        comp.addWidget(desig)
        objeto1=QVBoxLayout()

        dinfo1=QLabel()
        boton=QPushButton("Añadir Datos")


"""  def Reaccionar(self):
        if self.ventana_secundaria.isVisible():
            self.ventana_secundaria.hide() # hace que la ventana sea invisible: visible = False
        else:
            self.ventana_secundaria.show()
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() 

    app.exec()
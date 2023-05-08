from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(489, 369)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 303, 351, 41))
        self.pushButton.setCheckable(False)
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(50, 70, 141, 221))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 260, 111, 24))
        self.listView_2 = QListView(Dialog)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(300, 70, 141, 221))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 260, 111, 24))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 451, 21))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(72, 90, 101, 21))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(320, 90, 113, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Comparar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Agregar Datos", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Agregar Datos", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"Barril Vs. Onza", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"Barril", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Dialog", u"Onza", None))
    # retranslateUi

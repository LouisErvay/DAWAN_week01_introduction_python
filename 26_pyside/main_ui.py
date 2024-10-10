# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(904, 693)
        self.lineInput1 = QLineEdit(Form)
        self.lineInput1.setObjectName(u"lineInput1")
        self.lineInput1.setGeometry(QRect(350, 110, 113, 22))
        self.lineInput2 = QLineEdit(Form)
        self.lineInput2.setObjectName(u"lineInput2")
        self.lineInput2.setGeometry(QRect(350, 150, 113, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 110, 49, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 150, 49, 16))
        self.btnAddition = QPushButton(Form)
        self.btnAddition.setObjectName(u"btnAddition")
        self.btnAddition.setGeometry(QRect(360, 200, 75, 24))
        self.labelResult = QLabel(Form)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setGeometry(QRect(370, 270, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre2", None))
        self.btnAddition.setText(QCoreApplication.translate("Form", u"Additioner", None))
        self.labelResult.setText("")
    # retranslateUi


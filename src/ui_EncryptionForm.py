# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_EncryptionForm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
class Ui_EncryptionForm(object):
    def setupUi(self, EncryptionForm):
        if not EncryptionForm.objectName():
            EncryptionForm.setObjectName(u"EncryptionForm")
        EncryptionForm.resize(400, 300)
        self.verticalLayout = QVBoxLayout(EncryptionForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(EncryptionForm)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.encryptionCombo = QComboBox(self.widget)
        self.encryptionCombo.addItem("")
        self.encryptionCombo.addItem("")
        self.encryptionCombo.addItem("")
        self.encryptionCombo.addItem("")
        self.encryptionCombo.addItem("")
        self.encryptionCombo.setObjectName(u"encryptionCombo")

        self.verticalLayout_2.addWidget(self.encryptionCombo)

        self.saveBtn = QPushButton(self.widget)
        self.saveBtn.setObjectName(u"saveBtn")
        font1 = QFont()
        font1.setBold(True)
        self.saveBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.saveBtn)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(EncryptionForm)

        QMetaObject.connectSlotsByName(EncryptionForm)
    # setupUi

    def retranslateUi(self, EncryptionForm):
        EncryptionForm.setWindowTitle(QCoreApplication.translate("EncryptionForm", u"CustomComponent", None))
        self.label.setText(QCoreApplication.translate("EncryptionForm", u"Select Encryption Method", None))
        self.encryptionCombo.setItemText(0, QCoreApplication.translate("EncryptionForm", u"None", None))
        self.encryptionCombo.setItemText(1, QCoreApplication.translate("EncryptionForm", u"AES-256 Active", None))
        self.encryptionCombo.setItemText(2, QCoreApplication.translate("EncryptionForm", u"ChaCha20 Active", None))
        self.encryptionCombo.setItemText(3, QCoreApplication.translate("EncryptionForm", u"XOR Active", None))
        self.encryptionCombo.setItemText(4, QCoreApplication.translate("EncryptionForm", u"PBK Active", None))

        self.saveBtn.setText(QCoreApplication.translate("EncryptionForm", u"Save", None))
    # retranslateUi


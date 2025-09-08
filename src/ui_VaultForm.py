# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_VaultForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_VaultFormComponent(object):
    def setupUi(self, VaultFormComponent):
        if not VaultFormComponent.objectName():
            VaultFormComponent.setObjectName(u"VaultFormComponent")
        VaultFormComponent.resize(534, 684)
        self.verticalLayout = QVBoxLayout(VaultFormComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_8 = QWidget(VaultFormComponent)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(500, 0))
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.titleLabel = QLabel(self.widget_8)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.titleLabel)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_7.addWidget(self.customHorizontalSeparator)

        self.widget = QWidget(self.widget_8)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.itemTypeComboBox = QComboBox(self.widget)
        self.itemTypeComboBox.addItem("")
        self.itemTypeComboBox.addItem("")
        self.itemTypeComboBox.addItem("")
        self.itemTypeComboBox.addItem("")
        self.itemTypeComboBox.setObjectName(u"itemTypeComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.itemTypeComboBox)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.itemNameLineEdit = QLineEdit(self.widget)
        self.itemNameLineEdit.setObjectName(u"itemNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.itemNameLineEdit)

        self.notesPlainTextEdit = QPlainTextEdit(self.widget)
        self.notesPlainTextEdit.setObjectName(u"notesPlainTextEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.notesPlainTextEdit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout_7.addWidget(self.widget)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_7.addWidget(self.customHorizontalSeparator_2)

        self.widget_2 = QWidget(self.widget_8)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vaultStackedWidget = QCustomQStackedWidget(self.widget_2)
        self.vaultStackedWidget.setObjectName(u"vaultStackedWidget")
        self.vaultStackedWidget.setProperty("fadeTransition", True)
        self.vaultStackedWidget.setProperty("fadeTime", 1000)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.formLayout_2 = QFormLayout(self.widget_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.siteNameLineEdit = QLineEdit(self.widget_3)
        self.siteNameLineEdit.setObjectName(u"siteNameLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.siteNameLineEdit)

        self.usernameLineEdit = QLineEdit(self.widget_3)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLineEdit = QLineEdit(self.widget_3)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.passwordLineEdit)

        self.showPasswordBtn = QPushButton(self.widget_3)
        self.showPasswordBtn.setObjectName(u"showPasswordBtn")
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showPasswordBtn.setIcon(icon)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.showPasswordBtn)

        self.generatePasswordBtn = QPushButton(self.widget_3)
        self.generatePasswordBtn.setObjectName(u"generatePasswordBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/generating_tokens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generatePasswordBtn.setIcon(icon1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.generatePasswordBtn)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.vaultStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_9)

        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName(u"widget_4")
        self.formLayout_3 = QFormLayout(self.widget_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.noteTitleLineEdit = QLineEdit(self.widget_4)
        self.noteTitleLineEdit.setObjectName(u"noteTitleLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.noteTitleLineEdit)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.noteBodyPlainTextEdit = QPlainTextEdit(self.widget_4)
        self.noteBodyPlainTextEdit.setObjectName(u"noteBodyPlainTextEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.noteBodyPlainTextEdit)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.vaultStackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_12)

        self.widget_5 = QWidget(self.page_3)
        self.widget_5.setObjectName(u"widget_5")
        self.formLayout_4 = QFormLayout(self.widget_5)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_13 = QLabel(self.widget_5)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.cardHolderLineEdit = QLineEdit(self.widget_5)
        self.cardHolderLineEdit.setObjectName(u"cardHolderLineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.cardHolderLineEdit)

        self.cardNumberLineEdit = QLineEdit(self.widget_5)
        self.cardNumberLineEdit.setObjectName(u"cardNumberLineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.cardNumberLineEdit)

        self.expiryDateEdit = QDateEdit(self.widget_5)
        self.expiryDateEdit.setObjectName(u"expiryDateEdit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.expiryDateEdit)

        self.cvvLineEdit = QLineEdit(self.widget_5)
        self.cvvLineEdit.setObjectName(u"cvvLineEdit")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.cvvLineEdit)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.billingAddressLineEdit = QLineEdit(self.widget_5)
        self.billingAddressLineEdit.setObjectName(u"billingAddressLineEdit")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.billingAddressLineEdit)

        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_17)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.vaultStackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_18)

        self.widget_6 = QWidget(self.page_4)
        self.widget_6.setObjectName(u"widget_6")
        self.formLayout_5 = QFormLayout(self.widget_6)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_19 = QLabel(self.widget_6)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.contactNameLineEdit = QLineEdit(self.widget_6)
        self.contactNameLineEdit.setObjectName(u"contactNameLineEdit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.contactNameLineEdit)

        self.label_20 = QLabel(self.widget_6)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.contactEmailLineEdit = QLineEdit(self.widget_6)
        self.contactEmailLineEdit.setObjectName(u"contactEmailLineEdit")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.contactEmailLineEdit)

        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.contactPhoneLineEdit = QLineEdit(self.widget_6)
        self.contactPhoneLineEdit.setObjectName(u"contactPhoneLineEdit")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.contactPhoneLineEdit)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.vaultStackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.vaultStackedWidget)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout_7.addWidget(self.customHorizontalSeparator_3)

        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(self.widget_7)
        self.cancelButton.setObjectName(u"cancelButton")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(self.widget_7)
        self.saveButton.setObjectName(u"saveButton")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.saveButton)


        self.verticalLayout_7.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(VaultFormComponent)

        self.vaultStackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(VaultFormComponent)
    # setupUi

    def retranslateUi(self, VaultFormComponent):
        VaultFormComponent.setWindowTitle(QCoreApplication.translate("VaultFormComponent", u"Frame", None))
        self.titleLabel.setText(QCoreApplication.translate("VaultFormComponent", u"Add  New Vault Item", None))
        self.label_2.setText(QCoreApplication.translate("VaultFormComponent", u"Item Type", None))
        self.itemTypeComboBox.setItemText(0, QCoreApplication.translate("VaultFormComponent", u"Passwords", None))
        self.itemTypeComboBox.setItemText(1, QCoreApplication.translate("VaultFormComponent", u"Notes", None))
        self.itemTypeComboBox.setItemText(2, QCoreApplication.translate("VaultFormComponent", u"Payment Cards", None))
        self.itemTypeComboBox.setItemText(3, QCoreApplication.translate("VaultFormComponent", u"Contacts", None))

        self.itemTypeComboBox.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Item Type", None))
        self.label_3.setText(QCoreApplication.translate("VaultFormComponent", u"Item Name", None))
        self.itemNameLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Item Name", None))
        self.notesPlainTextEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Notes", None))
        self.label_4.setText(QCoreApplication.translate("VaultFormComponent", u"Notes", None))
        self.label_5.setText(QCoreApplication.translate("VaultFormComponent", u"Passwords", None))
        self.label_6.setText(QCoreApplication.translate("VaultFormComponent", u"Site Name", None))
        self.label_7.setText(QCoreApplication.translate("VaultFormComponent", u"Username / Email", None))
        self.label_8.setText(QCoreApplication.translate("VaultFormComponent", u"Password", None))
        self.siteNameLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Site Name", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Username / Email", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Password", None))
        self.showPasswordBtn.setText(QCoreApplication.translate("VaultFormComponent", u"Show Password", None))
        self.generatePasswordBtn.setText(QCoreApplication.translate("VaultFormComponent", u"Use Password Generator", None))
        self.label_9.setText(QCoreApplication.translate("VaultFormComponent", u"Notes ", None))
        self.label_10.setText(QCoreApplication.translate("VaultFormComponent", u"Title", None))
        self.noteTitleLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Title", None))
        self.label_11.setText(QCoreApplication.translate("VaultFormComponent", u"Note", None))
        self.noteBodyPlainTextEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Note", None))
        self.label_12.setText(QCoreApplication.translate("VaultFormComponent", u"Payment Cards", None))
        self.label_13.setText(QCoreApplication.translate("VaultFormComponent", u"Cardholder Name", None))
        self.label_14.setText(QCoreApplication.translate("VaultFormComponent", u"Card Number", None))
        self.label_15.setText(QCoreApplication.translate("VaultFormComponent", u"Expiry Date", None))
        self.cardHolderLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Cardholder Name", None))
        self.cardNumberLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Card Number", None))
        self.cvvLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"CVV", None))
        self.label_16.setText(QCoreApplication.translate("VaultFormComponent", u"CVV", None))
        self.billingAddressLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Billing Address", None))
        self.label_17.setText(QCoreApplication.translate("VaultFormComponent", u"Billing Address", None))
        self.label_18.setText(QCoreApplication.translate("VaultFormComponent", u"Contacts ", None))
        self.label_19.setText(QCoreApplication.translate("VaultFormComponent", u"Full Name", None))
        self.contactNameLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Full Name", None))
        self.label_20.setText(QCoreApplication.translate("VaultFormComponent", u"Email", None))
        self.contactEmailLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Email", None))
        self.label_21.setText(QCoreApplication.translate("VaultFormComponent", u"Phone", None))
        self.contactPhoneLineEdit.setPlaceholderText(QCoreApplication.translate("VaultFormComponent", u"Phone", None))
        self.cancelButton.setText(QCoreApplication.translate("VaultFormComponent", u"Cancel", None))
        self.saveButton.setText(QCoreApplication.translate("VaultFormComponent", u"Save", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_VaultItemDetails.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_VaultItemDetailsForm(object):
    def setupUi(self, VaultItemDetailsForm):
        if not VaultItemDetailsForm.objectName():
            VaultItemDetailsForm.setObjectName(u"VaultItemDetailsForm")
        VaultItemDetailsForm.resize(400, 429)
        self.verticalLayout = QVBoxLayout(VaultItemDetailsForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.details = QWidget(VaultItemDetailsForm)
        self.details.setObjectName(u"details")
        self.details.setMinimumSize(QSize(300, 0))
        self.details.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.details)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.details)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.closeBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.frame)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.details)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_2)

        self.frame_3 = QFrame(self.details)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 7)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.itemNameLabel = QLabel(self.frame_3)
        self.itemNameLabel.setObjectName(u"itemNameLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.itemNameLabel)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.itemTypeLabel = QLabel(self.frame_3)
        self.itemTypeLabel.setObjectName(u"itemTypeLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.itemTypeLabel)

        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.itemNotesTextEdit = QPlainTextEdit(self.frame_3)
        self.itemNotesTextEdit.setObjectName(u"itemNotesTextEdit")
        self.itemNotesTextEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.itemNotesTextEdit)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.itemDetailsPages = QCustomQStackedWidget(self.details)
        self.itemDetailsPages.setObjectName(u"itemDetailsPages")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemDetailsPages.sizePolicy().hasHeightForWidth())
        self.itemDetailsPages.setSizePolicy(sizePolicy)
        self.passwordPage = QWidget()
        self.passwordPage.setObjectName(u"passwordPage")
        self.gridLayout_3 = QGridLayout(self.passwordPage)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.showPasswordBtn = QPushButton(self.passwordPage)
        self.showPasswordBtn.setObjectName(u"showPasswordBtn")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/eye-slash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showPasswordBtn.setIcon(icon1)

        self.gridLayout_3.addWidget(self.showPasswordBtn, 2, 3, 1, 1)

        self.label_12 = QLabel(self.passwordPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.siteValueLabel = QLabel(self.passwordPage)
        self.siteValueLabel.setObjectName(u"siteValueLabel")

        self.gridLayout_3.addWidget(self.siteValueLabel, 0, 1, 1, 1)

        self.copyPasswordBtn = QPushButton(self.passwordPage)
        self.copyPasswordBtn.setObjectName(u"copyPasswordBtn")
        self.copyPasswordBtn.setMinimumSize(QSize(53, 0))
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/content_copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copyPasswordBtn.setIcon(icon2)

        self.gridLayout_3.addWidget(self.copyPasswordBtn, 2, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.customHorizontalSeparator_4 = QCustomHorizontalSeparator(self.passwordPage)
        self.customHorizontalSeparator_4.setObjectName(u"customHorizontalSeparator_4")

        self.gridLayout_3.addWidget(self.customHorizontalSeparator_4, 3, 0, 1, 4)

        self.passwordValueLabel = QLabel(self.passwordPage)
        self.passwordValueLabel.setObjectName(u"passwordValueLabel")

        self.gridLayout_3.addWidget(self.passwordValueLabel, 2, 1, 1, 1)

        self.showUsernameBtn = QPushButton(self.passwordPage)
        self.showUsernameBtn.setObjectName(u"showUsernameBtn")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showUsernameBtn.setIcon(icon3)

        self.gridLayout_3.addWidget(self.showUsernameBtn, 1, 3, 1, 1)

        self.usernameValueLabel = QLabel(self.passwordPage)
        self.usernameValueLabel.setObjectName(u"usernameValueLabel")

        self.gridLayout_3.addWidget(self.usernameValueLabel, 1, 1, 1, 1)

        self.label_10 = QLabel(self.passwordPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.copyUsernameBtn = QPushButton(self.passwordPage)
        self.copyUsernameBtn.setObjectName(u"copyUsernameBtn")
        self.copyUsernameBtn.setMinimumSize(QSize(53, 0))
        self.copyUsernameBtn.setIcon(icon2)

        self.gridLayout_3.addWidget(self.copyUsernameBtn, 1, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.passwordPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.copySiteBtn = QPushButton(self.passwordPage)
        self.copySiteBtn.setObjectName(u"copySiteBtn")
        self.copySiteBtn.setIcon(icon2)

        self.gridLayout_3.addWidget(self.copySiteBtn, 0, 2, 1, 1)

        self.openSiteBtn = QPushButton(self.passwordPage)
        self.openSiteBtn.setObjectName(u"openSiteBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/open_in_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openSiteBtn.setIcon(icon4)

        self.gridLayout_3.addWidget(self.openSiteBtn, 0, 3, 1, 1)

        self.itemDetailsPages.addWidget(self.passwordPage)
        self.notePage = QWidget()
        self.notePage.setObjectName(u"notePage")
        self.formLayout_2 = QFormLayout(self.notePage)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.notePage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        self.label_2.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.noteTitleLabel = QLabel(self.notePage)
        self.noteTitleLabel.setObjectName(u"noteTitleLabel")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.noteTitleLabel)

        self.label_14 = QLabel(self.notePage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.noteContentTextEdit = QPlainTextEdit(self.notePage)
        self.noteContentTextEdit.setObjectName(u"noteContentTextEdit")
        self.noteContentTextEdit.setAutoFillBackground(False)
        self.noteContentTextEdit.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.noteContentTextEdit)

        self.itemDetailsPages.addWidget(self.notePage)
        self.paymentCardPage = QWidget()
        self.paymentCardPage.setObjectName(u"paymentCardPage")
        self.gridLayout = QGridLayout(self.paymentCardPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.paymentCardPage)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_4.addWidget(self.label_31, 3, 0, 1, 1)

        self.copyCardNumberBtn = QPushButton(self.widget_2)
        self.copyCardNumberBtn.setObjectName(u"copyCardNumberBtn")
        self.copyCardNumberBtn.setIcon(icon2)

        self.gridLayout_4.addWidget(self.copyCardNumberBtn, 0, 2, 1, 1)

        self.cardExpiryValueLabel = QLabel(self.widget_2)
        self.cardExpiryValueLabel.setObjectName(u"cardExpiryValueLabel")

        self.gridLayout_4.addWidget(self.cardExpiryValueLabel, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.cardHolderValueLabel = QLabel(self.widget_2)
        self.cardHolderValueLabel.setObjectName(u"cardHolderValueLabel")

        self.gridLayout_4.addWidget(self.cardHolderValueLabel, 2, 1, 1, 1)

        self.copyHolderBtn = QPushButton(self.widget_2)
        self.copyHolderBtn.setObjectName(u"copyHolderBtn")
        self.copyHolderBtn.setIcon(icon2)

        self.gridLayout_4.addWidget(self.copyHolderBtn, 2, 2, 1, 1)

        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.cardCvvValueLabel = QLabel(self.widget_2)
        self.cardCvvValueLabel.setObjectName(u"cardCvvValueLabel")

        self.gridLayout_4.addWidget(self.cardCvvValueLabel, 3, 1, 1, 1)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.cardNumberValueLabel = QLabel(self.widget_2)
        self.cardNumberValueLabel.setObjectName(u"cardNumberValueLabel")

        self.gridLayout_4.addWidget(self.cardNumberValueLabel, 0, 1, 1, 1)

        self.copyExpiryBtn = QPushButton(self.widget_2)
        self.copyExpiryBtn.setObjectName(u"copyExpiryBtn")
        self.copyExpiryBtn.setIcon(icon2)

        self.gridLayout_4.addWidget(self.copyExpiryBtn, 1, 2, 1, 1)

        self.showCvvBtn = QPushButton(self.widget_2)
        self.showCvvBtn.setObjectName(u"showCvvBtn")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/remove_red_eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showCvvBtn.setIcon(icon5)

        self.gridLayout_4.addWidget(self.showCvvBtn, 3, 4, 1, 1)

        self.copyCvvBtn = QPushButton(self.widget_2)
        self.copyCvvBtn.setObjectName(u"copyCvvBtn")
        self.copyCvvBtn.setIcon(icon2)

        self.gridLayout_4.addWidget(self.copyCvvBtn, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 4, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.itemDetailsPages.addWidget(self.paymentCardPage)
        self.contactPage = QWidget()
        self.contactPage.setObjectName(u"contactPage")
        self.gridLayout_5 = QGridLayout(self.contactPage)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.contactPage)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.contactNameValueLabel = QLabel(self.widget)
        self.contactNameValueLabel.setObjectName(u"contactNameValueLabel")

        self.gridLayout_2.addWidget(self.contactNameValueLabel, 0, 1, 1, 1)

        self.copyNameBtn = QPushButton(self.widget)
        self.copyNameBtn.setObjectName(u"copyNameBtn")
        self.copyNameBtn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.copyNameBtn, 0, 2, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 1, 0, 1, 1)

        self.contactEmailValueLabel = QLabel(self.widget)
        self.contactEmailValueLabel.setObjectName(u"contactEmailValueLabel")

        self.gridLayout_2.addWidget(self.contactEmailValueLabel, 1, 1, 1, 1)

        self.copyEmailBtn = QPushButton(self.widget)
        self.copyEmailBtn.setObjectName(u"copyEmailBtn")
        self.copyEmailBtn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.copyEmailBtn, 1, 2, 1, 1)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 2, 0, 1, 1)

        self.contactPhoneValueLabel = QLabel(self.widget)
        self.contactPhoneValueLabel.setObjectName(u"contactPhoneValueLabel")

        self.gridLayout_2.addWidget(self.contactPhoneValueLabel, 2, 1, 1, 1)

        self.copyPhoneBtn = QPushButton(self.widget)
        self.copyPhoneBtn.setObjectName(u"copyPhoneBtn")
        self.copyPhoneBtn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.copyPhoneBtn, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.itemDetailsPages.addWidget(self.contactPage)

        self.verticalLayout_4.addWidget(self.itemDetailsPages, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.securityStatus = QFrame(self.details)
        self.securityStatus.setObjectName(u"securityStatus")
        self.securityStatus.setFrameShape(QFrame.Shape.StyledPanel)
        self.securityStatus.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.securityStatus)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.securityStatus)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_18 = QLabel(self.securityStatus)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_18)


        self.verticalLayout_4.addWidget(self.securityStatus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.details, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(VaultItemDetailsForm)

        self.itemDetailsPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VaultItemDetailsForm)
    # setupUi

    def retranslateUi(self, VaultItemDetailsForm):
        VaultItemDetailsForm.setWindowTitle(QCoreApplication.translate("VaultItemDetailsForm", u"Frame", None))
        self.label_9.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Item Details", None))
        self.closeBtn.setText("")
        self.label.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Name", None))
        self.itemNameLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Type", None))
        self.itemTypeLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Note", None))
        self.showPasswordBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Password ", None))
        self.siteValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Paypal.com", None))
        self.copyPasswordBtn.setText("")
        self.passwordValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"************", None))
        self.showUsernameBtn.setText("")
        self.usernameValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"user@paypal.com", None))
        self.label_10.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Site name", None))
        self.copyUsernameBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Username/email", None))
        self.copySiteBtn.setText("")
        self.openSiteBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Note Title", None))
        self.noteTitleLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Note Content", None))
        self.label_31.setText(QCoreApplication.translate("VaultItemDetailsForm", u"CVV", None))
        self.copyCardNumberBtn.setText("")
        self.cardExpiryValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Number", None))
        self.cardHolderValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.copyHolderBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Expiry", None))
        self.cardCvvValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Holder", None))
        self.cardNumberValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.copyExpiryBtn.setText("")
        self.showCvvBtn.setText("")
        self.copyCvvBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Name", None))
        self.contactNameValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.copyNameBtn.setText("")
        self.label_26.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Email", None))
        self.contactEmailValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.copyEmailBtn.setText("")
        self.label_33.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Phone", None))
        self.contactPhoneValueLabel.setText(QCoreApplication.translate("VaultItemDetailsForm", u"TextLabel", None))
        self.copyPhoneBtn.setText("")
        self.label_17.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Security Status: ", None))
        self.label_18.setText(QCoreApplication.translate("VaultItemDetailsForm", u"Good", None))
    # retranslateUi


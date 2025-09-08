# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_WelcomeComponent(object):
    def setupUi(self, WelcomeComponent):
        if not WelcomeComponent.objectName():
            WelcomeComponent.setObjectName(u"WelcomeComponent")
        WelcomeComponent.resize(666, 566)
        self.verticalLayout_3 = QVBoxLayout(WelcomeComponent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(WelcomeComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(141, 93))
        self.label_2.setMaximumSize(QSize(141, 93))
        self.label_2.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_2)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_2)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/cloud.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/contact_mail.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/edit_note.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/mark_email_unread.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_solid/icons/font_awesome/solid/credit-card.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.widget)

        self.fingerprint = QWidget(self.widget_2)
        self.fingerprint.setObjectName(u"fingerprint")
        self.fingerprint.setMinimumSize(QSize(150, 150))
        self.fingerprint.setMaximumSize(QSize(150, 150))
        self.fingerprint.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.fingerprint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.fingerprint)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 80))
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u":/material_design/icons/material_design/fingerprint.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.fingerprint)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(WelcomeComponent)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator)

        self.widget_3 = QWidget(WelcomeComponent)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.lock = QWidget(self.widget_3)
        self.lock.setObjectName(u"lock")
        self.lock.setMinimumSize(QSize(150, 150))
        self.lock.setMaximumSize(QSize(150, 150))
        self.verticalLayout_6 = QVBoxLayout(self.lock)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.lock)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 80))
        self.label_8.setMaximumSize(QSize(80, 80))
        self.label_8.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/lock-open.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.lock, 0, Qt.AlignmentFlag.AlignRight)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignRight)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.registerBtn = QPushButton(self.widget_5)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.registerBtn)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.loginBtn = QPushButton(self.widget_5)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.loginBtn)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(WelcomeComponent)

        QMetaObject.connectSlotsByName(WelcomeComponent)
    # setupUi

    def retranslateUi(self, WelcomeComponent):
        WelcomeComponent.setWindowTitle(QCoreApplication.translate("WelcomeComponent", u"CustomComponent", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("WelcomeComponent", u"Your Secure Vault for Everything Personal", None))
        self.label_5.setText(QCoreApplication.translate("WelcomeComponent", u"Why TrustedIn?", None))
        self.label_4.setText(QCoreApplication.translate("WelcomeComponent", u"In a world filled with digital threats, TrustedIn gives you peace of mind. It\u2019s your offline, encrypted vault built for storing more than just passwords \u2014 from banking details and payment cards to personal notes and contacts.", None))
        self.pushButton.setText(QCoreApplication.translate("WelcomeComponent", u"Cloud", None))
        self.pushButton_4.setText(QCoreApplication.translate("WelcomeComponent", u"Contacts", None))
        self.pushButton_5.setText(QCoreApplication.translate("WelcomeComponent", u"Notes", None))
        self.pushButton_3.setText(QCoreApplication.translate("WelcomeComponent", u"Email", None))
        self.pushButton_2.setText(QCoreApplication.translate("WelcomeComponent", u"Card", None))
        self.label.setText("")
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("WelcomeComponent", u"Get Started:", None))
        self.registerBtn.setText(QCoreApplication.translate("WelcomeComponent", u"Create an Account", None))
        self.label_7.setText(QCoreApplication.translate("WelcomeComponent", u"--Or--", None))
        self.loginBtn.setText(QCoreApplication.translate("WelcomeComponent", u"Login", None))
    # retranslateUi


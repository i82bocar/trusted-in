# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_LoginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_LoginFormComponent(object):
    def setupUi(self, LoginFormComponent):
        if not LoginFormComponent.objectName():
            LoginFormComponent.setObjectName(u"LoginFormComponent")
        LoginFormComponent.resize(416, 0)
        self.verticalLayout = QVBoxLayout(LoginFormComponent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.accountPages = QCustomQStackedWidget(LoginFormComponent)
        self.accountPages.setObjectName(u"accountPages")
        self.accountPages.setMinimumSize(QSize(400, 500))
        self.accountPages.setProperty("fadeTransition", False)
        self.accountPages.setProperty("slideTransition", True)
        self.accountPages.setProperty("transitionTime", 1000)
        self.accountPages.setProperty("fadeTime", 1000)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_7 = QVBoxLayout(self.loginPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.loginPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.header = QFrame(self.widget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.header)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(141, 93))
        self.logo.setMaximumSize(QSize(141, 93))
        self.logo.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_2.addWidget(self.customHorizontalSeparator)

        self.body = QFrame(self.widget)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.loginEmail = QLineEdit(self.frame)
        self.loginEmail.setObjectName(u"loginEmail")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.loginEmail)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.loginPassword = QLineEdit(self.frame)
        self.loginPassword.setObjectName(u"loginPassword")
        self.loginPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.loginPassword)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.loginBtn = QPushButton(self.frame_2)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(100, 0))
        self.loginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.loginBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.frame_2)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_5.addWidget(self.customHorizontalSeparator_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.forgotpassBtn = QPushButton(self.frame_3)
        self.forgotpassBtn.setObjectName(u"forgotpassBtn")
        self.forgotpassBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.forgotpassBtn)

        self.toRegisterBtn = QPushButton(self.frame_3)
        self.toRegisterBtn.setObjectName(u"toRegisterBtn")
        self.toRegisterBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.toRegisterBtn)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.body)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout_2.addWidget(self.customHorizontalSeparator_3)

        self.footer = QFrame(self.widget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.footer)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/fingerprint.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_brands/icons/font_awesome/brands/windows.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.footer, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.widget)

        self.accountPages.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerPage.sizePolicy().hasHeightForWidth())
        self.registerPage.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.registerPage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.registerPage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.header_2 = QFrame(self.widget_2)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.header_2)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.logo_2 = QLabel(self.header_2)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(141, 93))
        self.logo_2.setMaximumSize(QSize(141, 93))
        self.logo_2.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.logo_2.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.logo_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.header_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)


        self.verticalLayout_8.addWidget(self.header_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.customHorizontalSeparator_4 = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator_4.setObjectName(u"customHorizontalSeparator_4")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_4)

        self.body_2 = QFrame(self.widget_2)
        self.body_2.setObjectName(u"body_2")
        self.body_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.body_2)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.body_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frame_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.emailInput = QLineEdit(self.frame_5)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.emailInput)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.passwordInput = QLineEdit(self.frame_5)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.passwordInput)

        self.confirmPasswordInput = QLineEdit(self.frame_5)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.confirmPasswordInput)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.label_15)

        self.agreeCheckbox = QCustomCheckBox(self.frame_5)
        self.agreeCheckbox.setObjectName(u"agreeCheckbox")
        self.agreeCheckbox.setMinimumSize(QSize(100, 0))
        self.agreeCheckbox.setMaximumSize(QSize(16777215, 20))

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.agreeCheckbox)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.lastNameInput = QLineEdit(self.frame_5)
        self.lastNameInput.setObjectName(u"lastNameInput")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lastNameInput)

        self.firstNameInput = QLineEdit(self.frame_5)
        self.firstNameInput.setObjectName(u"firstNameInput")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.firstNameInput)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.body_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.registerBtn = QPushButton(self.frame_6)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setMinimumSize(QSize(100, 0))
        self.registerBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.registerBtn.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.registerBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.customHorizontalSeparator_5 = QCustomHorizontalSeparator(self.frame_6)
        self.customHorizontalSeparator_5.setObjectName(u"customHorizontalSeparator_5")

        self.verticalLayout_11.addWidget(self.customHorizontalSeparator_5)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_3.addWidget(self.label_10)

        self.toLoginBtn = QPushButton(self.frame_7)
        self.toLoginBtn.setObjectName(u"toLoginBtn")
        self.toLoginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.toLoginBtn)


        self.verticalLayout_11.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.verticalLayout_8.addWidget(self.body_2)

        self.customHorizontalSeparator_6 = QCustomHorizontalSeparator(self.widget_2)
        self.customHorizontalSeparator_6.setObjectName(u"customHorizontalSeparator_6")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_6)

        self.footer_2 = QFrame(self.widget_2)
        self.footer_2.setObjectName(u"footer_2")
        self.footer_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.footer_2)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.footer_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_12)

        self.frame_8 = QFrame(self.footer_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(35, 35))
        self.pushButton_4.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(35, 35))
        self.pushButton_5.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addWidget(self.footer_2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_13.addWidget(self.widget_2)

        self.accountPages.addWidget(self.registerPage)
        self.passwordRecoveryPage = QWidget()
        self.passwordRecoveryPage.setObjectName(u"passwordRecoveryPage")
        self.verticalLayout_19 = QVBoxLayout(self.passwordRecoveryPage)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.passwordRecoveryPage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_14 = QVBoxLayout(self.widget_3)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.header_3 = QFrame(self.widget_3)
        self.header_3.setObjectName(u"header_3")
        self.header_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.header_3)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.logo_3 = QLabel(self.header_3)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setMinimumSize(QSize(141, 93))
        self.logo_3.setMaximumSize(QSize(141, 93))
        self.logo_3.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.logo_3.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.logo_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_14 = QLabel(self.header_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_14)


        self.verticalLayout_14.addWidget(self.header_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.customHorizontalSeparator_7 = QCustomHorizontalSeparator(self.widget_3)
        self.customHorizontalSeparator_7.setObjectName(u"customHorizontalSeparator_7")

        self.verticalLayout_14.addWidget(self.customHorizontalSeparator_7)

        self.body_3 = QFrame(self.widget_3)
        self.body_3.setObjectName(u"body_3")
        self.body_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.body_3)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.body_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frame_9)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(10)
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.recoveryMail = QLineEdit(self.frame_9)
        self.recoveryMail.setObjectName(u"recoveryMail")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.recoveryMail)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.body_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.recoveryMailBtn = QPushButton(self.frame_10)
        self.recoveryMailBtn.setObjectName(u"recoveryMailBtn")
        self.recoveryMailBtn.setMinimumSize(QSize(100, 0))
        self.recoveryMailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.recoveryMailBtn.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.recoveryMailBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.customHorizontalSeparator_8 = QCustomHorizontalSeparator(self.frame_10)
        self.customHorizontalSeparator_8.setObjectName(u"customHorizontalSeparator_8")

        self.verticalLayout_17.addWidget(self.customHorizontalSeparator_8)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bLoginBtn = QPushButton(self.frame_11)
        self.bLoginBtn.setObjectName(u"bLoginBtn")
        self.bLoginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.bLoginBtn)

        self.bRegBtn = QPushButton(self.frame_11)
        self.bRegBtn.setObjectName(u"bRegBtn")
        self.bRegBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.bRegBtn)


        self.verticalLayout_17.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_10)


        self.verticalLayout_14.addWidget(self.body_3, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_9 = QCustomHorizontalSeparator(self.widget_3)
        self.customHorizontalSeparator_9.setObjectName(u"customHorizontalSeparator_9")

        self.verticalLayout_14.addWidget(self.customHorizontalSeparator_9)

        self.footer_3 = QFrame(self.widget_3)
        self.footer_3.setObjectName(u"footer_3")
        self.footer_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.footer_3)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.footer_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.frame_12 = QFrame(self.footer_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(35, 35))
        self.pushButton_6.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(35, 35))
        self.pushButton_7.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.pushButton_7)


        self.verticalLayout_18.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_14.addWidget(self.footer_3, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_19.addWidget(self.widget_3)

        self.accountPages.addWidget(self.passwordRecoveryPage)
        self.passwordTokenPage = QWidget()
        self.passwordTokenPage.setObjectName(u"passwordTokenPage")
        self.verticalLayout_31 = QVBoxLayout(self.passwordTokenPage)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.passwordTokenPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_26 = QVBoxLayout(self.widget_5)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.header_5 = QFrame(self.widget_5)
        self.header_5.setObjectName(u"header_5")
        self.header_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.header_5)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.logo_5 = QLabel(self.header_5)
        self.logo_5.setObjectName(u"logo_5")
        self.logo_5.setMinimumSize(QSize(141, 93))
        self.logo_5.setMaximumSize(QSize(141, 93))
        self.logo_5.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.logo_5.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.logo_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_18 = QLabel(self.header_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_18)


        self.verticalLayout_26.addWidget(self.header_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.customHorizontalSeparator_11 = QCustomHorizontalSeparator(self.widget_5)
        self.customHorizontalSeparator_11.setObjectName(u"customHorizontalSeparator_11")

        self.verticalLayout_26.addWidget(self.customHorizontalSeparator_11)

        self.body_5 = QFrame(self.widget_5)
        self.body_5.setObjectName(u"body_5")
        self.body_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.body_5)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.body_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_6 = QFormLayout(self.frame_17)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setHorizontalSpacing(10)
        self.formLayout_6.setVerticalSpacing(0)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.mailToken = QLineEdit(self.frame_17)
        self.mailToken.setObjectName(u"mailToken")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.mailToken)

        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_28.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_18 = QFrame(self.body_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_18)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verifyTokenBtn = QPushButton(self.frame_18)
        self.verifyTokenBtn.setObjectName(u"verifyTokenBtn")
        self.verifyTokenBtn.setMinimumSize(QSize(100, 0))
        self.verifyTokenBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verifyTokenBtn.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.verifyTokenBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.customHorizontalSeparator_13 = QCustomHorizontalSeparator(self.frame_18)
        self.customHorizontalSeparator_13.setObjectName(u"customHorizontalSeparator_13")

        self.verticalLayout_29.addWidget(self.customHorizontalSeparator_13)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bLoginBtn_2 = QPushButton(self.frame_19)
        self.bLoginBtn_2.setObjectName(u"bLoginBtn_2")
        self.bLoginBtn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.bLoginBtn_2)

        self.bRegBtn_2 = QPushButton(self.frame_19)
        self.bRegBtn_2.setObjectName(u"bRegBtn_2")
        self.bRegBtn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.bRegBtn_2)


        self.verticalLayout_29.addWidget(self.frame_19, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_28.addWidget(self.frame_18)


        self.verticalLayout_26.addWidget(self.body_5, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_14 = QCustomHorizontalSeparator(self.widget_5)
        self.customHorizontalSeparator_14.setObjectName(u"customHorizontalSeparator_14")

        self.verticalLayout_26.addWidget(self.customHorizontalSeparator_14)

        self.footer_5 = QFrame(self.widget_5)
        self.footer_5.setObjectName(u"footer_5")
        self.footer_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.footer_5)
        self.verticalLayout_30.setSpacing(10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.footer_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_21)

        self.frame_20 = QFrame(self.footer_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_20)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(35, 35))
        self.pushButton_10.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_20)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(35, 35))
        self.pushButton_11.setIcon(icon1)

        self.horizontalLayout_10.addWidget(self.pushButton_11)


        self.verticalLayout_30.addWidget(self.frame_20, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_26.addWidget(self.footer_5, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_31.addWidget(self.widget_5)

        self.accountPages.addWidget(self.passwordTokenPage)
        self.resetPasswordPage = QWidget()
        self.resetPasswordPage.setObjectName(u"resetPasswordPage")
        self.verticalLayout_25 = QVBoxLayout(self.resetPasswordPage)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.resetPasswordPage)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.header_4 = QFrame(self.widget_4)
        self.header_4.setObjectName(u"header_4")
        self.header_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.header_4)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.logo_4 = QLabel(self.header_4)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setMinimumSize(QSize(141, 93))
        self.logo_4.setMaximumSize(QSize(141, 93))
        self.logo_4.setPixmap(QPixmap(u":/images/images/TRUSTED IN_GREY.png"))
        self.logo_4.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.logo_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.header_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_17)


        self.verticalLayout_20.addWidget(self.header_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.customHorizontalSeparator_10 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_10.setObjectName(u"customHorizontalSeparator_10")

        self.verticalLayout_20.addWidget(self.customHorizontalSeparator_10)

        self.body_4 = QFrame(self.widget_4)
        self.body_4.setObjectName(u"body_4")
        self.body_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.body_4)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.body_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frame_13)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(10)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.newPassword = QLineEdit(self.frame_13)
        self.newPassword.setObjectName(u"newPassword")
        self.newPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.newPassword)

        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.confirmNewPassword = QLineEdit(self.frame_13)
        self.confirmNewPassword.setObjectName(u"confirmNewPassword")
        self.confirmNewPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.confirmNewPassword)


        self.verticalLayout_22.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.body_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_14)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.resetPassBtn = QPushButton(self.frame_14)
        self.resetPassBtn.setObjectName(u"resetPassBtn")
        self.resetPassBtn.setMinimumSize(QSize(100, 0))
        self.resetPassBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resetPassBtn.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.resetPassBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_22.addWidget(self.frame_14)


        self.verticalLayout_20.addWidget(self.body_4, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_12 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_12.setObjectName(u"customHorizontalSeparator_12")

        self.verticalLayout_20.addWidget(self.customHorizontalSeparator_12)

        self.footer_4 = QFrame(self.widget_4)
        self.footer_4.setObjectName(u"footer_4")
        self.footer_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.footer_4)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.footer_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_27)

        self.frame_16 = QFrame(self.footer_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_16)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(35, 35))
        self.pushButton_8.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_16)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(35, 35))
        self.pushButton_9.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.pushButton_9)


        self.verticalLayout_24.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_20.addWidget(self.footer_4, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_25.addWidget(self.widget_4)

        self.accountPages.addWidget(self.resetPasswordPage)

        self.verticalLayout.addWidget(self.accountPages)


        self.retranslateUi(LoginFormComponent)

        self.accountPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LoginFormComponent)
    # setupUi

    def retranslateUi(self, LoginFormComponent):
        LoginFormComponent.setWindowTitle(QCoreApplication.translate("LoginFormComponent", u"CustomComponent", None))
        self.logo.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginFormComponent", u"Welcome Back", None))
        self.label.setText(QCoreApplication.translate("LoginFormComponent", u"Email", None))
        self.loginEmail.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"your@email.com", None))
        self.label_3.setText(QCoreApplication.translate("LoginFormComponent", u"Password", None))
        self.loginPassword.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Password \u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.loginBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Login", None))
        self.forgotpassBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Forgot password?", None))
        self.toRegisterBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Create Account", None))
        self.label_6.setText(QCoreApplication.translate("LoginFormComponent", u"Biometric Login", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.logo_2.setText("")
        self.label_7.setText(QCoreApplication.translate("LoginFormComponent", u"Welcome ", None))
        self.label_8.setText(QCoreApplication.translate("LoginFormComponent", u"Email", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"your@email.com", None))
        self.label_9.setText(QCoreApplication.translate("LoginFormComponent", u"Password", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Password \u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.confirmPasswordInput.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Confirm Password \u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_13.setText(QCoreApplication.translate("LoginFormComponent", u"Confirm Password", None))
        self.label_15.setText(QCoreApplication.translate("LoginFormComponent", u"Accept our Terms and Conditions.", None))
        self.label_5.setText(QCoreApplication.translate("LoginFormComponent", u"First name", None))
        self.label_11.setText(QCoreApplication.translate("LoginFormComponent", u"Last Name", None))
        self.lastNameInput.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Last Name", None))
        self.firstNameInput.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"First Name", None))
        self.registerBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Register", None))
        self.label_10.setText(QCoreApplication.translate("LoginFormComponent", u"Already registered?", None))
        self.toLoginBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Login", None))
        self.label_12.setText(QCoreApplication.translate("LoginFormComponent", u"Biometric Login", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.logo_3.setText("")
        self.label_14.setText(QCoreApplication.translate("LoginFormComponent", u"Password Recovery", None))
        self.label_16.setText(QCoreApplication.translate("LoginFormComponent", u"Email", None))
        self.recoveryMail.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"your@email.com", None))
        self.recoveryMailBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Send Recovery Email", None))
        self.bLoginBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Back to Login", None))
        self.bRegBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Create Account", None))
        self.label_20.setText(QCoreApplication.translate("LoginFormComponent", u"Biometric Login", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.logo_5.setText("")
        self.label_18.setText(QCoreApplication.translate("LoginFormComponent", u"Password Token", None))
        self.label_19.setText(QCoreApplication.translate("LoginFormComponent", u"Token", None))
        self.mailToken.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Token", None))
        self.label_4.setText(QCoreApplication.translate("LoginFormComponent", u"Enter the token sent to your email.", None))
        self.verifyTokenBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Verify Token", None))
        self.bLoginBtn_2.setText(QCoreApplication.translate("LoginFormComponent", u"Back to Login", None))
        self.bRegBtn_2.setText(QCoreApplication.translate("LoginFormComponent", u"Create Account", None))
        self.label_21.setText(QCoreApplication.translate("LoginFormComponent", u"Biometric Login", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.logo_4.setText("")
        self.label_17.setText(QCoreApplication.translate("LoginFormComponent", u"Reset Your Password", None))
        self.label_22.setText(QCoreApplication.translate("LoginFormComponent", u"Password", None))
        self.newPassword.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Password \u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_23.setText(QCoreApplication.translate("LoginFormComponent", u"Confirm Password", None))
        self.confirmNewPassword.setPlaceholderText(QCoreApplication.translate("LoginFormComponent", u"Confirm Password \u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.resetPassBtn.setText(QCoreApplication.translate("LoginFormComponent", u"Reset Password", None))
        self.label_27.setText(QCoreApplication.translate("LoginFormComponent", u"Biometric Login", None))
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
    # retranslateUi


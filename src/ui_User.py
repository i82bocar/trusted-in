# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_User.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_UserComponent(object):
    def setupUi(self, UserComponent):
        if not UserComponent.objectName():
            UserComponent.setObjectName(u"UserComponent")
        UserComponent.resize(930, 508)
        self.verticalLayout = QVBoxLayout(UserComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(UserComponent)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.welcomeName = QLabel(self.frame)
        self.welcomeName.setObjectName(u"welcomeName")

        self.verticalLayout_2.addWidget(self.welcomeName)

        self.welcomeMessage = QLabel(self.frame)
        self.welcomeMessage.setObjectName(u"welcomeMessage")
        self.welcomeMessage.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.welcomeMessage)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(UserComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.widget_2 = QWidget(UserComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.customHorizontalSeparator_8 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_8.setObjectName(u"customHorizontalSeparator_8")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_8)

        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator)

        self.frame_11 = QFrame(self.widget_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.profileNameLabel = QLabel(self.frame_11)
        self.profileNameLabel.setObjectName(u"profileNameLabel")

        self.horizontalLayout_14.addWidget(self.profileNameLabel)

        self.editUsernameBtn = QPushButton(self.frame_11)
        self.editUsernameBtn.setObjectName(u"editUsernameBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/edit-2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editUsernameBtn.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.editUsernameBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.profileEmailLabel = QLabel(self.frame_6)
        self.profileEmailLabel.setObjectName(u"profileEmailLabel")

        self.horizontalLayout_9.addWidget(self.profileEmailLabel)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/verified.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.logoutBtn = QPushButton(self.widget_4)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.logoutBtn)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_2)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.deleteAccountBtn = QPushButton(self.frame_4)
        self.deleteAccountBtn.setObjectName(u"deleteAccountBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/delete_forever.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteAccountBtn.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.deleteAccountBtn)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(UserComponent)

        QMetaObject.connectSlotsByName(UserComponent)
    # setupUi

    def retranslateUi(self, UserComponent):
        UserComponent.setWindowTitle(QCoreApplication.translate("UserComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("UserComponent", u"User Profile", None))
        self.welcomeMessage.setText(QCoreApplication.translate("UserComponent", u"Manage your account, profile details, and preferences.", None))
        self.label.setText(QCoreApplication.translate("UserComponent", u"Profile Overview", None))
        self.label_3.setText("")
        self.profileNameLabel.setText(QCoreApplication.translate("UserComponent", u"Alex Johnson", None))
        self.editUsernameBtn.setText("")
        self.profileEmailLabel.setText(QCoreApplication.translate("UserComponent", u"alex@email.com", None))
        self.pushButton_8.setText("")
        self.logoutBtn.setText(QCoreApplication.translate("UserComponent", u"Logout", None))
        self.deleteAccountBtn.setText(QCoreApplication.translate("UserComponent", u"Delete Account", None))
    # retranslateUi


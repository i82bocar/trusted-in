# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Vault.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
class Ui_VaultComponent(object):
    def setupUi(self, VaultComponent):
        if not VaultComponent.objectName():
            VaultComponent.setObjectName(u"VaultComponent")
        VaultComponent.resize(843, 266)
        VaultComponent.setProperty("liveCompileStylesheet", False)
        VaultComponent.setProperty("paintQtDesignerUI", False)
        self.verticalLayout = QVBoxLayout(VaultComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(VaultComponent)
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

        self.searchFrame = QFrame(self.header)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(200, 0))
        self.searchFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.searchFrame)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.searchInput = QLineEdit(self.searchFrame)
        self.searchInput.setObjectName(u"searchInput")

        self.horizontalLayout_2.addWidget(self.searchInput)


        self.horizontalLayout.addWidget(self.searchFrame, 0, Qt.AlignmentFlag.AlignRight)

        self.clearSearchBtn = QPushButton(self.header)
        self.clearSearchBtn.setObjectName(u"clearSearchBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearSearchBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.clearSearchBtn)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addBtn = QPushButton(self.frame_2)
        self.addBtn.setObjectName(u"addBtn")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_solid/icons/font_awesome/solid/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addBtn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.addBtn)

        self.refreshBtn = QPushButton(self.frame_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshBtn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.refreshBtn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(VaultComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.widget_3 = QWidget(VaultComponent)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.widget_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.passwordTab = QWidget()
        self.passwordTab.setObjectName(u"passwordTab")
        self.verticalLayout_3 = QVBoxLayout(self.passwordTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabHeader = QWidget(self.passwordTab)
        self.tabHeader.setObjectName(u"tabHeader")
        self.tabHeader.setMaximumSize(QSize(16777215, 20))
        self.gridLayout_2 = QGridLayout(self.tabHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.tabHeader)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(150, 0))
        self.frame_10.setMaximumSize(QSize(150, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_8)


        self.gridLayout_2.addWidget(self.frame_10, 0, 0, 1, 1)

        self.customVerticalSeparator_6 = QCustomVerticalSeparator(self.tabHeader)
        self.customVerticalSeparator_6.setObjectName(u"customVerticalSeparator_6")
        self.customVerticalSeparator_6.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.customVerticalSeparator_6, 0, 6, 1, 1)

        self.customVerticalSeparator_5 = QCustomVerticalSeparator(self.tabHeader)
        self.customVerticalSeparator_5.setObjectName(u"customVerticalSeparator_5")
        self.customVerticalSeparator_5.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.customVerticalSeparator_5, 0, 4, 1, 1)

        self.frame_9 = QFrame(self.tabHeader)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 0))
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_9, 0, 7, 1, 1)

        self.frame_7 = QFrame(self.tabHeader)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.frame_7, 0, 3, 1, 1)

        self.frame_8 = QFrame(self.tabHeader)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(150, 0))
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)


        self.gridLayout_2.addWidget(self.frame_8, 0, 5, 1, 1)

        self.customVerticalSeparator_4 = QCustomVerticalSeparator(self.tabHeader)
        self.customVerticalSeparator_4.setObjectName(u"customVerticalSeparator_4")
        self.customVerticalSeparator_4.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.customVerticalSeparator_4, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.tabHeader)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.passwordTab)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator)

        self.passwordList = QWidget(self.passwordTab)
        self.passwordList.setObjectName(u"passwordList")
        self.verticalLayout_5 = QVBoxLayout(self.passwordList)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.passwordList)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/password.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.passwordTab, icon4, "")
        self.notesTab = QWidget()
        self.notesTab.setObjectName(u"notesTab")
        self.verticalLayout_9 = QVBoxLayout(self.notesTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabHeader_4 = QWidget(self.notesTab)
        self.tabHeader_4.setObjectName(u"tabHeader_4")
        self.tabHeader_4.setMaximumSize(QSize(16777215, 20))
        self.gridLayout_8 = QGridLayout(self.tabHeader_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.tabHeader_4)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(150, 0))
        self.frame_27.setMaximumSize(QSize(150, 16777215))
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_27)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_35)


        self.gridLayout_8.addWidget(self.frame_27, 0, 0, 1, 1)

        self.customVerticalSeparator_19 = QCustomVerticalSeparator(self.tabHeader_4)
        self.customVerticalSeparator_19.setObjectName(u"customVerticalSeparator_19")
        self.customVerticalSeparator_19.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.customVerticalSeparator_19, 0, 6, 1, 1)

        self.customVerticalSeparator_20 = QCustomVerticalSeparator(self.tabHeader_4)
        self.customVerticalSeparator_20.setObjectName(u"customVerticalSeparator_20")
        self.customVerticalSeparator_20.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.customVerticalSeparator_20, 0, 4, 1, 1)

        self.frame_28 = QFrame(self.tabHeader_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(200, 0))
        self.frame_28.setMaximumSize(QSize(200, 16777215))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_36, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_8.addWidget(self.frame_28, 0, 7, 1, 1)

        self.frame_29 = QFrame(self.tabHeader_4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(150, 0))
        self.frame_29.setMaximumSize(QSize(150, 16777215))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_29)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_37)


        self.gridLayout_8.addWidget(self.frame_29, 0, 3, 1, 1)

        self.frame_30 = QFrame(self.tabHeader_4)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(150, 0))
        self.frame_30.setMaximumSize(QSize(150, 16777215))
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_38)


        self.gridLayout_8.addWidget(self.frame_30, 0, 5, 1, 1)

        self.customVerticalSeparator_21 = QCustomVerticalSeparator(self.tabHeader_4)
        self.customVerticalSeparator_21.setObjectName(u"customVerticalSeparator_21")
        self.customVerticalSeparator_21.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.customVerticalSeparator_21, 0, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.tabHeader_4)

        self.customHorizontalSeparator_7 = QCustomHorizontalSeparator(self.notesTab)
        self.customHorizontalSeparator_7.setObjectName(u"customHorizontalSeparator_7")

        self.verticalLayout_9.addWidget(self.customHorizontalSeparator_7)

        self.notesList = QWidget(self.notesTab)
        self.notesList.setObjectName(u"notesList")
        self.verticalLayout_8 = QVBoxLayout(self.notesList)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout_9.addWidget(self.notesList)

        self.verticalSpacer_4 = QSpacerItem(20, 352, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_solid/icons/font_awesome/solid/note-sticky.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.notesTab, icon5, "")
        self.paymentCardsTab = QWidget()
        self.paymentCardsTab.setObjectName(u"paymentCardsTab")
        self.verticalLayout_11 = QVBoxLayout(self.paymentCardsTab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabHeader_3 = QWidget(self.paymentCardsTab)
        self.tabHeader_3.setObjectName(u"tabHeader_3")
        self.tabHeader_3.setMaximumSize(QSize(16777215, 20))
        self.gridLayout_6 = QGridLayout(self.tabHeader_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.tabHeader_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(150, 0))
        self.frame_19.setMaximumSize(QSize(150, 16777215))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_27)


        self.gridLayout_6.addWidget(self.frame_19, 0, 0, 1, 1)

        self.customVerticalSeparator_13 = QCustomVerticalSeparator(self.tabHeader_3)
        self.customVerticalSeparator_13.setObjectName(u"customVerticalSeparator_13")
        self.customVerticalSeparator_13.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_6.addWidget(self.customVerticalSeparator_13, 0, 6, 1, 1)

        self.customVerticalSeparator_14 = QCustomVerticalSeparator(self.tabHeader_3)
        self.customVerticalSeparator_14.setObjectName(u"customVerticalSeparator_14")
        self.customVerticalSeparator_14.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_6.addWidget(self.customVerticalSeparator_14, 0, 4, 1, 1)

        self.frame_20 = QFrame(self.tabHeader_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 0))
        self.frame_20.setMaximumSize(QSize(200, 16777215))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_20)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_20, 0, 7, 1, 1)

        self.frame_21 = QFrame(self.tabHeader_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(150, 0))
        self.frame_21.setMaximumSize(QSize(150, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_21)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_29)


        self.gridLayout_6.addWidget(self.frame_21, 0, 3, 1, 1)

        self.frame_22 = QFrame(self.tabHeader_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(150, 0))
        self.frame_22.setMaximumSize(QSize(150, 16777215))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_22)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_30)


        self.gridLayout_6.addWidget(self.frame_22, 0, 5, 1, 1)

        self.customVerticalSeparator_15 = QCustomVerticalSeparator(self.tabHeader_3)
        self.customVerticalSeparator_15.setObjectName(u"customVerticalSeparator_15")
        self.customVerticalSeparator_15.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_6.addWidget(self.customVerticalSeparator_15, 0, 2, 1, 1)


        self.verticalLayout_11.addWidget(self.tabHeader_3)

        self.customHorizontalSeparator_6 = QCustomHorizontalSeparator(self.paymentCardsTab)
        self.customHorizontalSeparator_6.setObjectName(u"customHorizontalSeparator_6")

        self.verticalLayout_11.addWidget(self.customHorizontalSeparator_6)

        self.paymentCardsList = QWidget(self.paymentCardsTab)
        self.paymentCardsList.setObjectName(u"paymentCardsList")
        self.verticalLayout_7 = QVBoxLayout(self.paymentCardsList)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_11.addWidget(self.paymentCardsList)

        self.verticalSpacer_3 = QSpacerItem(20, 352, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_solid/icons/font_awesome/solid/credit-card.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.paymentCardsTab, icon6, "")
        self.contactsTab = QWidget()
        self.contactsTab.setObjectName(u"contactsTab")
        self.verticalLayout_10 = QVBoxLayout(self.contactsTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabHeader_2 = QWidget(self.contactsTab)
        self.tabHeader_2.setObjectName(u"tabHeader_2")
        self.tabHeader_2.setMaximumSize(QSize(16777215, 20))
        self.gridLayout_4 = QGridLayout(self.tabHeader_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.tabHeader_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(150, 0))
        self.frame_11.setMaximumSize(QSize(150, 16777215))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_19)


        self.gridLayout_4.addWidget(self.frame_11, 0, 0, 1, 1)

        self.customVerticalSeparator_7 = QCustomVerticalSeparator(self.tabHeader_2)
        self.customVerticalSeparator_7.setObjectName(u"customVerticalSeparator_7")
        self.customVerticalSeparator_7.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.customVerticalSeparator_7, 0, 6, 1, 1)

        self.customVerticalSeparator_8 = QCustomVerticalSeparator(self.tabHeader_2)
        self.customVerticalSeparator_8.setObjectName(u"customVerticalSeparator_8")
        self.customVerticalSeparator_8.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.customVerticalSeparator_8, 0, 4, 1, 1)

        self.frame_12 = QFrame(self.tabHeader_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(200, 0))
        self.frame_12.setMaximumSize(QSize(200, 16777215))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_12, 0, 7, 1, 1)

        self.frame_13 = QFrame(self.tabHeader_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(150, 0))
        self.frame_13.setMaximumSize(QSize(150, 16777215))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_21)


        self.gridLayout_4.addWidget(self.frame_13, 0, 3, 1, 1)

        self.frame_14 = QFrame(self.tabHeader_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(150, 0))
        self.frame_14.setMaximumSize(QSize(150, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_22)


        self.gridLayout_4.addWidget(self.frame_14, 0, 5, 1, 1)

        self.customVerticalSeparator_9 = QCustomVerticalSeparator(self.tabHeader_2)
        self.customVerticalSeparator_9.setObjectName(u"customVerticalSeparator_9")
        self.customVerticalSeparator_9.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.customVerticalSeparator_9, 0, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.tabHeader_2)

        self.customHorizontalSeparator_5 = QCustomHorizontalSeparator(self.contactsTab)
        self.customHorizontalSeparator_5.setObjectName(u"customHorizontalSeparator_5")

        self.verticalLayout_10.addWidget(self.customHorizontalSeparator_5)

        self.contactsList = QWidget(self.contactsTab)
        self.contactsList.setObjectName(u"contactsList")
        self.verticalLayout_6 = QVBoxLayout(self.contactsList)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_10.addWidget(self.contactsList)

        self.verticalSpacer_2 = QSpacerItem(20, 352, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/contact_phone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.contactsTab, icon7, "")

        self.horizontalLayout_12.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(VaultComponent)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VaultComponent)
    # setupUi

    def retranslateUi(self, VaultComponent):
        VaultComponent.setWindowTitle(QCoreApplication.translate("VaultComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("VaultComponent", u"Secure Vault", None))
        self.welcomeMessage.setText(QCoreApplication.translate("VaultComponent", u"Browse your saved passwords, notes, payment cards, contacts and bank accounts.", None))
        self.pushButton.setText("")
        self.searchInput.setPlaceholderText(QCoreApplication.translate("VaultComponent", u"Search for something..", None))
        self.clearSearchBtn.setText("")
        self.addBtn.setText("")
        self.refreshBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("VaultComponent", u"Item Name", None))
        self.label_7.setText(QCoreApplication.translate("VaultComponent", u"Actions", None))
        self.label_5.setText(QCoreApplication.translate("VaultComponent", u"Type ", None))
        self.label_6.setText(QCoreApplication.translate("VaultComponent", u"Last Modified", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.passwordTab), QCoreApplication.translate("VaultComponent", u"Passwords", None))
        self.label_35.setText(QCoreApplication.translate("VaultComponent", u"Item Name", None))
        self.label_36.setText(QCoreApplication.translate("VaultComponent", u"Actions", None))
        self.label_37.setText(QCoreApplication.translate("VaultComponent", u"Type ", None))
        self.label_38.setText(QCoreApplication.translate("VaultComponent", u"Last Modified", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), QCoreApplication.translate("VaultComponent", u"Notes", None))
        self.label_27.setText(QCoreApplication.translate("VaultComponent", u"Item Name", None))
        self.label_28.setText(QCoreApplication.translate("VaultComponent", u"Actions", None))
        self.label_29.setText(QCoreApplication.translate("VaultComponent", u"Type ", None))
        self.label_30.setText(QCoreApplication.translate("VaultComponent", u"Last Modified", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.paymentCardsTab), QCoreApplication.translate("VaultComponent", u"Payment Cards", None))
        self.label_19.setText(QCoreApplication.translate("VaultComponent", u"Item Name", None))
        self.label_20.setText(QCoreApplication.translate("VaultComponent", u"Actions", None))
        self.label_21.setText(QCoreApplication.translate("VaultComponent", u"Type ", None))
        self.label_22.setText(QCoreApplication.translate("VaultComponent", u"Last Modified", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contactsTab), QCoreApplication.translate("VaultComponent", u"Contacts", None))
    # retranslateUi


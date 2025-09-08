# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Dashboard.ui'
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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomProgressBars import QCustomRoundProgressBar
class Ui_DashboardComponent(object):
    def setupUi(self, DashboardComponent):
        if not DashboardComponent.objectName():
            DashboardComponent.setObjectName(u"DashboardComponent")
        DashboardComponent.resize(878, 509)
        DashboardComponent.setMinimumSize(QSize(862, 501))
        self.verticalLayout = QVBoxLayout(DashboardComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(DashboardComponent)
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

        self.verticalLayout_2.addWidget(self.welcomeMessage)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.addBtn)

        self.notificationBtn = QPushButton(self.frame_2)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.notificationBtn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(DashboardComponent)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_2)

        self.widget_2 = QWidget(DashboardComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.customHorizontalSeparator_8 = QCustomHorizontalSeparator(self.widget_3)
        self.customHorizontalSeparator_8.setObjectName(u"customHorizontalSeparator_8")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_8)

        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.vaultScoreProgressBar = QCustomRoundProgressBar(self.frame_3)
        self.vaultScoreProgressBar.setObjectName(u"vaultScoreProgressBar")
        self.vaultScoreProgressBar.setMinimumSize(QSize(50, 50))
        self.vaultScoreProgressBar.setMaximumSize(QSize(50, 50))
        self.vaultScoreProgressBar.setProperty("value", 40)

        self.horizontalLayout_5.addWidget(self.vaultScoreProgressBar)

        self.quickFixBtn = QPushButton(self.frame_3)
        self.quickFixBtn.setObjectName(u"quickFixBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/tool.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quickFixBtn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.quickFixBtn)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.customHorizontalSeparator_9 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_9.setObjectName(u"customHorizontalSeparator_9")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_9)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.breachLabel = QLabel(self.frame_4)
        self.breachLabel.setObjectName(u"breachLabel")
        self.breachLabel.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.breachLabel)

        self.breachBtn = QPushButton(self.frame_4)
        self.breachBtn.setObjectName(u"breachBtn")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.breachBtn.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.breachBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.customHorizontalSeparator_10 = QCustomHorizontalSeparator(self.widget_5)
        self.customHorizontalSeparator_10.setObjectName(u"customHorizontalSeparator_10")

        self.verticalLayout_5.addWidget(self.customHorizontalSeparator_10)

        self.frame_5 = QFrame(self.widget_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.generatorBtn = QPushButton(self.frame_5)
        self.generatorBtn.setObjectName(u"generatorBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/generating_tokens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generatorBtn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.generatorBtn)

        self.settingsBtn = QPushButton(self.frame_5)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.settingsBtn)

        self.userBtn = QPushButton(self.frame_5)
        self.userBtn.setObjectName(u"userBtn")
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.userBtn.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.userBtn)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(DashboardComponent)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout.addWidget(self.customHorizontalSeparator)

        self.widget_6 = QWidget(DashboardComponent)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.customHorizontalSeparator_5 = QCustomHorizontalSeparator(self.widget_7)
        self.customHorizontalSeparator_5.setObjectName(u"customHorizontalSeparator_5")

        self.verticalLayout_6.addWidget(self.customHorizontalSeparator_5)

        self.frame_6 = QFrame(self.widget_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.weakPassLabel = QLabel(self.frame_6)
        self.weakPassLabel.setObjectName(u"weakPassLabel")
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        self.weakPassLabel.setFont(font2)
        self.weakPassLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.weakPassLabel)

        self.viewWeakPass = QPushButton(self.frame_6)
        self.viewWeakPass.setObjectName(u"viewWeakPass")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/browser_updated.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewWeakPass.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.viewWeakPass)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_11.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.customHorizontalSeparator_6 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_6.setObjectName(u"customHorizontalSeparator_6")

        self.verticalLayout_7.addWidget(self.customHorizontalSeparator_6)

        self.frame_7 = QFrame(self.widget_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.reusedPassLabel = QLabel(self.frame_7)
        self.reusedPassLabel.setObjectName(u"reusedPassLabel")
        self.reusedPassLabel.setFont(font2)
        self.reusedPassLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reusedPassLabel.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.reusedPassLabel)

        self.viewpassBtn = QPushButton(self.frame_7)
        self.viewpassBtn.setObjectName(u"viewpassBtn")
        self.viewpassBtn.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.viewpassBtn)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.horizontalLayout_11.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_8 = QVBoxLayout(self.widget_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.customHorizontalSeparator_7 = QCustomHorizontalSeparator(self.widget_9)
        self.customHorizontalSeparator_7.setObjectName(u"customHorizontalSeparator_7")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_7)

        self.frame_8 = QFrame(self.widget_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.oldPassLabel = QLabel(self.frame_8)
        self.oldPassLabel.setObjectName(u"oldPassLabel")
        self.oldPassLabel.setFont(font2)
        self.oldPassLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.oldPassLabel)

        self.updatePassBtn = QPushButton(self.frame_8)
        self.updatePassBtn.setObjectName(u"updatePassBtn")
        self.updatePassBtn.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.updatePassBtn)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.horizontalLayout_11.addWidget(self.widget_9)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_13 = QFrame(self.widget_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.vaultBtn = QPushButton(self.frame_13)
        self.vaultBtn.setObjectName(u"vaultBtn")
        icon8 = QIcon()
        icon8.addFile(u":/font_awesome_solid/icons/font_awesome/solid/shield.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vaultBtn.setIcon(icon8)

        self.horizontalLayout_16.addWidget(self.vaultBtn)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.customHorizontalSeparator_4 = QCustomHorizontalSeparator(self.widget_11)
        self.customHorizontalSeparator_4.setObjectName(u"customHorizontalSeparator_4")

        self.verticalLayout_9.addWidget(self.customHorizontalSeparator_4)

        self.frame_12 = QFrame(self.widget_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_12)
        self.formLayout.setObjectName(u"formLayout")
        self.totalPassLabel = QLabel(self.frame_12)
        self.totalPassLabel.setObjectName(u"totalPassLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.totalPassLabel)

        self.totalNotesLabel = QLabel(self.frame_12)
        self.totalNotesLabel.setObjectName(u"totalNotesLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.totalNotesLabel)

        self.totalCardsLabel = QLabel(self.frame_12)
        self.totalCardsLabel.setObjectName(u"totalCardsLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.totalCardsLabel)

        self.totalContactsLabel = QLabel(self.frame_12)
        self.totalContactsLabel.setObjectName(u"totalContactsLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.totalContactsLabel)


        self.verticalLayout_9.addWidget(self.frame_12)


        self.horizontalLayout_11.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignTop)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(DashboardComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.footer = QWidget(DashboardComponent)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_12 = QHBoxLayout(self.footer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_9 = QFrame(self.footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(20, 20))
        self.label_8.setMaximumSize(QSize(20, 20))
        self.label_8.setPixmap(QPixmap(u":/material_design/icons/material_design/settings_backup_restore.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_8)

        self.lastBackupLabel = QLabel(self.frame_9)
        self.lastBackupLabel.setObjectName(u"lastBackupLabel")

        self.horizontalLayout_13.addWidget(self.lastBackupLabel)


        self.horizontalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.footer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 20))
        self.label_10.setMaximumSize(QSize(20, 20))
        self.label_10.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/lock.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.encryptionStatusLabel = QLabel(self.frame_10)
        self.encryptionStatusLabel.setObjectName(u"encryptionStatusLabel")

        self.horizontalLayout_14.addWidget(self.encryptionStatusLabel)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.footer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(20, 20))
        self.label_12.setMaximumSize(QSize(20, 20))
        self.label_12.setPixmap(QPixmap(u":/material_design/icons/material_design/sd_storage.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.storageUsedLabel = QLabel(self.frame_11)
        self.storageUsedLabel.setObjectName(u"storageUsedLabel")

        self.horizontalLayout_15.addWidget(self.storageUsedLabel)

        self.storageProgressBar = QProgressBar(self.frame_11)
        self.storageProgressBar.setObjectName(u"storageProgressBar")
        self.storageProgressBar.setMinimumSize(QSize(0, 10))
        self.storageProgressBar.setMaximumSize(QSize(500, 10))
        self.storageProgressBar.setValue(24)

        self.horizontalLayout_15.addWidget(self.storageProgressBar)


        self.horizontalLayout_12.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.footer)


        self.retranslateUi(DashboardComponent)

        QMetaObject.connectSlotsByName(DashboardComponent)
    # setupUi

    def retranslateUi(self, DashboardComponent):
        DashboardComponent.setWindowTitle(QCoreApplication.translate("DashboardComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("DashboardComponent", u"Hello, Alex!", None))
        self.welcomeMessage.setText(QCoreApplication.translate("DashboardComponent", u"Welcome back.Ready for some encrypton?", None))
        self.addBtn.setText("")
        self.notificationBtn.setText("")
        self.label.setText(QCoreApplication.translate("DashboardComponent", u"Vault Health Scroe", None))
        self.quickFixBtn.setText(QCoreApplication.translate("DashboardComponent", u"Quick fix", None))
        self.label_2.setText(QCoreApplication.translate("DashboardComponent", u"Breach Alerts", None))
        self.breachLabel.setText(QCoreApplication.translate("DashboardComponent", u"5 credentials exposed in breaches", None))
        self.breachBtn.setText(QCoreApplication.translate("DashboardComponent", u"View Details", None))
        self.label_4.setText(QCoreApplication.translate("DashboardComponent", u"Quick Actions", None))
        self.generatorBtn.setText("")
        self.settingsBtn.setText("")
        self.userBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("DashboardComponent", u"Weak Passwords", None))
        self.weakPassLabel.setText(QCoreApplication.translate("DashboardComponent", u"24", None))
        self.viewWeakPass.setText(QCoreApplication.translate("DashboardComponent", u"Update All", None))
        self.label_5.setText(QCoreApplication.translate("DashboardComponent", u"Reused Passwords", None))
        self.reusedPassLabel.setText(QCoreApplication.translate("DashboardComponent", u"3", None))
        self.viewpassBtn.setText(QCoreApplication.translate("DashboardComponent", u"View ", None))
        self.label_6.setText(QCoreApplication.translate("DashboardComponent", u"Old Passwords", None))
        self.oldPassLabel.setText(QCoreApplication.translate("DashboardComponent", u"120", None))
        self.updatePassBtn.setText(QCoreApplication.translate("DashboardComponent", u"Update All", None))
        self.label_15.setText(QCoreApplication.translate("DashboardComponent", u"Vault Statistics", None))
        self.vaultBtn.setText(QCoreApplication.translate("DashboardComponent", u"View Vault", None))
        self.totalPassLabel.setText(QCoreApplication.translate("DashboardComponent", u"Total passwords: 211", None))
        self.totalNotesLabel.setText(QCoreApplication.translate("DashboardComponent", u"Secure notes: 34", None))
        self.totalCardsLabel.setText(QCoreApplication.translate("DashboardComponent", u"Payment cards: 3", None))
        self.totalContactsLabel.setText(QCoreApplication.translate("DashboardComponent", u"TextLabel", None))
        self.label_8.setText("")
        self.lastBackupLabel.setText(QCoreApplication.translate("DashboardComponent", u"Last Backup: ", None))
        self.label_10.setText("")
        self.encryptionStatusLabel.setText(QCoreApplication.translate("DashboardComponent", u"Encryption Status: AES-256 Active", None))
        self.label_12.setText("")
        self.storageUsedLabel.setText(QCoreApplication.translate("DashboardComponent", u"Storage Used:", None))
    # retranslateUi


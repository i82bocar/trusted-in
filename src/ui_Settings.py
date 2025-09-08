# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomThemeDarkLightToggle import QCustomThemeDarkLightToggle
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
class Ui_SettingsComponent(object):
    def setupUi(self, SettingsComponent):
        if not SettingsComponent.objectName():
            SettingsComponent.setObjectName(u"SettingsComponent")
        SettingsComponent.resize(970, 821)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsComponent.sizePolicy().hasHeightForWidth())
        SettingsComponent.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(SettingsComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(SettingsComponent)
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

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.saveSettingsBtn = QPushButton(self.frame_2)
        self.saveSettingsBtn.setObjectName(u"saveSettingsBtn")
        font = QFont()
        font.setBold(True)
        self.saveSettingsBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveSettingsBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.saveSettingsBtn)

        self.resetSettingsBtn = QPushButton(self.frame_2)
        self.resetSettingsBtn.setObjectName(u"resetSettingsBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/settings_backup_restore.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetSettingsBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.resetSettingsBtn)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.header)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(SettingsComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.widget_2 = QWidget(SettingsComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
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

        self.horizontalLayout_5.addWidget(self.label_3)

        self.autoLockComboBox = QComboBox(self.frame_3)
        self.autoLockComboBox.addItem("")
        self.autoLockComboBox.addItem("")
        self.autoLockComboBox.addItem("")
        self.autoLockComboBox.addItem("")
        self.autoLockComboBox.addItem("")
        self.autoLockComboBox.setObjectName(u"autoLockComboBox")
        self.autoLockComboBox.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.autoLockComboBox)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.customHorizontalSeparator_9 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_9.setObjectName(u"customHorizontalSeparator_9")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_9)

        self.frame_11 = QFrame(self.widget_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.comboBox_4 = QComboBox(self.frame_11)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.comboBox_4)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.customHorizontalSeparator_11 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_11.setObjectName(u"customHorizontalSeparator_11")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_11)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.CustomThemeDarkLightToggle = QCustomThemeDarkLightToggle(self.frame_6)
        self.CustomThemeDarkLightToggle.setObjectName(u"CustomThemeDarkLightToggle")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/dark_mode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CustomThemeDarkLightToggle.setProperty("darkThemeIcon", icon2)
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/light_mode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CustomThemeDarkLightToggle.setProperty("lightThemeIcon", icon3)

        self.horizontalLayout_9.addWidget(self.CustomThemeDarkLightToggle)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.customHorizontalSeparator_14 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_14.setObjectName(u"customHorizontalSeparator_14")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_14)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.breachAlertSwitch = QCustomCheckBox(self.frame_4)
        self.breachAlertSwitch.setObjectName(u"breachAlertSwitch")

        self.horizontalLayout_6.addWidget(self.breachAlertSwitch)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.customHorizontalSeparator_15 = QCustomHorizontalSeparator(self.widget_4)
        self.customHorizontalSeparator_15.setObjectName(u"customHorizontalSeparator_15")

        self.verticalLayout_3.addWidget(self.customHorizontalSeparator_15)

        self.frame_12 = QFrame(self.widget_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clipboardNotifySwitch = QCustomCheckBox(self.frame_12)
        self.clipboardNotifySwitch.setObjectName(u"clipboardNotifySwitch")

        self.horizontalLayout_2.addWidget(self.clipboardNotifySwitch)

        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_12)


        self.horizontalLayout_4.addWidget(self.widget_4)

        self.customVerticalSeparator = QCustomVerticalSeparator(self.widget_2)
        self.customVerticalSeparator.setObjectName(u"customVerticalSeparator")

        self.horizontalLayout_4.addWidget(self.customVerticalSeparator)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_29 = QLabel(self.widget_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.verticalLayout_6.addWidget(self.label_29)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_6.addWidget(self.customHorizontalSeparator_2)

        self.frame_14 = QFrame(self.widget_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.frame_14)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.encryptionComboBox = QComboBox(self.frame_14)
        self.encryptionComboBox.addItem("")
        self.encryptionComboBox.addItem("")
        self.encryptionComboBox.addItem("")
        self.encryptionComboBox.setObjectName(u"encryptionComboBox")
        self.encryptionComboBox.setEnabled(False)
        self.encryptionComboBox.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_16.addWidget(self.encryptionComboBox)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.customHorizontalSeparator_6 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_6.setObjectName(u"customHorizontalSeparator_6")

        self.verticalLayout_6.addWidget(self.customHorizontalSeparator_6)

        self.label_28 = QLabel(self.widget_8)
        self.label_28.setObjectName(u"label_28")
        font2 = QFont()
        self.label_28.setFont(font2)
        self.label_28.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_28)

        self.frame_15 = QFrame(self.widget_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.exportVaultBtn = QPushButton(self.frame_15)
        self.exportVaultBtn.setObjectName(u"exportVaultBtn")

        self.horizontalLayout_17.addWidget(self.exportVaultBtn)

        self.lastBackupLabel = QLabel(self.frame_15)
        self.lastBackupLabel.setObjectName(u"lastBackupLabel")
        self.lastBackupLabel.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.lastBackupLabel)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.importVaultBtn = QPushButton(self.widget_8)
        self.importVaultBtn.setObjectName(u"importVaultBtn")

        self.verticalLayout_6.addWidget(self.importVaultBtn)

        self.customHorizontalSeparator_7 = QCustomHorizontalSeparator(self.widget_8)
        self.customHorizontalSeparator_7.setObjectName(u"customHorizontalSeparator_7")

        self.verticalLayout_6.addWidget(self.customHorizontalSeparator_7)

        self.label_31 = QLabel(self.widget_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_31)

        self.frame_16 = QFrame(self.widget_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.syncVaultBtn = QPushButton(self.frame_16)
        self.syncVaultBtn.setObjectName(u"syncVaultBtn")

        self.horizontalLayout_18.addWidget(self.syncVaultBtn)

        self.lastSyncLabel = QLabel(self.frame_16)
        self.lastSyncLabel.setObjectName(u"lastSyncLabel")
        self.lastSyncLabel.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.lastSyncLabel)


        self.verticalLayout_6.addWidget(self.frame_16)


        self.horizontalLayout_4.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget_2)

        self.customHorizontalSeparator_19 = QCustomHorizontalSeparator(SettingsComponent)
        self.customHorizontalSeparator_19.setObjectName(u"customHorizontalSeparator_19")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_19)

        self.widget_7 = QWidget(SettingsComponent)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_22)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.widget_5)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator)

        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.clipboardComboBox = QComboBox(self.frame_8)
        self.clipboardComboBox.addItem("")
        self.clipboardComboBox.addItem("")
        self.clipboardComboBox.addItem("")
        self.clipboardComboBox.addItem("")
        self.clipboardComboBox.addItem("")
        self.clipboardComboBox.setObjectName(u"clipboardComboBox")
        self.clipboardComboBox.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_11.addWidget(self.clipboardComboBox)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_11.addWidget(self.label_24)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.customHorizontalSeparator_16 = QCustomHorizontalSeparator(self.widget_5)
        self.customHorizontalSeparator_16.setObjectName(u"customHorizontalSeparator_16")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_16)

        self.frame_13 = QFrame(self.widget_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.clearClipboardSwitch = QCustomCheckBox(self.frame_13)
        self.clearClipboardSwitch.setObjectName(u"clearClipboardSwitch")

        self.horizontalLayout_15.addWidget(self.clearClipboardSwitch)

        self.label_25 = QLabel(self.frame_13)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.label_25)


        self.verticalLayout_4.addWidget(self.frame_13)


        self.horizontalLayout_8.addWidget(self.widget_5)

        self.customVerticalSeparator_3 = QCustomVerticalSeparator(self.widget_7)
        self.customVerticalSeparator_3.setObjectName(u"customVerticalSeparator_3")

        self.horizontalLayout_8.addWidget(self.customVerticalSeparator_3)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.customHorizontalSeparator_12 = QCustomHorizontalSeparator(self.widget_9)
        self.customHorizontalSeparator_12.setObjectName(u"customHorizontalSeparator_12")

        self.verticalLayout_7.addWidget(self.customHorizontalSeparator_12)

        self.frame_7 = QFrame(self.widget_9)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_16)

        self.changePasswordBtn = QPushButton(self.frame_7)
        self.changePasswordBtn.setObjectName(u"changePasswordBtn")

        self.verticalLayout_9.addWidget(self.changePasswordBtn)

        self.label_3h_2 = QLabel(self.frame_7)
        self.label_3h_2.setObjectName(u"label_3h_2")
        self.label_3h_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3h_2.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_3h_2)

        self.resetVaultBtn = QPushButton(self.frame_7)
        self.resetVaultBtn.setObjectName(u"resetVaultBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/warning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetVaultBtn.setIcon(icon4)

        self.verticalLayout_9.addWidget(self.resetVaultBtn)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.horizontalLayout_8.addWidget(self.widget_9)

        self.customVerticalSeparator_4 = QCustomVerticalSeparator(self.widget_7)
        self.customVerticalSeparator_4.setObjectName(u"customVerticalSeparator_4")

        self.horizontalLayout_8.addWidget(self.customVerticalSeparator_4)

        self.widget_10m = QWidget(self.widget_7)
        self.widget_10m.setObjectName(u"widget_10m")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10m)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget_10m)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.customHorizontalSeparator_13 = QCustomHorizontalSeparator(self.widget_10m)
        self.customHorizontalSeparator_13.setObjectName(u"customHorizontalSeparator_13")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_13)

        self.label_5 = QLabel(self.widget_10m)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.label_5)

        self.customHorizontalSeparator_17 = QCustomHorizontalSeparator(self.widget_10m)
        self.customHorizontalSeparator_17.setObjectName(u"customHorizontalSeparator_17")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_17)

        self.label_20 = QLabel(self.widget_10m)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20)

        self.customHorizontalSeparator_18 = QCustomHorizontalSeparator(self.widget_10m)
        self.customHorizontalSeparator_18.setObjectName(u"customHorizontalSeparator_18")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_18)

        self.label_21 = QLabel(self.widget_10m)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_8.addWidget(self.label_21)


        self.horizontalLayout_8.addWidget(self.widget_10m)


        self.verticalLayout.addWidget(self.widget_7)


        self.retranslateUi(SettingsComponent)

        QMetaObject.connectSlotsByName(SettingsComponent)
    # setupUi

    def retranslateUi(self, SettingsComponent):
        SettingsComponent.setWindowTitle(QCoreApplication.translate("SettingsComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("SettingsComponent", u"Settings", None))
        self.welcomeMessage.setText(QCoreApplication.translate("SettingsComponent", u"Customize your security and application preferences.", None))
        self.saveSettingsBtn.setText(QCoreApplication.translate("SettingsComponent", u"Save Settings", None))
        self.resetSettingsBtn.setText(QCoreApplication.translate("SettingsComponent", u"Restore Default", None))
        self.label.setText(QCoreApplication.translate("SettingsComponent", u"General Settings", None))
        self.label_3.setText(QCoreApplication.translate("SettingsComponent", u" Auto-lock timer:", None))
        self.autoLockComboBox.setItemText(0, QCoreApplication.translate("SettingsComponent", u"30", None))
        self.autoLockComboBox.setItemText(1, QCoreApplication.translate("SettingsComponent", u"1", None))
        self.autoLockComboBox.setItemText(2, QCoreApplication.translate("SettingsComponent", u"5", None))
        self.autoLockComboBox.setItemText(3, QCoreApplication.translate("SettingsComponent", u"10", None))
        self.autoLockComboBox.setItemText(4, QCoreApplication.translate("SettingsComponent", u"Never", None))

        self.label_6.setText(QCoreApplication.translate("SettingsComponent", u"min", None))
        self.label_19.setText(QCoreApplication.translate("SettingsComponent", u"Language", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("SettingsComponent", u"English", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("SettingsComponent", u"Spanish", None))

        self.label_17.setText(QCoreApplication.translate("SettingsComponent", u"Set Theme", None))
        self.label_15.setText(QCoreApplication.translate("SettingsComponent", u"Enable breach alerts", None))
        self.label_2.setText(QCoreApplication.translate("SettingsComponent", u" Enable clipboard expiration notifications", None))
        self.label_29.setText(QCoreApplication.translate("SettingsComponent", u"Vault Settings", None))
        self.label_26.setText(QCoreApplication.translate("SettingsComponent", u" Default encryption method", None))
        self.encryptionComboBox.setItemText(0, QCoreApplication.translate("SettingsComponent", u"AES-256", None))
        self.encryptionComboBox.setItemText(1, QCoreApplication.translate("SettingsComponent", u"ChaCha20", None))
        self.encryptionComboBox.setItemText(2, QCoreApplication.translate("SettingsComponent", u"PBKDF2", None))

        self.label_28.setText(QCoreApplication.translate("SettingsComponent", u" Backup Vault", None))
        self.exportVaultBtn.setText(QCoreApplication.translate("SettingsComponent", u"Export Encrypted Vault", None))
        self.lastBackupLabel.setText(QCoreApplication.translate("SettingsComponent", u"Last backup: \"3 days ago\"", None))
        self.importVaultBtn.setText(QCoreApplication.translate("SettingsComponent", u"Import Encrypted Vault", None))
        self.label_31.setText(QCoreApplication.translate("SettingsComponent", u" Sync  Vault", None))
        self.syncVaultBtn.setText(QCoreApplication.translate("SettingsComponent", u"Sync Now", None))
        self.lastSyncLabel.setText(QCoreApplication.translate("SettingsComponent", u" Last synced: \u201c5 mins ago\u201d", None))
        self.label_22.setText(QCoreApplication.translate("SettingsComponent", u"Clipboard & Password Behavior", None))
        self.label_23.setText(QCoreApplication.translate("SettingsComponent", u"Clipboard expiration time", None))
        self.clipboardComboBox.setItemText(0, QCoreApplication.translate("SettingsComponent", u"1", None))
        self.clipboardComboBox.setItemText(1, QCoreApplication.translate("SettingsComponent", u"5", None))
        self.clipboardComboBox.setItemText(2, QCoreApplication.translate("SettingsComponent", u"10", None))
        self.clipboardComboBox.setItemText(3, QCoreApplication.translate("SettingsComponent", u"30", None))
        self.clipboardComboBox.setItemText(4, QCoreApplication.translate("SettingsComponent", u"Never", None))

        self.label_24.setText(QCoreApplication.translate("SettingsComponent", u"min", None))
        self.label_25.setText(QCoreApplication.translate("SettingsComponent", u"Clear clipboard on app close", None))
        self.label_7.setText(QCoreApplication.translate("SettingsComponent", u"Advanced / Developer Settings", None))
        self.label_16.setText(QCoreApplication.translate("SettingsComponent", u" Master Password", None))
        self.changePasswordBtn.setText(QCoreApplication.translate("SettingsComponent", u"Change Master Password", None))
        self.label_3h_2.setText(QCoreApplication.translate("SettingsComponent", u"Destructive action!", None))
        self.resetVaultBtn.setText(QCoreApplication.translate("SettingsComponent", u"Reset Vault Data", None))
        self.label_8.setText(QCoreApplication.translate("SettingsComponent", u"About Section", None))
        self.label_5.setText(QCoreApplication.translate("SettingsComponent", u"App Version: v1.0.0", None))
        self.label_20.setText(QCoreApplication.translate("SettingsComponent", u"Last Update ., \"May 2025\"", None))
        self.label_21.setText(QCoreApplication.translate("SettingsComponent", u"Links: [Terms of Service] [Privacy Policy] [GitHub] [Website]", None))
    # retranslateUi


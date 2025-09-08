# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Footer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
class Ui_FooterComponent(object):
    def setupUi(self, FooterComponent):
        if not FooterComponent.objectName():
            FooterComponent.setObjectName(u"FooterComponent")
        FooterComponent.resize(604, 300)
        self.horizontalLayout = QHBoxLayout(FooterComponent)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(FooterComponent)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/user-lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.autoLockLabel = QLabel(self.widget)
        self.autoLockLabel.setObjectName(u"autoLockLabel")

        self.horizontalLayout_2.addWidget(self.autoLockLabel)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_2 = QWidget(FooterComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.clipboardStatusLabel = QPushButton(self.widget_2)
        self.clipboardStatusLabel.setObjectName(u"clipboardStatusLabel")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/clipboard-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clipboardStatusLabel.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.clipboardStatusLabel)

        self.lastSyncedLabel = QPushButton(self.widget_2)
        self.lastSyncedLabel.setObjectName(u"lastSyncedLabel")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/cloud_sync.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lastSyncedLabel.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.lastSyncedLabel)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_3 = QWidget(FooterComponent)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.versionLabel = QPushButton(self.widget_3)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout_4.addWidget(self.versionLabel)


        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(FooterComponent)

        QMetaObject.connectSlotsByName(FooterComponent)
    # setupUi

    def retranslateUi(self, FooterComponent):
        FooterComponent.setWindowTitle(QCoreApplication.translate("FooterComponent", u"CustomComponent", None))
        self.pushButton.setText("")
        self.autoLockLabel.setText(QCoreApplication.translate("FooterComponent", u"Auto-lock in 2:30 min", None))
        self.clipboardStatusLabel.setText(QCoreApplication.translate("FooterComponent", u"Clipboard status", None))
        self.lastSyncedLabel.setText(QCoreApplication.translate("FooterComponent", u"Last synced: 2 min ago", None))
        self.versionLabel.setText(QCoreApplication.translate("FooterComponent", u"v1.0.0", None))
    # retranslateUi


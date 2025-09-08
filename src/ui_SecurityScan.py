# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_SecurityScan.ui'
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
from Custom_Widgets.QCustomProgressBars import QCustomRoundProgressBar
from Custom_Widgets.QCustomVerticalSeparator import QCustomVerticalSeparator
class Ui_SecurityScanComponent(object):
    def setupUi(self, SecurityScanComponent):
        if not SecurityScanComponent.objectName():
            SecurityScanComponent.setObjectName(u"SecurityScanComponent")
        SecurityScanComponent.resize(1010, 716)
        SecurityScanComponent.setMinimumSize(QSize(1010, 716))
        self.verticalLayout = QVBoxLayout(SecurityScanComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(SecurityScanComponent)
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
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.securityScanBtn = QPushButton(self.frame_2)
        self.securityScanBtn.setObjectName(u"securityScanBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/radar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.securityScanBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.securityScanBtn)

        self.addBtn = QPushButton(self.frame_2)
        self.addBtn.setObjectName(u"addBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.addBtn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.customHorizontalSeparator_3 = QCustomHorizontalSeparator(SecurityScanComponent)
        self.customHorizontalSeparator_3.setObjectName(u"customHorizontalSeparator_3")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_3)

        self.widget_2 = QWidget(SecurityScanComponent)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.customVerticalSeparator = QCustomVerticalSeparator(self.widget_2)
        self.customVerticalSeparator.setObjectName(u"customVerticalSeparator")

        self.horizontalLayout_4.addWidget(self.customVerticalSeparator)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(300, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.customHorizontalSeparator_8 = QCustomHorizontalSeparator(self.widget_6)
        self.customHorizontalSeparator_8.setObjectName(u"customHorizontalSeparator_8")

        self.verticalLayout_5.addWidget(self.customHorizontalSeparator_8)

        self.vaultScoreProgressBar = QCustomRoundProgressBar(self.widget_6)
        self.vaultScoreProgressBar.setObjectName(u"vaultScoreProgressBar")
        self.vaultScoreProgressBar.setMinimumSize(QSize(100, 100))
        self.vaultScoreProgressBar.setMaximumSize(QSize(100, 100))
        self.vaultScoreProgressBar.setProperty("value", 40)

        self.verticalLayout_5.addWidget(self.vaultScoreProgressBar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.vaultScoreLabel = QLabel(self.widget_6)
        self.vaultScoreLabel.setObjectName(u"vaultScoreLabel")
        font1 = QFont()
        font1.setItalic(True)
        self.vaultScoreLabel.setFont(font1)
        self.vaultScoreLabel.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.vaultScoreLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.customHorizontalSeparator_10 = QCustomHorizontalSeparator(self.widget_6)
        self.customHorizontalSeparator_10.setObjectName(u"customHorizontalSeparator_10")

        self.verticalLayout_5.addWidget(self.customHorizontalSeparator_10)

        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.weakPassLabel = QLabel(self.frame_5)
        self.weakPassLabel.setObjectName(u"weakPassLabel")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.weakPassLabel.setFont(font3)
        self.weakPassLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.weakPassLabel)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.widget_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.reusedPassLabel = QLabel(self.frame_10)
        self.reusedPassLabel.setObjectName(u"reusedPassLabel")
        sizePolicy.setHeightForWidth(self.reusedPassLabel.sizePolicy().hasHeightForWidth())
        self.reusedPassLabel.setSizePolicy(sizePolicy)
        self.reusedPassLabel.setFont(font3)
        self.reusedPassLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.reusedPassLabel)

        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_13.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.widget_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.oldPassLabel = QLabel(self.frame_9)
        self.oldPassLabel.setObjectName(u"oldPassLabel")
        self.oldPassLabel.setFont(font3)
        self.oldPassLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.oldPassLabel)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_12.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.customHorizontalSeparator_9 = QCustomHorizontalSeparator(self.widget_6)
        self.customHorizontalSeparator_9.setObjectName(u"customHorizontalSeparator_9")

        self.verticalLayout_5.addWidget(self.customHorizontalSeparator_9)

        self.frame_4 = QFrame(self.widget_6)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.breachLabel = QLabel(self.frame_4)
        self.breachLabel.setObjectName(u"breachLabel")
        self.breachLabel.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.breachLabel)

        self.viewBreachBtn = QPushButton(self.frame_4)
        self.viewBreachBtn.setObjectName(u"viewBreachBtn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewBreachBtn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.viewBreachBtn)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.widget_6)

        self.customVerticalSeparator_2 = QCustomVerticalSeparator(self.widget_2)
        self.customVerticalSeparator_2.setObjectName(u"customVerticalSeparator_2")

        self.horizontalLayout_4.addWidget(self.customVerticalSeparator_2)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.widget)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator_2)

        self.donutChartContainer = QFrame(self.widget)
        self.donutChartContainer.setObjectName(u"donutChartContainer")
        self.donutChartContainer.setMinimumSize(QSize(200, 200))
        self.donutChartContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.donutChartContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.donutChartContainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_4.addWidget(self.donutChartContainer)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout.addWidget(self.widget_2)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(SecurityScanComponent)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout.addWidget(self.customHorizontalSeparator)

        self.widget_7 = QWidget(SecurityScanComponent)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_10m = QWidget(self.widget_7)
        self.widget_10m.setObjectName(u"widget_10m")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10m)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget_10m)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.customHorizontalSeparator_13 = QCustomHorizontalSeparator(self.widget_10m)
        self.customHorizontalSeparator_13.setObjectName(u"customHorizontalSeparator_13")

        self.verticalLayout_8.addWidget(self.customHorizontalSeparator_13)

        self.frame_8 = QFrame(self.widget_10m)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.generateReportBtn = QPushButton(self.frame_8)
        self.generateReportBtn.setObjectName(u"generateReportBtn")

        self.horizontalLayout_11.addWidget(self.generateReportBtn)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.horizontalLayout_8.addWidget(self.widget_10m)


        self.verticalLayout.addWidget(self.widget_7)


        self.retranslateUi(SecurityScanComponent)

        QMetaObject.connectSlotsByName(SecurityScanComponent)
    # setupUi

    def retranslateUi(self, SecurityScanComponent):
        SecurityScanComponent.setWindowTitle(QCoreApplication.translate("SecurityScanComponent", u"CustomComponent", None))
        self.welcomeName.setText(QCoreApplication.translate("SecurityScanComponent", u"Security Center", None))
        self.welcomeMessage.setText(QCoreApplication.translate("SecurityScanComponent", u"Review the health and security of your saved credentials.", None))
#if QT_CONFIG(statustip)
        self.securityScanBtn.setStatusTip(QCoreApplication.translate("SecurityScanComponent", u"Scan", None))
#endif // QT_CONFIG(statustip)
        self.securityScanBtn.setText("")
        self.addBtn.setText("")
        self.label.setText(QCoreApplication.translate("SecurityScanComponent", u"Vault Health Score", None))
        self.vaultScoreLabel.setText(QCoreApplication.translate("SecurityScanComponent", u"Your vault is in good condition. 12 passwords need attention.", None))
        self.label_4.setText(QCoreApplication.translate("SecurityScanComponent", u" Warnings and Alerts Section", None))
        self.label_9.setText(QCoreApplication.translate("SecurityScanComponent", u"Weak Passwords:", None))
        self.weakPassLabel.setText(QCoreApplication.translate("SecurityScanComponent", u"2", None))
        self.pushButton.setText(QCoreApplication.translate("SecurityScanComponent", u"View", None))
        self.label_13.setText(QCoreApplication.translate("SecurityScanComponent", u"Reused Passwords", None))
        self.reusedPassLabel.setText(QCoreApplication.translate("SecurityScanComponent", u"13", None))
        self.pushButton_5.setText(QCoreApplication.translate("SecurityScanComponent", u"View", None))
        self.label_11.setText(QCoreApplication.translate("SecurityScanComponent", u"Old Passwords (>6 months)", None))
        self.oldPassLabel.setText(QCoreApplication.translate("SecurityScanComponent", u"32", None))
        self.pushButton_2.setText(QCoreApplication.translate("SecurityScanComponent", u"View", None))
        self.breachLabel.setText(QCoreApplication.translate("SecurityScanComponent", u"5 credentials exposed in breaches", None))
        self.viewBreachBtn.setText(QCoreApplication.translate("SecurityScanComponent", u"View Details", None))
        self.label_3.setText(QCoreApplication.translate("SecurityScanComponent", u"Vault Summary", None))
        self.label_8.setText(QCoreApplication.translate("SecurityScanComponent", u"Security Audit Report", None))
        self.label_5.setText(QCoreApplication.translate("SecurityScanComponent", u"Exports or displays a PDF-style summary:", None))
        self.generateReportBtn.setText(QCoreApplication.translate("SecurityScanComponent", u"Generate Full Audit", None))
    # retranslateUi

